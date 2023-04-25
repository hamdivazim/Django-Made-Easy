# Django Made Easy
# https://github.com/hamdivazim/Django-Made-Easy
#
#
# Copyright Hamd Waseem 2023
# This project is licensed under the Apache License 2.0
#

import sys
import os
import subprocess

def pip_cmd(cmd):
    subprocess.run(["pip", cmd], check=True)

def get_args():
    args = sys.argv[1:]
    if not args:
        print("Usage: python django_made_easy.py project_name")
        sys.exit(1)
    return args

def set_py_name():
    global PYTHON_NAME
    PYTHON_NAME = os.path.basename(sys.executable)

def create_venv():
    print("Creating virtual environment...")
    subprocess.run([PYTHON_NAME, "-m", "venv", "virt"], check=True)

def install_django():
    print("Installing django in virtual environment...")
    pip_cmd("install django")

def create_project():
    project_name = get_args()[0]
    print(f"Creating project named {project_name} at {os.getcwd()} ...")
    subprocess.run(["virt/Scripts/django-admin", "startproject", project_name], check=True)

def activate_venv():
    if sys.platform == "win32":
        activate_path = "virt/Scripts/activate.bat"
    else:
        activate_path = "virt/bin/activate"
    subprocess.run([activate_path], shell=True)

def main():
    set_py_name()
    create_venv()
    activate_venv()
    install_django()
    create_project()
    print("Done!")

if __name__ == "__main__":
    main()
