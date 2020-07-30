import os
import json

from platform import system
from screeninfo import get_monitors
from numpy import array
from cv2 import cvtColor, COLOR_BGR2RGB, VideoWriter_fourcc, VideoWriter
from datetime import datetime
from math import floor
from keyboard import is_pressed
from setting import load_settings
from colorama import init, Fore
init(autoreset=True)

if system() == "Windows":
    from PIL.ImageGrab import grab
else:
    from pyscreenshot import grab

def get_primary_monitor():
    return (get_monitors()[0].width, get_monitors()[0].height)

def grab_to_opencv():
    return cvtColor(array(grab()), COLOR_BGR2RGB)

def name_video(date_format):
    return datetime.now().strftime(date_format)

def make_video():
    settings = load_settings()
    if not os.path.exists(settings["output folder"]):
        os.mkdir(settings["output folder"])

    fname_path = settings["output folder"] + "/" + name_video(settings["date format"]) + ".avi"
    print(Fore.GREEN+fname_path)
    
    vobj = VideoWriter(fname_path, VideoWriter_fourcc(*settings["fourcc"]),
                            float(settings["fps"]), get_primary_monitor())

    while True:
        vobj.write(grab_to_opencv())
        if is_pressed(settings["stop key"]):
            break

    vobj.release()
