# Django Made Easy
# https://github.com/hamdivazim/Django-Made-Easy
#
#
# Copyright Hamd Waseem 2023
# This project is licensed under the Apache License 2.0
#

import sys, os

def pip_cmd(cmd):
    os.system(Rf"virt\Scripts\pip.exe {cmd} > django-made-easy.log")

def get_args():
    return sys.argv[1:]

def set_py_name():
    global PYTHON_NAME
    if os.system("python --version > django-made-easy.log") != "0":
        PYTHON_NAME = "py"

PYTHON_NAME = "python"

def win():
    set_py_name()

    print("Creating virtual environment...")
    os.system(f"{PYTHON_NAME} -m venv virt > django-made-easy.log")

    print("Installing django..")
    pip_cmd("install django")

    print(f"Creating project named {get_args()[0]} at {os.getcwd()} ...")
    os.system(Rf"virt\Scripts\django-admin.exe startproject {get_args()[0]} > django-made-easy.log")

    os.system("color 07")

    print("Remember to activate the virtual enironment 'virt'.")

if __name__ == "__main__":
    win()