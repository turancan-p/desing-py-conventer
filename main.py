from PyQt5.QtWidgets import QApplication
from converter_menu import MainMenu

app = QApplication([])

window = MainMenu()
window.show()
app.exec_()