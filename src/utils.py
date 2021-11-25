import pandas as pd
import os
import librosa
from PyQt5 import QtWidgets as qtw
import numpy as np


def openSound(window):
    path, _ = qtw.QFileDialog.getOpenFileName(window, 'Open File', "sample.wav","Sounds(*.wav)")
    return loadSound(path)


def parsePath(path):
    file_name = path.split(os.path.sep)[-1]
    dot_splits = file_name.split(".")
    extension = dot_splits[-1] if len(dot_splits) > 1 else ""
    name = "".join(dot_splits[0:-1])

    return (name, extension)

def loadSound(path):
    name, extension = parsePath(path)
    #DEBUG 
    print(name, extension)
    if extension == "wav":
        full_data, sr = librosa.core.load(path)
        return (True, name, path, (full_data, sr))
    else:
        return (False, None, None, (None, None))
