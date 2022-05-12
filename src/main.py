#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import datetime
import cv2

import concurrent.futures as mp
from main_ui_form import Ui_MainWindow

from PySide6.QtCore import * #Qt, Slot, QTimer, QPoint
from PySide6.QtGui import * #QGuiApplication, QMouseEvent,QCloseEvent, QAction
from PySide6.QtWidgets import * #(QApplication, QMainWindow,QLabel, QWidget, QMessageBox, QVBoxLayout)

from option_trans import Option_trans_dialog
from cnocr_src.ocr import * 

#visual code 에서 한글 깨질 때
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.w = None # No external window yet
        
        # option 기본 세팅
        self.transval = 1
        
        # menuTooltip Function
        # 파일 > 종료버튼
        quit_btn = self.actionQuit
        quit_btn.setShortcut(Qt.CTRL | Qt.Key_Q)
        quit_btn.triggered.connect(self.close)

        # 옵션 > 투명도버튼
        trans_btn = self.actioTrans
        trans_btn.setShortcut(Qt.CTRL | Qt.Key_T)
        trans_btn.triggered.connect(self.actionButton_trans)
        
        # 메인화면 캡쳐 button Function
        pushButton_capture = self.pushButton_capture
        pushButton_capture.clicked.connect(self.captureWindow_handler)
        pushButton_capture.setShortcut(Qt.CTRL | Qt.Key_F)
        
        #클립보드 이벤트 트리거
        self.clip = QApplication.clipboard()
        self.clip.dataChanged.connect(self.dataChanged_handler)
        
        #setTitle Function
        self.textEdit_clip.textChanged.connect(self.textChanged_handler)

        # time 업데이트 기능 - 메인 ui 타이머       
        timerVar = QTimer(self)
        executor = mp.ThreadPoolExecutor(max_workers=1)
        executor.submit(self.timeUpdate_handler(timerVar))
        timerVar.start()
        
    
    def __del__(self):
        print("__del__ 메서드 수행")
    
    def main():
        pass
    
    def actionButton_trans(self) -> None:
        option_dlg = Option_trans_dialog(self)
        option_dlg.exec()
    
    @Slot()
    def dataChanged_handler(self) -> None:
        text = self.clip.text()
        if not text:
            return

        self.textEdit_clip.setText(text)   
        
    @Slot()
    def textChanged_handler(self) -> None:
        text = self.textEdit_clip.toPlainText()
        conv_text = text
        self.textEdit_trans.setText(conv_text)
    
    @Slot()
    def timeUpdate_handler(self, timerVar:QTimer) -> None:
        #Qtimer
        timerVar.setInterval(1000)
        timerVar.timeout.connect(self.timeUpdate)
    
    def timeUpdate(self) -> None:
        now = datetime.datetime.now()
        date = now.strftime("%Y년%m월%d일 %H시%M분%S초")
        #checkbox checking
        global flag
        flag = self.checkBox_start.isChecked()
        str = f"{date} :: 동작상태 : {flag}"
        #statusbar Message
        self.statusBar().showMessage(str)
    
    
    def captureWindow_handler(self):
        self.w = captureWindow(self)
        self.w.show()
        
     
class captureWindow(QWidget):
    #def __init__(self, *args, obj=None, **kwargs):
    def __init__(self, parent) -> None:
        #super(captureWindow, self).__init__(*args, **kwargs)
        super().__init__()

        self.main = parent

        self.setWindowTitle(" ")
        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint) # 항상 위로 올라옴 | 상단 타이틀 부분 가리기 
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(self.main.transval * 0.1) #투명도
        self.setAutoFillBackground(True)
        
        #Qwidget 화면에 표시해줄 Label
        self.screenshot_label = QLabel(self)

        # time 업데이트 기능        
        screenTimer = QTimer(self)
        executor = mp.ThreadPoolExecutor(max_workers=1)
        executor.submit(self.Update_handler(screenTimer))
        screenTimer.start()
        
        self._screen = QGuiApplication.primaryScreen()

        #context Menu
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        action1 = QAction("White Color" , self)
        action2 = QAction("Black Color" , self)
        action3 = QAction("Red Color" , self)
        action4 = QAction("Green Color" , self)
        action5 = QAction("Blue Color" , self)
        action6 = QAction("투명도 변경" , self)

        action1.triggered.connect(self.action1_change)
        action2.triggered.connect(self.action2_change)
        action3.triggered.connect(self.action3_change)
        action4.triggered.connect(self.action4_change)
        action5.triggered.connect(self.action5_change)
        action6.triggered.connect(self.action6_change)

        self.addAction(action1)
        self.addAction(action2)
        self.addAction(action3)        
        self.addAction(action4)        
        self.addAction(action5)        
        self.addAction(action6)        

        
    def closeEvent(self, event: QCloseEvent) -> None:
        close = QMessageBox()
        close.setWindowTitle("Exit")
        close.setText("You sure?")
        close.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        close = close.exec()
        
        if close == QMessageBox.Ok:
            event.accept()
        else:
            event.ignore()
                
    # 마우스 관련 이벤트 함수들   
    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.oldPos = event.globalPosition().toPoint() 
        if(event.buttons() == Qt.RightButton):
            pass

    def mouseMoveEvent(self, event: QMouseEvent):
        if(event.buttons() == Qt.LeftButton):
            vector2D = QPoint(event.globalPosition().toPoint() - self.oldPos)
            self.move(self.x() + vector2D.x(), self.y() + vector2D.y())
            self.oldPos = event.globalPosition().toPoint()   

    def mouseButtonKind(self, buttons): # Not used
        if buttons & Qt.LeftButton: print('LEFT') 
        if buttons & Qt.RightButton: print('RIGHT')


    def action1_change(self):
        self.setStyleSheet("background:white;")
    def action2_change(self):
        self.setStyleSheet("background:black;")
    def action3_change(self):
        self.setStyleSheet("background:red;")
    def action4_change(self):
        self.setStyleSheet("background:green;")
    def action5_change(self):
        self.setStyleSheet("background:blue;")
    def action6_change(self):
        option_dlg = Option_trans_dialog(self.main)
        option_dlg.exec()

        self.setWindowOpacity(self.main.transval * 0.1) #투명도

            
    def Update_handler(self, timerVar:QTimer) -> None:
        #Qtimer
        timerVar.setInterval(1000)
        timerVar.timeout.connect(self.screnShot)
        
    def screnShot(self):
        if(flag):
            
            if not self._screen:
                return
            
            print(self._screen)
            #self.update_screenshot_label()
            
            #텍스트 앱 기타항목 크기 100% 125% 다르면 범위 깨짐
            p=self._screen.grabWindow(0, self.x(), self.y() + 30, self.width(), self.height())
            p.save("saveImage.jpg")            
            
            x = ocr.img_ocr("saveImage.jpg")
            self.main.textEdit_trans.setText(str(x))
            #pass

    def update_screenshot_label(self):
        pass

        
class Util:

    def clickBtn():
        print("gl")
        box = QMessageBox()
        box.setWindowTitle("title")
        box.setText("message")
        box.exec()
        
    def printCV2():
        print(cv2.__version__)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec() # https://www.pythonguis.com/faq/pyqt6-vs-pyside6/
    #app.exec_() # DeprecationWarning: 'exec_' will be removed in the future. Use 'exec' instead.

if __name__ == '__main__':
    main()
    
