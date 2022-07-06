from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

from widgets.start_menu import Ui_Form

class StartMenu(QWidget):
    def __init__(self, program):
        self.program = program

        super(StartMenu, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.run_button.clicked.connect(self.program.go_to_play_window)
        self.ui.texts_button.clicked.connect(self.program.go_to_texts_window)
        self.ui.settings_button.clicked.connect(self.program.go_to_settings_window)
        self.ui.credits_button.clicked.connect(self.program.go_to_credits_window)


