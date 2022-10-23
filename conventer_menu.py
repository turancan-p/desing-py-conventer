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
        self.uipath = QFileDialog.getOpenFileName(caption="Select UI File",
                                               filter="UI File (*.ui)")
        self.main_menu.ui_path_textbox.setText(self.uipath[0])
        self.filename = os.path.basename(self.uipath[0]).split('.')[0]

        self.cmdpath = os.path.dirname(self.uipath[0])

    def select_save_file(self):
        self.savepath = QFileDialog.getExistingDirectory(caption="Select Save Folder")
        self.main_menu.py_path_textbox.setText(f'{self.savepath}/{self.filename}.py')

    def convert_and_save(self):
        os.chdir(f'{self.cmdpath}/')
        os.system(f'pyuic5 -x {self.filename}.ui -o {self.filename}_design2.py')
        os.system(f'MOVE {self.filename}_design2.py {self.savepath}')