from os import system, path, getcwd
import json

from PyQt5.QtWidgets import *
from design.converter_menu_design import Ui_MainWindow


class MainMenu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.input_path = None
        self.output_path = None
        self.ui_path = None
        self.save_path = None
        self.file_name = None
        self.main_menu = Ui_MainWindow()
        self.main_menu.setupUi(self)

        self.main_menu.select_ui_path_button.clicked.connect(self.select_ui_path)
        self.main_menu.select_py_path_button.clicked.connect(self.select_save_path)
        self.main_menu.convert_button.clicked.connect(self.convert_and_save)

        with open('settings.json', 'r') as json_file:
            self.settings_json = json.load(json_file)

        if self.settings_json["ui_path"] != "":
            self.ui_path = self.settings_json["ui_path"]
            self.main_menu.ui_path_textbox.setText(self.ui_path)
        if self.settings_json["save_path"] != "":
            self.save_path = self.settings_json["save_path"]
            self.main_menu.py_path_textbox.setText(self.save_path)

    def select_ui_path(self):
        self.ui_path = QFileDialog.getOpenFileName(caption="Select UI File",
                                                   filter="UI File (*.ui)",
                                                   directory=f'{self.settings_json["ui_path"]}')

        self.ui_path, self.file_name = path.split(self.ui_path[0])
        self.file_name = str(self.file_name).split(".")[0]

        if self.ui_path != "":
            self.settings_json["ui_path"] = self.ui_path
            with open('settings.json', 'w') as json_file:
                json.dump(self.settings_json, json_file)
        self.main_menu.ui_path_textbox.setText(self.ui_path)

    def select_save_path(self):
        self.save_path = QFileDialog.getExistingDirectory(caption="Select Save Folder",
                                                          directory=f'{self.settings_json["save_path"]}')

        if self.save_path != "":
            self.settings_json["save_path"] = self.save_path
            with open('settings.json', 'w') as json_file:
                json.dump(self.settings_json, json_file)
        self.main_menu.py_path_textbox.setText(self.save_path)

    def convert_and_save(self):
        self.input_path = f'{self.ui_path}/{self.file_name}.ui'
        self.output_path = f'{self.save_path}/{self.file_name}_design.py'
        system(f'pyuic5 {self.input_path} -o {self.output_path}')
