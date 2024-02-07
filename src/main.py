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

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from utils import *
import re
import os
import time

#visual code 에서 한글 깨질 때
#sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
#sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.w = None # No external window yet
        
        self.driver = None
        self.driver1 = None
        self.driver_run = False
        self.startFlag = False
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless") #창 안띄우기
        chrome_options.add_argument("--no-sandbox") #root 권한으로 실행
        # chrome_options.add_argument("--disable-dev-shm-usage") #디스크 메모리 사용안함
        
        self.textEdit_clip.setText("클립보드창")
        self.textEdit_trans.setText("번역창")


        
        try:
            s = os.walk('./') #현재 디렉토리
            for path, dir, files in s:
                for filename in files:
                    # print(filename)
                    ext = os.path.splitext(filename)[-1]
                    if ext == '.exe':
                        print("%s/%s" % (path, filename))
                        file_path = f"{path}/{filename}" #파일 경로
                        self.driver = webdriver.Chrome(service = Service(file_path), options=chrome_options)
                        self.driver1 = webdriver.Chrome(service = Service(file_path), options=chrome_options)
                        # time 업데이트 기능 - 메인 ui 타이머       
                        self.chromeDriver_init()
                        self.driver_run = True
                        break
                
            if(self.driver_run == False) :
                print("ChromeDriver not found")
                raise AttributeError("ChromeDriver not found")

                    
        except AttributeError as e:
            print('Install ChromeDriver : ,', e)
            
            insatll_Box = QMessageBox()
            insatll_Box.setWindowTitle("Warning")
            insatll_Box.setText("ChromeDriver not found. 설치할까요?")
            insatll_Box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            insatll_Box = insatll_Box.exec()
            
            if insatll_Box == QMessageBox.Ok:
                get_chrome_version()
                download_chromedriver()
                
                Util.showBox("Success", "Install ChromeDriver")
                osRest()

            else:
                Util.showBox("Warning", "Test Mode Start")
                pass
            
            
            
        self.transval = 1 # 투명도 값
        
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
        timerVar.start()
        
        workTime = QTimer(self)
        workTime.setInterval(5000)
        workTime.start()
        
        executor = mp.ThreadPoolExecutor(max_workers=4)
        executor.submit(self.timeUpdate_handler(timerVar), 1)
        executor.submit(self.workerUpdate_papago_handler(workTime), 2)
        executor.submit(self.workerUpdate_google_handler(workTime), 3)

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
        
        time.sleep(1)
        
        
        if self.startFlag == True:
            if self.driver != None:
                self.get_papago_trans(text) #파파고 번역 실행
                
            if self.driver1 != None:
                self.get_google_trans(text) #구글 번역 실행

    
    @Slot()
    def timeUpdate_handler(self, timerVar:QTimer) -> None:
        #Qtimer
        timerVar.setInterval(500)
        timerVar.timeout.connect(self.timeUpdate)
    
    def timeUpdate(self) -> None:
        now = datetime.datetime.now()
        date = now.strftime("%Y년%m월%d일 %H시%M분%S초")
        
        if self.driver != None:
            driverF = "O"
        else:
            driverF = "X"

        if self.driver1 != None:
            driver1F = "O"
        else:
            driver1F = "X"

        self.startFlag = self.checkBox_start.isChecked()
        
        str_time = f"[{date}] 파파고 : {driverF} 구글 : {driver1F}"
        #statusbar Message
        self.statusBar().showMessage(str_time)
    
    
    @Slot()
    def workerUpdate_papago_handler(self, timerVar:QTimer) -> None:
        #Qtimer
        timerVar.setInterval(3000)
        timerVar.timeout.connect(self.chromeDriver_papago_walker) #파파고 번역 가져욤
    
    @Slot()
    def workerUpdate_google_handler(self, timerVar:QTimer) -> None:
        #Qtimer
        timerVar.setInterval(3000)
        timerVar.timeout.connect(self.chromeDriver_google_walker) #구글 번역 가져욤
    
    
    def captureWindow_handler(self):
        self.w = captureWindow(self)
        self.w.show()
    
    def chromeDriver_init(self) -> None:
        if self.driver != None:
            self.driver.get("https://papago.naver.com/?sk=en&tk=ko&hn=0&st=test")
            # self.driver.implicitly_wait(10) #10초 대기
            # self.driver.maximize_window() #전체화면
            # self.driver.implicitly_wait(10) #10초 대기
            # self.driver.set_window_size(1920, 1080) #화면 크기
            # self.driver.implicitly_wait(10) #10초 대기
                  
        if self.driver1 != None:  
            self.driver1.get("https://translate.google.com/?sl=en&tl=ko&text=test&op=translate")
            # self.driver1.implicitly_wait(10) #10초 대기
            # self.driver1.maximize_window() #전체화면
            # self.driver1.implicitly_wait(10) #10초 대기
            # self.driver1.set_window_size(1920, 1080) #화면 크기
            # self.driver1.implicitly_wait(10) #10초 대기
            
    def chromeDriver_papago_walker(self) -> None:
        # text = self.textEdit_trans.toPlainText()
        if self.driver != None:
            result = self.driver.find_element(by=By.XPATH, value='//*[@id="txtTarget"]/span').text # 번역된 내용 가져오기
            self.textEdit_papago.setText(result)
        
    def chromeDriver_google_walker(self) -> None:
        if self.driver1 != None:
            result1 = self.driver1.find_element(by=By.XPATH, value='/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[2]/div[1]/div[7]/div/div[1]/span[1]/span/span').text
            self.textEdit_google.setText(result1)

    def get_papago_trans(self, text):
        if self.driver != None:
            try:
                self.driver.find_element(by=By.ID, value='txtSource').clear() # 초기화
                self.driver.find_element(by=By.ID, value='txtSource').send_keys(text) # 번역할 내용 입력
                self.driver.find_element(by=By.XPATH, value='//*[@id="txtSource"]').click() # 번역하기 버튼 클릭
            except Exception as e:
                print('retrying 0...')

    def get_google_trans(self, text):
        if self.driver1 != None:
            try:
                self.driver1.find_element(by=By.CSS_SELECTOR, value='textarea').clear() # 초기화
                self.driver1.find_element(by=By.CSS_SELECTOR, value='textarea').send_keys(text) # 번역할 내용 입력
            except Exception as e:
                print('retrying 1...')

        
class captureWindow(QWidget):
    #def __init__(self, *args, obj=None, **kwargs):
    def __init__(self, parent) -> None:
        #super(captureWindow, self).__init__(*args, **kwargs)
        super().__init__()

        self.main = parent

        self.setWindowTitle(" ")
        #self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint) # 항상 위로 올라옴 | 상단 타이틀 부분 가리기 
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
        timerVar.setInterval(5000)
        timerVar.timeout.connect(self.screnShot)
        
    def screnShot(self):
        if not self._screen:
            return
        
        #print(self._screen)
        #self.update_screenshot_label()
        
        #텍스트 앱 기타항목 크기 100% 125% 다르면 범위 깨짐
        p=self._screen.grabWindow(0, self.x(), self.y() + 30, self.width(), self.height())
        p.save("saveImage.jpg")            
        
        x = ocr.img_ocr("saveImage.jpg")
        self.main.textEdit_trans.setText(str(x))
        #pass

    def update_screenshot_label(self):
        pass

def osRest():
    os.execl(sys.executable, sys.executable, *sys.argv)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()

    window.show()
    app.exec() # https://www.pythonguis.com/faq/pyqt6-vs-pyside6/
    #app.exec_() # DeprecationWarning: 'exec_' will be removed in the future. Use 'exec' instead.

class Util:
    def showBox(Title = "Title", send = "Message"):
        box = QMessageBox()
        box.setWindowTitle("Title")
        box.setWindowFlag(Qt.FramelessWindowHint)
        box.setText(send)
        box.exec()
        
if __name__ == '__main__':
    main()
    


