# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxImageOrVideo = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxImageOrVideo.setGeometry(QtCore.QRect(10, 10, 581, 384))
        self.groupBoxImageOrVideo.setAutoFillBackground(True)
        self.groupBoxImageOrVideo.setObjectName("groupBoxImageOrVideo")
        self.labelImageOrVideo = QtWidgets.QLabel(self.groupBoxImageOrVideo)
        self.labelImageOrVideo.setGeometry(QtCore.QRect(10, 20, 561, 351))
        self.labelImageOrVideo.setAutoFillBackground(True)
        self.labelImageOrVideo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.labelImageOrVideo.setText("")
        self.labelImageOrVideo.setTextFormat(QtCore.Qt.AutoText)
        self.labelImageOrVideo.setPixmap(QtGui.QPixmap("src/default.png"))
        self.labelImageOrVideo.setScaledContents(True)
        self.labelImageOrVideo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImageOrVideo.setObjectName("labelImageOrVideo")
        self.groupBoxLog = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxLog.setGeometry(QtCore.QRect(10, 400, 581, 141))
        self.groupBoxLog.setAutoFillBackground(True)
        self.groupBoxLog.setObjectName("groupBoxLog")
        self.textLog = QtWidgets.QTextBrowser(self.groupBoxLog)
        self.textLog.setGeometry(QtCore.QRect(10, 20, 561, 111))
        self.textLog.setObjectName("textLog")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuLoadLocalFile = QtWidgets.QMenu(self.menuFile)
        self.menuLoadLocalFile.setObjectName("menuLoadLocalFile")
        self.menuCamera = QtWidgets.QMenu(self.menubar)
        self.menuCamera.setObjectName("menuCamera")
        self.menuActions = QtWidgets.QMenu(self.menubar)
        self.menuActions.setObjectName("menuActions")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionCloseCamera = QtWidgets.QAction(MainWindow)
        self.actionCloseCamera.setObjectName("actionCloseCamera")
        self.actionLoadImage = QtWidgets.QAction(MainWindow)
        self.actionLoadImage.setObjectName("actionLoadImage")
        self.actionLoadVideo = QtWidgets.QAction(MainWindow)
        self.actionLoadVideo.setObjectName("actionLoadVideo")
        self.actionStart = QtWidgets.QAction(MainWindow)
        self.actionStart.setObjectName("actionStart")
        self.actionLoop = QtWidgets.QAction(MainWindow)
        self.actionLoop.setObjectName("actionLoop")
        self.actionOpenCamera = QtWidgets.QAction(MainWindow)
        self.actionOpenCamera.setObjectName("actionOpenCamera")
        self.actionSelectedCamera = QtWidgets.QAction(MainWindow)
        self.actionSelectedCamera.setObjectName("actionSelectedCamera")
        self.actionVideoFPS = QtWidgets.QAction(MainWindow)
        self.actionVideoFPS.setObjectName("actionVideoFPS")
        self.actionpowered_by_515code_com = QtWidgets.QAction(MainWindow)
        self.actionpowered_by_515code_com.setObjectName("actionpowered_by_515code_com")
        self.actionMosaicLevel = QtWidgets.QAction(MainWindow)
        self.actionMosaicLevel.setObjectName("actionMosaicLevel")
        self.menuLoadLocalFile.addAction(self.actionLoadImage)
        self.menuLoadLocalFile.addAction(self.actionLoadVideo)
        self.menuFile.addAction(self.menuLoadLocalFile.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuCamera.addAction(self.actionOpenCamera)
        self.menuCamera.addAction(self.actionCloseCamera)
        self.menuCamera.addAction(self.actionSelectedCamera)
        self.menuActions.addAction(self.actionStart)
        self.menuSettings.addAction(self.actionVideoFPS)
        self.menuSettings.addAction(self.actionLoop)
        self.menuSettings.addAction(self.actionMosaicLevel)
        self.menu.addAction(self.actionpowered_by_515code_com)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuCamera.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBoxImageOrVideo.setTitle(_translate("MainWindow", "图片/视频"))
        self.groupBoxLog.setTitle(_translate("MainWindow", "日志"))
        self.menuFile.setTitle(_translate("MainWindow", "文件"))
        self.menuLoadLocalFile.setTitle(_translate("MainWindow", "导入"))
        self.menuCamera.setTitle(_translate("MainWindow", "摄像头"))
        self.menuActions.setTitle(_translate("MainWindow", "操作"))
        self.menuSettings.setTitle(_translate("MainWindow", "设置"))
        self.menu.setTitle(_translate("MainWindow", "关于"))
        self.actionExit.setText(_translate("MainWindow", "关闭窗口"))
        self.actionCloseCamera.setText(_translate("MainWindow", "关闭"))
        self.actionLoadImage.setText(_translate("MainWindow", "图片"))
        self.actionLoadVideo.setText(_translate("MainWindow", "视频"))
        self.actionStart.setText(_translate("MainWindow", "开始打码"))
        self.actionLoop.setText(_translate("MainWindow", "视频循环 (关)"))
        self.actionOpenCamera.setText(_translate("MainWindow", "打开"))
        self.actionSelectedCamera.setText(_translate("MainWindow", "切换摄像头"))
        self.actionVideoFPS.setText(_translate("MainWindow", "设置fps"))
        self.actionpowered_by_515code_com.setText(_translate("MainWindow", "powered by 515code.com"))
        self.actionMosaicLevel.setText(_translate("MainWindow", "模糊程度"))
