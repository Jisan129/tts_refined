# -*- coding: utf-8 -*-
# !/usr/bin/env python


import threading
import pygame
import uno
import io
import requests
import re
import getpass
from pydub import AudioSegment
from io import BytesIO
import numpy as np
from com.sun.star.awt.MessageBoxButtons import BUTTONS_OK, BUTTONS_OK_CANCEL, BUTTONS_YES_NO, BUTTONS_YES_NO_CANCEL, \
    BUTTONS_RETRY_CANCEL, BUTTONS_ABORT_IGNORE_RETRY
from com.sun.star.awt.MessageBoxButtons import DEFAULT_BUTTON_OK, DEFAULT_BUTTON_CANCEL, DEFAULT_BUTTON_RETRY, \
    DEFAULT_BUTTON_YES, DEFAULT_BUTTON_NO, DEFAULT_BUTTON_IGNORE
from com.sun.star.awt.MessageBoxType import MESSAGEBOX, INFOBOX, WARNINGBOX, ERRORBOX, QUERYBOX
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

try:
    from tts_writer_UI import tts_writer_UI
except:
    from pythonpath.tts_writer_UI import tts_writer_UI
FLAG_TEST = True
MAX_WORDS = 20
MAX_RETRY_COUNT = 5
FOOL = "ok"
URL = "https://stt.bangla.gov.bd:9381/utils"
HEADERS = {"Content-Type": "application/json"}
response_audios = {}
is_playing = [False]
main_chunks = []
lock = threading.Lock()
gender = ["Male"]
flag = [1]
app = None;
resumeFlag = [1]
download_chunk = []
concentrated_bytes = None;
username = getpass.getuser();
download_file = f"/home/{username}/Documents/TTS_Download_File";
pause_event = threading.Event()

pause_threads = threading.Event()
pause_threads.set()

pygame.init()
pygame.mixer.init()


def tempFunc():
    pass


class tts_writer(tts_writer_UI):
    '''
    Class documentation...
    '''

    def __init__(self, flag=False, ctx=uno.getComponentContext(), **kwargs):
        self.ctx = ctx
        tts_writer_UI.__init__(self, flag, self.ctx)

        # for key, value in kwargs.items():
        # if key == 'document':
        # self.document = value

        # --------- my code ---------------------

        self.DialogModel.Title = "TTS Writer Extension"
        # mri(self.ctx, self.DialogContainer)

    def myFunction(self):
        # TODO: not implemented
        pass

    # --------- helpers ---------------------

    def messageBox(self, MsgText, MsgTitle, MsgType=MESSAGEBOX, MsgButtons=BUTTONS_OK):
        sm = self.ctx.ServiceManager
        si = sm.createInstanceWithContext("com.sun.star.awt.Toolkit", self.ctx)
        mBox = si.createMessageBox(self.Toolkit, MsgType, MsgButtons, MsgTitle, MsgText)
        mBox.execute()

    # -----------------------------------------------------------
    #               Execute dialog
    # -----------------------------------------------------------

    def showDialog(self):
        global app
        app = self
        self.DialogContainer.setVisible(True)
        self.DialogContainer.createPeer(self.Toolkit, None)
        xWindow = uno.getClass("com.sun.star.awt.XWindow")
        dialog_window = uno.QueryInterface(xWindow, self.DialogContainer)
        dialog_window.setVisible(True)
        self.DialogContainer.execute()

    '''
        xWindow = uno.getClass("com.sun.star.awt.XWindow")
        dialog_window = uno.QueryInterface(xWindow, self.DialogContainer)
        dialog_window.setVisible(True) 
    '''

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def textButton_OnClick(self):
        tts_writer_UI.new_flag = False

    def ssmlButton_OnClick(self):
        tts_writer_UI.new_flag = True
        print("onclick")
        print(tts_writer_UI.new_flag)

    def ansiButton_OnClick(self):
        pass

    def unicodeButton_OnClick(self):
        pass

    def startButton_OnClick(self):
        a = flag.pop()
        result = a % 3
        print(result)
        pygame.mixer.init()

        if result == 1:
            result += 1

            try:
                ctx = remote_ctx  # IDE
            except:
                ctx = uno.getComponentContext()  # UI

            desktop = ctx.getByName("/singletons/com.sun.star.frame.theDesktop")

            # get document
            document = desktop.getCurrentComponent()
            text = document.Text
            content = text.getString()
            print(content)
            if document is not None:
                combined_text = None
                combined_text = content
                main_thread = threading.Thread(target=self.proxy, args=(combined_text,))
                main_thread.start()
            self.startButton.Label = "Pause"
            self.ansiButton.Enabled=False
            self.unicodeButton.Enabled=False
            self.femaleButton.Enabled=False
            self.maleButton.Enabled=False
            self.clearButton.Enabled=False

        elif result == 2:
            pygame.mixer.pause()
            result += 1
            self.startButton.Label = "Resume"

        elif result == 0:
            pygame.mixer.unpause()
            result += 2
            self.startButton.Label = "Pause"
        flag.append(result)

    def stopButton_OnClick(self):
        pygame.mixer.stop()
        resumeFlag.append(0)
        flag.pop()
        flag.append(1)
        clear_variables()
        self.startButton.Label = "Play"
        self.ansiButton.Enabled = True
        self.unicodeButton.Enabled = True
        self.femaleButton.Enabled = True
        self.maleButton.Enabled = True
        self.clearButton.Enabled=True
        

    def clearButton_OnClick(self):
        audio_segments = []
        for audio_bytes in download_chunk:
            audio_segment = AudioSegment.from_file(io.BytesIO(audio_bytes))
            audio_segments.append(audio_segment)

        # Concatenate all the audio segments into one
        final_audio = sum(audio_segments)

        # Save the concatenated audio as an audio file (e.g., WAV or MP3)
        final_audio.export(download_file, format="wav")
        self.messageBox("Audio downloaded to Documents Folder", "Download Completed", INFOBOX)

    def proxy(self, main_text):
        print(main_text)
        clear_variables()
        chunks = re.split(r'[\r\n।?!,;—:`’‘\']+', main_text)
        chunks = list(filter(lambda token: token.strip() != "", chunks))
        for chunk in chunks:
            create_chunk_array(chunk)

        threads = []
        for chunk in main_chunks:
            thread = threading.Thread(target=send_and_receive_chunk, args=(chunk,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        play_audios()

    def closeButton_OnClick(self):
        self.DialogContainer.dispose()

        # TODO: not implemented

    def resumeButton_OnClick(self):
        pygame.mixer.unpause()
        self.femaleButton_OnClick()

    def maleButton_OnClick(self):
        self.disableButtons()

    def femaleButton_OnClick(self):

        a = flag.pop()
        result = a % 2
        flag.append(0)
        pygame.mixer.unpause()
        self.startButton.Label = "Pause"

def disableButtons():
    app.ansiButton.Enabled = False
    app.unicodeButton.Enabled = False
    app.maleButton.Enabled = False
    app.femaleButton.Enabled = False
    app.pitchBox.Enabled = False
    app.speedBox.Enabled = False
    app.maleDrop.Enabled = False
    app.femaleDrop.Enabled = False


def enableButtons():
    app.unicodeButton.Enabled = True
    app.ansiButton.Enabled = True
    app.maleButton.Enabled = True
    app.ssmlButton.Enabled = True
    app.femaleButton.Enabled = True
    app.maleDrop.Enabled = True
    app.femaleDrop.Enabled = True
    app.pitchBox.Enabled = True
    app.speedBox.Enabled = True
    app.startButton.Label = "Play"
    app.clearButton.Label = "Download"

    def main_chunkify(main_text):
        clear_variables()
        chunks = re.split(r'[\r\n।?!,;—:`’‘\']+', main_text)
        chunks = list(filter(lambda token: token.strip() != "", chunks))
        for chunk in chunks:
            create_chunk_array(chunk)

        threads = []
        for chunk in main_chunks:
            thread = threading.Thread(target=send_and_receive_chunk, args=(chunk,))
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        play_audios()


def create_chunk_array(chunk):
    words = chunk.strip().split(" ")

    if len(words) > MAX_WORDS:
        word_chunks = split_long_words(words, MAX_WORDS)
        for word_chunk in word_chunks:
            main_chunks.append(word_chunk)
    else:
        main_chunks.append(chunk)


def split_long_words(words, max_words):
    word_chunks = []
    current_word_chunk = ""

    for word in words:
        if len((current_word_chunk + word).split(" ")) <= max_words:
            current_word_chunk += word + " "
        else:
            if current_word_chunk != "":
                word_chunks.append(current_word_chunk.strip())
                current_word_chunk = ""
            word_chunks.append(word)

    if current_word_chunk != "":
        word_chunks.append(current_word_chunk.strip())

    return word_chunks


def send_request(text):
    retry_count = 0
    response = None
    while retry_count < MAX_RETRY_COUNT:
        try:
            response = requests.post(URL, headers=HEADERS,
                                     json={
                                         "text": text, "module": "backend_tts", "submodule": "infer"},
                                     verify=False)
            if response.ok:
                break
        except requests.exceptions.RequestException as error:
            print(error)
        retry_count += 1
    return response


def send_and_receive_chunk(chunk):
    response = send_request(chunk)
    if response and response.ok:
        print("Response received")

        audio_data = response.content;
        download_chunk.append(audio_data)

        audio = AudioSegment.from_file(BytesIO(audio_data))
        with lock:
            response_audios[chunk] = audio
        if chunk == main_chunks[0]:
            play_audio(chunk)


# TODO: not implemented
def pause_audio():
    pause_event.set()


# To resume audio playback
def resume_audio():
    pause_event.clear()


def play_audio(chunk):
    if not is_playing[0] and chunk in response_audios:
        is_playing[0] = True
        with lock:
            audio = response_audios.pop(chunk)
        if audio.channels != 2:
            audio = audio.set_channels(2)
        audio = audio.set_frame_rate(44100)  # Convert AudioSegment to a NumP array
        audio_array = np.array(audio.get_array_of_samples()).reshape(-1, 2)
        sound = pygame.sndarray.make_sound(audio_array)  # Play the sound
        sound.play()

        # play(audio)
        while pygame.mixer.get_busy():
            pygame.time.Clock().tick(10)  # Limit the loop's speed to avoid high CPU usage
        is_playing[0] = False


def play_audios():
    for chunk in main_chunks[1:]:
        if not is_playing[0] and chunk in response_audios:
            play_audio(chunk)
        else:
            # Sleep to avoid busy waiting
            threading.Event().wait(0.1)


def clear_variables():
    response_audios.clear()
    is_playing[0] = False
    main_chunks.clear()


# Usage example


def Run_tts_writer(*args):
    try:
        ctx = uno.getComponentContext()  # UI

        # get desktop
        desktop = ctx.getByName("/singletons/com.sun.star.frame.theDesktop")

        # get document
        document = desktop.getCurrentComponent()

        app = tts_writer(ctx=ctx)
        app.showDialog()
    except Exception:
        pass


# Execute macro from LibreOffice UI (Tools - Macro)
g_exportedScripts = Run_tts_writer,

# -------------------------------------
# HELPER FOR AN IDE
# -------------------------------------

if __name__ == "__main__":
    """ Connect to LibreOffice proccess.
    1) Start the office in shell with command:
    soffice "--accept=socket,host=127.0.0.1,port=2002,tcpNoDelay=1;urp;StarOffice.ComponentContext" --norestore
    2) Run script
    """
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__), 'pythonpath'))

    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstance("com.sun.star.bridge.UnoUrlResolver")
    try:
        remote_ctx = resolver.resolve("uno:socket,"
                                      "host=127.0.0.1,"
                                      "port=2002,"
                                      "tcpNoDelay=1;"
                                      "urp;"
                                      "StarOffice.ComponentContext")
    except Exception as err:
        print(err)

    Run_tts_writer()
'''

    try:
        ctx = remote_ctx  # IDE
    except:
        ctx = uno.getComponentContext()  # UI

    # get desktop
    desktop = ctx.getByName("/singletons/com.sun.star.frame.theDesktop")

    # get document
    document = desktop.getCurrentComponent()

    app = tts_writer(ctx=ctx)
    app.showDialog()

'''

'''
    try:
        ctx = uno.getComponentContext()  # UI

        # get desktop
        desktop = ctx.getByName("/singletons/com.sun.star.frame.theDesktop")

        # get document
        document = desktop.getCurrentComponent()

        app = tts_writer(ctx=ctx)
        app.showDialog()
    except Exception:
        pass

'''
