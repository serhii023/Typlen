from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget

from widgets.results_window import Ui_Form

class ResultsWindow(QWidget):
    def __init__(self, program):
        self.program = program
        
        super(ResultsWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.start_menu_button.clicked.connect(self.program.go_to_start_menu)
