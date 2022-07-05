from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget


class StartMenu(QWidget):
    def __init__(self, program):
        self.program = program
        super(StartMenu, self).__init__()
        loadUi('src/window_uis/start_menu.ui', self)
        self.run_button.clicked.connect(self.program.go_to_play_window)
        self.texts_button.clicked.connect(self.program.go_to_texts_window)
        self.settings_button.clicked.connect(self.program.go_to_settings_window)
        self.credits_button.clicked.connect(self.program.go_to_credits_window)


