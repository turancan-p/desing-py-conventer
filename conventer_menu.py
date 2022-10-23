import os

from PyQt5.QtWidgets import *
from design.conventer_menu_design import Ui_MainWindow


class MainMenu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_menu = Ui_MainWindow()
        self.main_menu.setupUi(self)

        self.main_menu.select_ui_path_button.clicked.connect(self.select_ui)
        self.main_menu.select_py_path_button.clicked.connect(self.select_save_file)
        self.main_menu.convert_button.clicked.connect(self.convert_and_save)

    def select_ui(self):
        filepath = QFileDialog.getOpenFileName(caption="Select UI File",
                                               filter="UI File (*.ui)")
        self.main_menu.ui_path_textbox.setText(filepath[0])
        self.filename = os.path.basename(filepath[0]).split('.')[0]

    def select_save_file(self):
        self.filepath = QFileDialog.getExistingDirectory(caption="Select Save Folder")
        self.main_menu.py_path_textbox.setText(f'{self.filepath}/{self.filename}.py')

    def convert_and_save(self):
        print(f'{self.filepath}/cmd.exe python -m PyQt5.uic.pyuic -x {self.filename}.ui -o {self.filename}.py')