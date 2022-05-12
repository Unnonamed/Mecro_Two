import option_trans_form as dialog
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QMessageBox, QDialog

class Option_trans_dialog(QDialog):
    def __init__(self, parent: ...) -> None:
        super().__init__(parent)
        self.dialog = dialog.Ui_dialog()
        self.main = parent
        
        #객체에 옵션을 가져오는 함수
        self.dialog.setupUi(self)
        
        self.dialog_slider = self.dialog.horizontalSlider
        self.dialog_text = self.dialog.label
        
        #self.dialog_slider.sliderMoved.connect(self.sliderhanged_handler)
        self.dialog_slider.valueChanged.connect(self.sliderhanged_handler)
        
        self.load_run_option(self.main)

    def __del__(self):
        pass
    
    def closeEvent(self, event: QCloseEvent) -> None:
        if self.check_run_option() == False:
            event.ignore()
            return
        
        #객체에 옵션을 반영하는 함수
        self.save_run_option()
        pass
    
    def load_run_option(self, parent):
        self.main_transval = parent.transval
        self.dialog_slider.setValue(self.main_transval)
        pass
    
    def save_run_option(self):
        self.main.transval = self.main_transval
        pass
    
    def check_run_option(self) -> bool:
        return True
    
    def sliderhanged_handler(self) -> None:
        self.main_transval = self.dialog_slider.value()
        self.dialog_text.setText(str(self.main_transval))
        pass
    
