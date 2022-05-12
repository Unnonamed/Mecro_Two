# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(481, 556)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actioTrans = QAction(MainWindow)
        self.actioTrans.setObjectName(u"actioTrans")
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton_capture = QPushButton(self.centralwidget)
        self.pushButton_capture.setObjectName(u"pushButton_capture")
        self.pushButton_capture.setGeometry(QRect(380, 0, 91, 31))
        self.checkBox_capture = QCheckBox(self.centralwidget)
        self.checkBox_capture.setObjectName(u"checkBox_capture")
        self.checkBox_capture.setGeometry(QRect(260, 0, 116, 31))
        self.checkBox_start = QCheckBox(self.centralwidget)
        self.checkBox_start.setObjectName(u"checkBox_start")
        self.checkBox_start.setGeometry(QRect(180, 0, 76, 31))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 461, 471))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.textEdit_clip = QTextEdit(self.layoutWidget)
        self.textEdit_clip.setObjectName(u"textEdit_clip")

        self.verticalLayout.addWidget(self.textEdit_clip)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.textEdit_trans = QTextEdit(self.layoutWidget)
        self.textEdit_trans.setObjectName(u"textEdit_trans")

        self.verticalLayout.addWidget(self.textEdit_trans)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 481, 22))
        self.menu_option = QMenu(self.menubar)
        self.menu_option.setObjectName(u"menu_option")
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName(u"menu_view")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_start = QMenu(self.menubar)
        self.menu_start.setObjectName(u"menu_start")
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_start.menuAction())
        self.menubar.addAction(self.menu_option.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_option.addAction(self.actioTrans)
        self.menu_help.addAction(self.actionhelp)
        self.menu_file.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ud654\uba74\ucea1\uccd0_ver1.0.0", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actioTrans.setText(QCoreApplication.translate("MainWindow", u"\ud22c\uba85\ub3c4\uc124\uc815", None))
        self.actionhelp.setText(QCoreApplication.translate("MainWindow", u"\uc815\ubcf4(Info)", None))
        self.pushButton_capture.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc601\uc5ed", None))
        self.checkBox_capture.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0 \uc601\uc5ed\uc5d0 \ubc88\uc5ed", None))
        self.checkBox_start.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791\ud558\uae30", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub9bd\ubcf4\ub4dc \ud14d\uc2a4\ud2b8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ubc88\uc5ed \ud14d\uc2a4\ud2b8", None))
        self.menu_option.setTitle(QCoreApplication.translate("MainWindow", u"\uc635\uc158", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", u"\ubcf4\uae30", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0", None))
        self.menu_start.setTitle(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
    # retranslateUi

