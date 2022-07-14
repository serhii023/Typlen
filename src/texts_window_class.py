from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

from widgets.texts_window import Ui_Form

class TextsWindow(QWidget):
    def __init__(self, program):
        self.program = program

        super(TextsWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.start_menu_button.clicked.connect(self.program.go_to_start_menu)
        self.ui.edit_button.clicked.connect(self.program.go_to_text_edit_window)

        self.texts_files = []
        


