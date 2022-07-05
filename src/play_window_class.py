from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget


class PlayWindow(QWidget):
    def __init__(self, program):
        self.program = program
        super(PlayWindow, self).__init__()
        loadUi('src/window_uis/play_window.ui', self)
        self.start_menu_button.clicked.connect(self.program.go_to_start_menu)
        self.end_button.clicked.connect(self.program.go_to_results_window)


