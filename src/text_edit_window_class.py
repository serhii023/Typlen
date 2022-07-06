from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

from widgets.text_edit_window import Ui_Form

class TextEditWindow(QWidget):
    def __init__(self, program):
        self.program = program

        super(TextEditWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.start_menu_button.clicked.connect(self.program.go_to_start_menu)
        self.ui.texts_button.clicked.connect(self.program.go_to_texts_window)
