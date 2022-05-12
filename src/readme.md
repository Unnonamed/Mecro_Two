# pip list (정리해서 required.txt로)
charset-normalizer 2.0.12
idna               3.3
numpy              1.22.3
Pillow             9.1.0
pip                22.0.4
PySide6            6.2.4
requests           2.27.1
setuptools         60.10.0
shiboken6          6.2.4
torch              1.11.0
torchaudio         0.11.0
torchvision        0.12.0
typing_extensions  4.1.1
urllib3            1.26.9
wheel              0.37.1
opencv-contrib-python 

# <h3> pyqt 사용법 #
##### 배포 pip freeze > requirements.txt
##### 설치 pip install -r requirements.txt

1. pyside6-designer 실행
    - pyside6-designer.exe
2. pyside6-designer로 만든 코드 컴파일
    - pyside6-uic.exe untitled.ui > main_ui.py
3. pyinstaller로 exe 파일로 컴파일 (-F : 한 파일로 만들기)
    - pyinstaller -w ui_test.py  