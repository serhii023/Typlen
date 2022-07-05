from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget


class SettingsWindow(QWidget):
    def __init__(self, program):
        self.program = program
        super(SettingsWindow, self).__init__()
        loadUi('src/window_uis/settings_window.ui', self)
        self.start_menu_button.clicked.connect(self.program.go_to_start_menu)


