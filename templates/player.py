# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'player.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.video_frame = QtWidgets.QFrame(self.centralwidget)
        self.video_frame.setAutoFillBackground(True)
        self.video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_frame.setObjectName("video_frame")
        self.verticalLayout.addWidget(self.video_frame)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.subtitle_label_1 = QtWidgets.QLabel(self.centralwidget)
        self.subtitle_label_1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.subtitle_label_1.setObjectName("subtitle_label_1")
        self.horizontalLayout_2.addWidget(self.subtitle_label_1)
        self.subtitle_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.subtitle_label_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.subtitle_label_2.setObjectName("subtitle_label_2")
        self.horizontalLayout_2.addWidget(self.subtitle_label_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.play_slider = QtWidgets.QSlider(self.centralwidget)
        self.play_slider.setOrientation(QtCore.Qt.Horizontal)
        self.play_slider.setObjectName("play_slider")
        self.verticalLayout_2.addWidget(self.play_slider)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.play_button = QtWidgets.QPushButton(self.centralwidget)
        self.play_button.setObjectName("play_button")
        self.horizontalLayout.addWidget(self.play_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sound_slider = QtWidgets.QSlider(self.centralwidget)
        self.sound_slider.setMaximumSize(QtCore.QSize(100, 16777215))
        self.sound_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sound_slider.setObjectName("sound_slider")
        self.horizontalLayout.addWidget(self.sound_slider)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Audio = QtWidgets.QMenu(self.menubar)
        self.menu_Audio.setObjectName("menu_Audio")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.menu_File.addAction(self.actionOpen)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Audio.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.subtitle_label_1.setText(_translate("MainWindow", "1"))
        self.subtitle_label_2.setText(_translate("MainWindow", "2"))
        self.play_button.setText(_translate("MainWindow", "Play/Pause"))
        self.menu_File.setTitle(_translate("MainWindow", "&File"))
        self.menu_Audio.setTitle(_translate("MainWindow", "&Audio"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))

