from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget


class TextEditWindow(QWidget):
    def __init__(self, program):
        self.program = program
        super(TextEditWindow, self).__init__()
        loadUi('src/window_uis/text_edit_window.ui', self)
        self.start_menu_button.clicked.connect(self.program.go_to_start_menu)
        self.texts_button.clicked.connect(self.program.go_to_texts_window)
