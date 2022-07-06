from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QLabel

from widgets.play_window import Ui_Form

from play_word_class import WordWidget

APROPRIATE_CHARS = ['.', ',', ':', '"', "'", ';', '?', ' ',
                    '!', '@', '$', '*', '/', '-', '+','{','}','[',']','=', '_',
                    1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
class PlayWindow(QWidget):
    def __init__(self, program):
        self.program = program

        super(PlayWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.start_menu_button.clicked.connect(self.program.go_to_start_menu)
        self.ui.end_button.clicked.connect(self.program.go_to_results_window)

        self.words = []
        with open('texts/empty_text.txt','r') as file:
            for line in file:
                for word in line.split():
                    self.words.append(word)

        self.ui.prew.setText("")
        self.current_word_id = 0
        self.current_word = WordWidget(self, self.words[0])
        self.ui.horizontalLayout_3.addWidget(self.current_word)
        self.ui.next.setText(self.words[1])

    def keyPressEvent(self, e):
        s = e.text()
        if s.isalpha() or s in APROPRIATE_CHARS:
            if(self.current_word.check_letter(s)):
                self.next_word()
                

    def next_word(self):
        self.ui.horizontalLayout_3.removeWidget(self.current_word)
        self.current_word.deleteLater()
        self.ui.prew.setText(self.words[self.current_word_id])
        self.current_word_id += 1
        self.current_word = WordWidget(self, self.words[self.current_word_id])
        self.ui.horizontalLayout_3.addWidget(self.current_word)
        if(self.current_word_id + 1 < len(self.words)):
            self.ui.next.setText(self.words[self.current_word_id + 1])
