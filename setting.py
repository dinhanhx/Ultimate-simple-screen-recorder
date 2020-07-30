import os
import json

from colorama import init, Fore
init(autoreset=True)

def setup_settings(file_name):
    # Check, copy file to current_settings.json
    if os.path.exists(file_name):
        fobj_r = open(file_name, "r")
        fobj_w = open("current_settings.json", "w")
        json.dump(json.load(fobj_r), fobj_w)
    else:
        print(Fore.RED+"Input file does not exists")

    return None

def print_current_settings():
    # Read, print nicely current_settings.json
    fobj_r = open("current_settings.json", "r")
    settings = json.load(fobj_r)
    print(Fore.GREEN+"Current settings: ")
    print(json.dumps(settings, indent = 3))
    return None

def load_settings():
    fobj_r = open("current_settings.json", "r")
    settings = json.load(fobj_r)
    fobj_r.close()
    return settings
