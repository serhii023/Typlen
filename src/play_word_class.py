from curses.ascii import isalpha
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QWidget, QLabel
from PyQt5.QtGui import QFont

from widgets.play_word_widget import Ui_Form

# class for checking if the typed symbol is corect and/or is the last
class WordWidget(QWidget):
    def __init__(self, program, word):
        self.program = program
        
        super(WordWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # font for defolt leters
        self.usual = QFont()
        self.usual.setPointSize(12)
        
        # font for leter, that must be presed
        self.underline = QFont()
        self.underline.setPointSize(12)
        self.underline.setUnderline(True)

        self.letters = []

        for c in word:
            l = QLabel(c ,self)
            l.setFont(self.usual)
            self.ui.horizontalLayout.addWidget(l)
            self.letters.append(l)
        l = QLabel(' ' ,self)
        l.setFont(self.usual)
        self.ui.horizontalLayout.addWidget(l)
        self.letters.append(l)
        
        self.current_letter_id = 0
        self.letters[self.current_letter_id].setFont(self.underline)

    # if it's the last character return 1 else 0
    # if character is correct, go to the next
    # if isn't correct, mark current character
    def check_letter(self, letter):
        if letter == self.letters[self.current_letter_id].text():
            self.letters[self.current_letter_id].setFont(self.usual)
            self.current_letter_id += 1
            
            if self.current_letter_id >= len(self.letters):
                return 1

            self.letters[self.current_letter_id].setFont(self.underline)

        return 0
        



