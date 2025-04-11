from PyQt5.QtCore import Qt                                                                       
from PyQt5.QtWidgets import (                                                                     
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QInputDialog, QTextEdit, QLineEdit, QListWidget
)    

app = QApplication([])
main_window = QWidget()
main_window.resize(700, 700)
main_window.setWindowTitle("розумні замітки")
























main_window.show()
app.exec_()