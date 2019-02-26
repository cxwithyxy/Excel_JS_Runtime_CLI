#coding=utf-8

import configparser
import mylib.PythonSingleton.Singleton as SLT

class projIni(SLT.Singleton):

    config = None

    config_file_name = "Excel_JS_Runtime_CLI.ini"

    base_path = ""

    def __Singleton_Init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("ini", encoding="utf-8")

    def set_base_path(self, base_path):
        self.base_path = base_path

    def init_config_file(self, project_name):
        self.config.add_section("project")
        self.config.set("project", "name", project_name)
        self.save_ini_file()

    def save_ini_file(self):
        self.config.write(open(self.config_file_name, "w"))


# config.read("ini", encoding="utf-8")
# add_section
# config.set("db", "db_port", "69")  #修改db_port的值为69
# config.write(open("ini", "w"))

# print config
