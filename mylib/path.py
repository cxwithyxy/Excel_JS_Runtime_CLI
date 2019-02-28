#coding=utf-8

import pathlib

def mkdir(path_from_argu):
    the_path = pathlib.PureWindowsPath(path_from_argu)
    try:
        pathlib.Path.mkdir(pathlib.Path(the_path))
    except:
        print path_from_argu + u" 文件夹已经存在了"
        exit()

def join_path(path_1, path_2):
    return str(pathlib.PureWindowsPath(path_1).joinpath(path_2))

def abs_path(path):
    return str(pathlib.Path(path).resolve())

def get_js_saving_path_base_on_xlsm(xlsm_path):
    return str(pathlib.PureWindowsPath(xlsm_path).parent.joinpath("src"))

def get_file_name_without_suffixs(file_path):
    return pathlib.PureWindowsPath(file_path).name.split(".")[0]

def is_exist(path):
    return pathlib.Path(path).exists()