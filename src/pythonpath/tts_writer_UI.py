# -*- coding: utf-8 -*-
# !/usr/bin/env python

# =============================================================================
#
# Dialog implementation generated from a XDL file.
#
# Created: Sun Jul 16 11:01:57 2023
#      by: unodit 0.8.0
#
# WARNING! All changes made in this file will be overwritten
#          if the file is generated again!
#
# =============================================================================

import uno
import getpass
import unohelper
from com.sun.star.awt import XActionListener
from com.sun.star.task import XJobExecutor


class tts_writer_UI(unohelper.Base, XActionListener, XJobExecutor):
    """
    Class documentation...AAAAAAAAAAAAAAAAAAAAAAA
    """
    new_flag = True;

    def __init__(self, flag=new_flag, ctx=uno.getComponentContext()):
        self.flag = flag
        self.LocalContext = ctx
        self.ServiceManager = self.LocalContext.ServiceManager
        self.Toolkit = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.ExtToolkit", self.LocalContext)

        # -----------------------------------------------------------
        #               Create dialog and insert controls
        # -----------------------------------------------------------

        # --------------create dialog container and set model and properties
        self.DialogContainer = self.ServiceManager.createInstanceWithContext("com.sun.star.awt.UnoControlDialog",
                                                                             self.LocalContext)
        self.DialogModel = self.ServiceManager.createInstance("com.sun.star.awt.UnoControlDialogModel")
        self.DialogContainer.setModel(self.DialogModel)

        self.DialogModel.Name = "TTS Writer Extension"
        self.DialogModel.PositionX = "750"
        self.DialogModel.PositionY = "250"
        self.DialogModel.Width = 180
        self.DialogModel.Height = 320
        self.DialogModel.Closeable = True
        self.DialogModel.Moveable = False
        self.DialogModel.DesktopAsParent = False

        #imagesection
        self.ImageControl1 = self.DialogModel.createInstance("com.sun.star.awt.UnoControlImageControlModel")

        self.ImageControl1.Name = "ImageControl1"
        self.ImageControl1.TabIndex = 1
        self.ImageControl1.PositionX = "20"
        self.ImageControl1.PositionY = "20"
        self.ImageControl1.Width = 140
        self.ImageControl1.Height = 36
        username = getpass.getuser();
        print(f'/home/{username}/Documents/decoded_image.png')
        self.ImageControl1.ImageURL = uno.fileUrlToSystemPath(f"file:///home/{username}/Documents/decoded_image.png")

        # /home/reve/Downloads/download.png
        # inserts the control model into the dialog model

        # Remove the border around the image (optional)

        self.DialogModel.insertByName("ImageControl1", self.ImageControl1)

        # --------- create an instance of Button control, set properties ---
        self.textButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.textButton.Name = "textButton"
        self.textButton.TabIndex = 3
        self.textButton.PositionX = "140"
        self.textButton.PositionY = "134"
        self.textButton.Width = 40
        self.textButton.Height = 15
        self.textButton.Label = "TEXT"
        self.textButton.Toggle = 1
        # self.textButton.FocusOnClick = False
        self.textButton.State = 0

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("textButton", self.textButton)

        # add the action listener
        self.DialogContainer.getControl('textButton').addActionListener(self)
        self.DialogContainer.getControl('textButton').setActionCommand('textButton_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.ssmlButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.ssmlButton.Name = "ssmlButton"
        self.ssmlButton.TabIndex = 17
        self.ssmlButton.PositionX = "180"
        self.ssmlButton.PositionY = "134"
        self.ssmlButton.Width = 40
        self.ssmlButton.Height = 15
        self.ssmlButton.Label = "SSML"
        self.ssmlButton.Toggle = 1
        # self.ssmlButton.FocusOnClick = False
        self.ssmlButton.State = 0

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ssmlButton", self.ssmlButton)

        # add the action listener
        self.DialogContainer.getControl('ssmlButton').addActionListener(self)
        self.DialogContainer.getControl('ssmlButton').setActionCommand('ssmlButton_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.ansiButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.ansiButton.Name = "ansiButton"
        self.ansiButton.TabIndex = 4
        self.ansiButton.PositionX = "55"
        self.ansiButton.PositionY = "134"
        self.ansiButton.Width = 35
        self.ansiButton.Height = 15
        self.ansiButton.Label = "ANSI"
        self.ansiButton.Toggle = 1
        # self.ansiButton.FocusOnClick = False
        self.ansiButton.State = 0

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("ansiButton", self.ansiButton)

        # add the action listener
        self.DialogContainer.getControl('ansiButton').addActionListener(self)
        self.DialogContainer.getControl('ansiButton').setActionCommand('ansiButton_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.unicodeButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.unicodeButton.Name = "unicodeButton"
        self.unicodeButton.TabIndex = 5
        self.unicodeButton.PositionX = "90"
        self.unicodeButton.PositionY = "134"
        self.unicodeButton.Width = 35
        self.unicodeButton.Height = 15
        self.unicodeButton.Label = "UNICODE"
        self.unicodeButton.Toggle = 1
        # self.unicodeButton.FocusOnClick = False
        self.unicodeButton.State = 0

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("unicodeButton", self.unicodeButton)

        # add the action listener
        self.DialogContainer.getControl('unicodeButton').addActionListener(self)
        self.DialogContainer.getControl('unicodeButton').setActionCommand('unicodeButton_OnClick')

        # add the action listener
        self.DialogContainer.getControl('ansiButton').addActionListener(self)
        self.DialogContainer.getControl('ansiButton').setActionCommand('ansiButton_OnClick')

        self.startButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.startButton.Name = "startButton"
        self.startButton.TabIndex = 10
        self.startButton.PositionX = "100"
        self.startButton.PositionY = "91"
        self.startButton.Width = 55
        self.startButton.Height = 20
        self.startButton.Label = "Start"
        self.startButton.FocusOnClick = False

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("startButton", self.startButton)

        # add the action listener
        self.DialogContainer.getControl('startButton').addActionListener(self)
        self.DialogContainer.getControl('startButton').setActionCommand('startButton_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.clearButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.clearButton.Name = "clearButton"
        self.clearButton.TabIndex = 11
        self.clearButton.PositionX = "165"
        self.clearButton.PositionY = "91"
        self.clearButton.Width = 55
        self.clearButton.Height = 20
        self.clearButton.Label = "Download"
        self.clearButton.FocusOnClick = False

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("clearButton", self.clearButton)

        # add the action listener
        self.DialogContainer.getControl('clearButton').addActionListener(self)
        self.DialogContainer.getControl('clearButton').setActionCommand('clearButton_OnClick')

        # --------- create an instance of Button control, set properties ---
        self.closeButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlButtonModel")

        self.closeButton.Name = "closeButton"
        self.closeButton.TabIndex = 12
        self.closeButton.PositionX = "190"
        self.closeButton.PositionY = "16"
        self.closeButton.Width = 30
        self.closeButton.Height = 24
        self.closeButton.Label = "Close"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("closeButton", self.closeButton)

        # add the action listener
        self.DialogContainer.getControl('closeButton').addActionListener(self)
        self.DialogContainer.getControl('closeButton').setActionCommand('closeButton_OnClick')

        self.maleButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.maleButton.Name = "maleButton"
        self.maleButton.TabIndex = 6
        self.maleButton.PositionX = "84"
        self.maleButton.PositionY = "190"
        self.maleButton.Width = 32
        self.maleButton.Height = 30
        self.maleButton.Label = "পুরুষ"
        self.maleButton.State = True

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("maleButton", self.maleButton)

        # add the action listener
        self.DialogContainer.getControl('maleButton').addActionListener(self)
        self.DialogContainer.getControl('maleButton').setActionCommand('maleButton_OnClick')

        # --------- create an instance of RadioButton control, set properties ---
        self.femaleButton = self.DialogModel.createInstance("com.sun.star.awt.UnoControlRadioButtonModel")

        self.femaleButton.Name = "femaleButton"
        self.femaleButton.TabIndex = 7
        self.femaleButton.PositionX = "84"
        self.femaleButton.PositionY = "220"
        self.femaleButton.Width = 30
        self.femaleButton.Height = 30
        self.femaleButton.Label = "নারী"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("femaleButton", self.femaleButton)

        # add the action listener
        self.DialogContainer.getControl('femaleButton').addActionListener(self)
        self.DialogContainer.getControl('femaleButton').setActionCommand('femaleButton_OnClick')

        # --------- create an instance of RadioButton control, set properties ---

        # --------- create an instance of ListBox control, set properties ---
        self.maleDrop = self.DialogModel.createInstance("com.sun.star.awt.UnoControlListBoxModel")

        self.maleDrop.Name = "maleDrop"
        self.maleDrop.TabIndex = 19
        self.maleDrop.PositionX = "130"
        self.maleDrop.PositionY = "188"
        self.maleDrop.Width = 40
        self.maleDrop.Height = 10
        self.maleDrop.Dropdown = True
        self.maleDrop.Align = 1
        self.maleDrop.StringItemList = ('কণ্ঠ ১', 'কণ্ঠ ২')
        self.maleDrop.SelectedItems = ['0']

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("maleDrop", self.maleDrop)

        self.femaleDrop = self.DialogModel.createInstance("com.sun.star.awt.UnoControlListBoxModel")

        self.femaleDrop.Name = "femaleDrop"
        self.femaleDrop.TabIndex = 19
        self.femaleDrop.PositionX = "130"
        self.femaleDrop.PositionY = "225"
        self.femaleDrop.Width = 40
        self.femaleDrop.Height = 10
        self.femaleDrop.Dropdown = True
        self.femaleDrop.Align = 1
        self.femaleDrop.StringItemList = ('কণ্ঠ ১', 'কণ্ঠ ২')
        self.femaleDrop.SelectedItems = ['0']

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("femaleDrop", self.femaleDrop)

        self.speedBox = self.DialogModel.createInstance("com.sun.star.awt.UnoControlListBoxModel")

        self.speedBox.Name = "speedBox"
        self.speedBox.TabIndex = 13
        self.speedBox.PositionX = "57"
        self.speedBox.PositionY = "260"
        self.speedBox.Width = 60
        self.speedBox.Height = 24
        self.speedBox.Dropdown = True
        self.speedBox.Align = 1
        self.speedBox.StringItemList = ('-2X', '-1X', '0', '1X', '2X', '-2X', '-1X', '0', '1X', '2X')
        self.speedBox.SelectedItems = ['2']

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("speedBox", self.speedBox)

        # --------- create an instance of FixedText control, set properties ---
        self.speedLabel = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.speedLabel.Name = "speedLabel"
        self.speedLabel.TabIndex = 15
        self.speedLabel.PositionX = "40"
        self.speedLabel.PositionY = "260"
        self.speedLabel.Width = 24
        self.speedLabel.Height = 18
        self.speedLabel.Label = "গতি"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("speedLabel", self.speedLabel)

        # --------- create an instance of FixedText control, set properties ---
        self.pitchLabel = self.DialogModel.createInstance("com.sun.star.awt.UnoControlFixedTextModel")

        self.pitchLabel.Name = "pitchLabel"
        self.pitchLabel.TabIndex = 16
        self.pitchLabel.PositionX = "135"
        self.pitchLabel.PositionY = "260"
        self.pitchLabel.Width = 24
        self.pitchLabel.Height = 18
        self.pitchLabel.Label = "পিচ"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("pitchLabel", self.pitchLabel)

        self.pitchBox = self.DialogModel.createInstance("com.sun.star.awt.UnoControlListBoxModel")
        self.pitchBox.Name = "pitchBox"
        self.pitchBox.TabIndex = 14
        self.pitchBox.PositionX = "158"
        self.pitchBox.PositionY = "260"
        self.pitchBox.Width = 60
        self.pitchBox.Height = 24
        self.pitchBox.Dropdown = True
        self.pitchBox.Align = 1
        self.pitchBox.StringItemList = ('-2X', '-1X', '0', '1X', '2X', '-2X', '-1X', '0', '1X', '2X')
        self.pitchBox.SelectedItems = ['2']

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("pitchBox", self.pitchBox)

        # dialogbox
        self.kontho = self.DialogModel.createInstance("com.sun.star.awt.UnoControlGroupBoxModel")
        self.kontho.Name = "kontho"
        self.kontho.TabIndex = 51
        self.kontho.PositionX = "40"
        self.kontho.PositionY = "170"
        self.kontho.Width = 180
        self.kontho.Height = 80
        self.kontho.Label = "কণ্ঠ"

        # inserts the control model into the dialog model
        self.DialogModel.insertByName("kontho", self.kontho)

    # -----------------------------------------------------------
    #               Action events
    # -----------------------------------------------------------

    def actionPerformed(self, oActionEvent):
        if oActionEvent.ActionCommand == 'textButton_OnClick':
            if self.textButton.State == 1:
                self.ssmlButton.State = 0
            else:
                self.ssmlButton.State = 1
            self.textButton_OnClick()

        if oActionEvent.ActionCommand == 'ssmlButton_OnClick':
            if self.ssmlButton.State == 1:
                self.textButton.State = 0
            else:
                self.textButton.State = 1
            self.ssmlButton_OnClick()

        if oActionEvent.ActionCommand == 'ansiButton_OnClick':
            self.unicodeButton.State = 0 if self.ansiButton.State == 1 else 1
            self.ansiButton_OnClick()

        if oActionEvent.ActionCommand == 'startButton_OnClick':
            self.startButton_OnClick()

        if oActionEvent.ActionCommand == 'clearButton_OnClick':
            self.clearButton_OnClick()

        if oActionEvent.ActionCommand == 'closeButton_OnClick':
            self.closeButton_OnClick()

        if oActionEvent.ActionCommand == 'unicodeButton_OnClick':
            self.ansiButton.State = 0 if self.unicodeButton.State == 1 else 1
            self.unicodeButton_OnClick()

        if oActionEvent.ActionCommand == 'maleButton_OnClick':
            self.maleButton_OnClick()

        if oActionEvent.ActionCommand == 'femaleButton_OnClick':
            self.femaleButton_OnClick()

# ----------------- END GENERATED CODE ----------------------------------------
