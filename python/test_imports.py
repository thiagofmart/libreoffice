# python version must 3.8.10
# on <LibreOffice_pathh>/user/Script/python
# create a folder "pythonpath" with another folder "__pycache__" inside;
# install the requirements.txt using python38 -m pip install <module> inside the venv
# move the installed packages to 
# add your python scripts
import uno
import easymacro
import numpy as np
import pandas as pd


def enviardados():
    doc = XSCRIPTCONTEXT.getDocument()
    sheet = doc.CurrentController.ActiveSheet
    easymacro.msgbox('Hello World!')
