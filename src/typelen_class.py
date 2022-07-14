import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import json
from PyQt5 import QtGui

from widgets.main_window import Ui_MainWindow

from start_menu_class import StartMenu
from start_menu_class import StartMenu
from play_window_class import PlayWindow
from texts_window_class import TextsWindow
from settings_window_class import SettingsWindow
from credits_window_class import CreditsWindow
from results_window_class import ResultsWindow
from text_edit_window_class import TextEditWindow


class Typlen(QMainWindow):
    def __init__(self):
        super(Typlen, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.go_to_start_menu()
        self.load_setings()

    def load_setings(self):
        with open("settings.json", 'r', encoding='utf-8') as settings:
            self.settings = json.loads(settings.read())
    
    def save_settings(self):
        with open("settings.json", 'w', encoding='utf-8') as settings:
            settings.write(json.dumps(self.settings, indent=4))

    def open_new_window(self, window):
        self.setCentralWidget(window)
        self.show()

    def go_to_start_menu(self):
        self.open_new_window(StartMenu(self))

    def go_to_play_window(self):
        self.open_new_window(PlayWindow(self))

    def go_to_results_window(self):
        self.open_new_window(ResultsWindow(self))

    def go_to_texts_window(self):
        self.open_new_window(TextsWindow(self))

    def go_to_text_edit_window(self):
        self.open_new_window(TextEditWindow(self))

    def go_to_settings_window(self):
        self.open_new_window(SettingsWindow(self))

    def go_to_credits_window(self):
        self.open_new_window(CreditsWindow(self))


def run_program():
    app = QApplication(sys.argv)
        
    typlen = Typlen()

    typlen.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    typlen = Typlen()

    print(typlen.settings)
    typlen.settings['age'] = "34"
    print(typlen.settings)
    typlen.save_settings()


    typlen.show()
    #sys.exit(app.exec_())
