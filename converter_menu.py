import os
import json

from PyQt5.QtWidgets import *
from design.converter_menu_design import Ui_MainWindow


class MainMenu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_menu = Ui_MainWindow()
        self.main_menu.setupUi(self)

        self.main_menu.select_ui_path_button.clicked.connect(self.select_ui)
        self.main_menu.select_py_path_button.clicked.connect(self.select_save_file)
        self.main_menu.convert_button.clicked.connect(self.convert_and_save)

        with open('settings.json', 'r') as json_file:
            self.settings_json = json.load(json_file)
            print(self.settings_json["ui_path"])

    def select_ui(self):
        with open('settings.json', 'r') as json_file:
            self.settings_json = json.load(json_file)
        self.uipath = QFileDialog.getOpenFileName(caption="Select UI File",
                                                  filter="UI File (*.ui)",
                                                  directory=f'{self.settings_json["ui_path"]}')

        self.settings_json["ui_path"] = self.uipath[0]
        with open('settings.json', 'w') as json_file:
            json.dump(self.settings_json, json_file)

        self.main_menu.ui_path_textbox.setText(self.uipath[0])
        self.filename = os.path.basename(self.uipath[0]).split('.')[0]

        self.cmdpath = os.path.dirname(self.uipath[0])

    def select_save_file(self):
        with open('settings.json', 'r') as json_file:
            self.settings_json = json.load(json_file)
        self.savepath = QFileDialog.getExistingDirectory(caption="Select Save Folder",
                                                         directory=f'{self.settings_json["save_path"]}')
        self.main_menu.py_path_textbox.setText(f'{self.savepath}/{self.filename}.py')
        self.settings_json["save_path"] = self.savepath
        with open('settings.json', 'w') as json_file:
            json.dump(self.settings_json, json_file)

    def convert_and_save(self):
        os.chdir(f'{self.cmdpath}/')
        os.system(f'pyuic5 -x {self.filename}.ui -o {self.filename}_design.py')
        os.system(f'MOVE {self.filename}_design.py {self.savepath}')
