# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(597, 628)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actioTrans = QAction(MainWindow)
        self.actioTrans.setObjectName(u"actioTrans")
        self.actionhelp = QAction(MainWindow)
        self.actionhelp.setObjectName(u"actionhelp")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_8 = QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox_start = QCheckBox(self.groupBox)
        self.checkBox_start.setObjectName(u"checkBox_start")

        self.horizontalLayout.addWidget(self.checkBox_start)

        self.pushButton_capture = QPushButton(self.groupBox)
        self.pushButton_capture.setObjectName(u"pushButton_capture")

        self.horizontalLayout.addWidget(self.pushButton_capture)


        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(435, 16))

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignTop)

        self.textEdit_clip = QTextEdit(self.groupBox)
        self.textEdit_clip.setObjectName(u"textEdit_clip")
        self.textEdit_clip.setMinimumSize(QSize(0, 71))
        self.textEdit_clip.setMaximumSize(QSize(16777215, 71))

        self.verticalLayout.addWidget(self.textEdit_clip, 0, Qt.AlignTop)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(435, 16))

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignLeft|Qt.AlignTop)

        self.textEdit_trans = QTextEdit(self.groupBox)
        self.textEdit_trans.setObjectName(u"textEdit_trans")
        self.textEdit_trans.setMaximumSize(QSize(16777215, 71))

        self.verticalLayout.addWidget(self.textEdit_trans, 0, Qt.AlignTop)


        self.gridLayout_8.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.textEdit_google = QTextEdit(self.groupBox)
        self.textEdit_google.setObjectName(u"textEdit_google")

        self.gridLayout.addWidget(self.textEdit_google, 1, 0, 1, 1)

        self.textEdit_papago = QTextEdit(self.groupBox)
        self.textEdit_papago.setObjectName(u"textEdit_papago")

        self.gridLayout.addWidget(self.textEdit_papago, 1, 1, 1, 1)

        self.comboBox_google = QComboBox(self.groupBox)
        self.comboBox_google.addItem("")
        self.comboBox_google.addItem("")
        self.comboBox_google.addItem("")
        self.comboBox_google.setObjectName(u"comboBox_google")

        self.gridLayout.addWidget(self.comboBox_google, 0, 0, 1, 1)

        self.comboBox_papago = QComboBox(self.groupBox)
        self.comboBox_papago.addItem("")
        self.comboBox_papago.addItem("")
        self.comboBox_papago.addItem("")
        self.comboBox_papago.setObjectName(u"comboBox_papago")

        self.gridLayout.addWidget(self.comboBox_papago, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout, 2, 0, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 597, 22))
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
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.checkBox_start.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791\ud558\uae30", None))
        self.pushButton_capture.setText(QCoreApplication.translate("MainWindow", u"\ucea1\uccd0\uc601\uc5ed", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\ud074\ub9bd\ubcf4\ub4dc \ud14d\uc2a4\ud2b8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ubc88\uc5ed \ud14d\uc2a4\ud2b8", None))
        self.comboBox_google.setItemText(0, QCoreApplication.translate("MainWindow", u"\uad6c\uae00 - \ud55c\uad6d\uc5b4", None))
        self.comboBox_google.setItemText(1, QCoreApplication.translate("MainWindow", u"\uad6c\uae00 - \uc601\uc5b4", None))
        self.comboBox_google.setItemText(2, QCoreApplication.translate("MainWindow", u"\uad6c\uae00 - \uc77c\uc5b4", None))

        self.comboBox_papago.setItemText(0, QCoreApplication.translate("MainWindow", u"\ud30c\ud30c\uace0 - \ud55c\uad6d\uc5b4", None))
        self.comboBox_papago.setItemText(1, QCoreApplication.translate("MainWindow", u"\ud30c\ud30c\uace0 - \uc77c\uc5b4", None))
        self.comboBox_papago.setItemText(2, QCoreApplication.translate("MainWindow", u"\ud30c\ud30c\uace0 - \uc601\uc5b4", None))

        self.menu_option.setTitle(QCoreApplication.translate("MainWindow", u"\uc635\uc158", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", u"\ubcf4\uae30", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\ub3c4\uc6c0\ub9d0", None))
        self.menu_start.setTitle(QCoreApplication.translate("MainWindow", u"\uc2dc\uc791", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\ud30c\uc77c", None))
    # retranslateUi

