#coding=utf-8

import configparser
import mylib.PythonSingleton.Singleton as SLT
import os
import mylib.path

class projIni(SLT.Singleton):

    config = None

    config_file_name = "Excel_JS_Runtime_CLI.ini"

    base_path = ""

    def __Singleton_Init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.get_saving_path(), encoding="utf-8")

    def get_saving_path(self):
        return os.getcwd() + "/" + self.base_path + self.config_file_name

    def set_base_path(self, base_path):
        self.base_path = base_path

    def init_config_file(self, project_name):
        self.config.add_section("project")
        self.config.set("project", "name", project_name)
        self.save_ini_file()

    def save_ini_file(self):
        self.config.write(open(self.get_saving_path(), "w"))

    def read_proj_name(self):
        return self.config.get("project", "name")
    
    def get_xlsm_full_name(self):
        return self.read_proj_name() + ".xlsm"

    def get_xlsm_full_path(self):
        return mylib.path.abs_path(self.get_xlsm_full_name())
