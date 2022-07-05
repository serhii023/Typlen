import sys
from PyQt5.QtWidgets import QApplication

from typelen_class import Typlen


if __name__ == '__main__':
    app = QApplication(sys.argv)
        
    typlen = Typlen()

    typlen.showMaximized()
    sys.exit(app.exec_())
