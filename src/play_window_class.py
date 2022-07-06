from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

from widgets.play_window import Ui_Form


class PlayWindow(QWidget):
    def __init__(self, program):
        self.program = program
        
        super(PlayWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.start_menu_button.clicked.connect(self.program.go_to_start_menu)
        self.ui.end_button.clicked.connect(self.program.go_to_results_window)


