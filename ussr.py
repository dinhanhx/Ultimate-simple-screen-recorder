import os
import sys
import json
from video import make_video
from audio import make_audio
from setting import setup_settings, print_current_settings
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

# Cmd parsers
if len(sys.argv) == 1:
    print_help()

if len(sys.argv) >= 2:
    if sys.argv[1] == "-h": # ussr -h
        print_help()

    if sys.argv[1] == "/?": # ussr /?
        print_windows_help()

    if sys.argv[1] == "-r": # ussr -r
        make_video()

    if len(sys.argv) >= 3:
        if sys.argv[1] == "-s":
            if sys.argv[2].split(".")[-1] == "json": # ussr -s settings.json
                setup_settings(sys.argv[2])

            if sys.argv[2] == "-i": # ussr -s -i
                print_current_settings()
