import os
import sys
import json
from colorama import init, Fore
init(autoreset=True)

def print_help():
    # Print cmds and descriptions
    print(Fore.YELLOW+"Welcome to Ultimate simple screen recorder")
    print(Fore.RED+"For the art, for the people, for the minimalism")
    print("Here are available cmds\n")

    print(Fore.GREEN+"ussr -h")
    print("To show this section\n")

    print(Fore.GREEN+"ussr -s settings.json")
    print("To load settings\n")

    print(Fore.GREEN+"ussr -s -i")
    print("To show settings infor\n")

    print(Fore.GREEN+"ussr -r")
    print("To record your screen fully\n")
    return None

def print_windows_help():
    # Print easter egg
    print(Fore.YELLOW+"Union of Soviet Socialist Republics")
    print(Fore.RED+"Workers of the world, unite!")
    return None

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

# Cmd parsers
if len(sys.argv) == 1:
    print_help()

if len(sys.argv) >= 2:
    if sys.argv[1] == "-h": # ussr -h
        print_help()

    if sys.argv[1] == "/?": # ussr /?
        print_windows_help()

    if len(sys.argv) >= 3:
        if sys.argv[1] == "-s":
            if sys.argv[2].split(".")[-1] == "json": # ussr -s settings.json
                setup_settings(sys.argv[2])

            if sys.argv[2] == "-i": # ussr -s -i
                print_current_settings()

        if sys.argv[1] == "-r": # ussr -r
            pass

        else:
            print_help()
