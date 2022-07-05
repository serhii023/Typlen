from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget


class TextsWindow(QWidget):
    def __init__(self, program):
        self.program = program
        super(TextsWindow, self).__init__()
        loadUi('src/window_uis/texts_window.ui', self)
        self.start_menu_button.clicked.connect(self.program.go_to_start_menu)
        self.edit_button.clicked.connect(self.program.go_to_text_edit_window)


