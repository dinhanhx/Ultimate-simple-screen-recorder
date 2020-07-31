# Ultimate simple screen recorder

Or USSR for short

[![HitCount](http://hits.dwyl.com/dinhanhx/Ultimate-simple-screen-recorder.svg)](http://hits.dwyl.com/dinhanhx/Ultimate-simple-screen-recorder)
![](https://img.shields.io/badge/Python-3-blue)
![](https://img.shields.io/badge/Cross--platform-True-brightgreen)
![](https://img.shields.io/badge/license-MIT-green)

[![](https://img.shields.io/badge/Author-Vu%20Dinh%20Anh-red)](https://github.com/dinhanhx)

## 1 Introduction

### Why I make this tool?

I always encounter black screen errors of OBS on Windows. "Why did you just choose another OS or screen recorder?" I have tried a lot (the list is long) but I could not get used to any of them.

Fun fact: I use Windows Subsystem for Linux

### How I make this tool?

My friend: "Don't use Python for this project. Python is slow."

Me: "I know, that why I use, I want to try my best to make something faster!"

Ussr is made in Python 3.7 with a lot of dependencies to make Ussr become compatible with every platforms.

## 2 Installation

You can check for release section of this repos for pre-compiled binary files. Using these files, you don't need to install Python 3.

### Windows

You need Python 3. You can clone this repos and setup all dependencies in file `req_for_windows.txt` and go to folder `whl` to install the dependencies via .whl files (Example: PyAudio). Then you are good to go.

You can skip this part. This is for people who want to make ussr dependent from Python LVM.

Then you can use this command to create binary files

```
pyinstaller --onefile ussr.py
```

Note that:
  - Make sure you copy current_settings.json (from the repos) to the folder (`dist`) that has ussr.exe
  - [Make sure you have opencv_videoio_ffmpeg420_64.dll](https://stackoverflow.com/a/62014968/13358358)

### Not Windows

(Yes I know UNIX and GNU/LINUX)

You need Python 3. You can clone this repos and setup all dependencies in file `req_for_not_windows.txt`. Then you are good to go.

You can skip this part. This is for people who want to make ussr dependent from Python LVM.

Then you can use this command to create binary files

```
pyinstaller --onefile ussr.py
```

Note that:
  - Make sure you copy current_settings.json (from the repos) to the folder (`dist`) that has ussr (executable file)
  - [Make sure you have opencv_videoio_ffmpeg420_64.dll](https://stackoverflow.com/a/62014968/13358358)

## 3 Usage

### `ussr -h`

Or `py ussr.py -h` if you use Python LVM

To show help section

### `ussr -s your_settings.json`

Or `py ussr.py -s your_settings.json` if you use Python LVM

To load/setup your settings.

Just read `currrent_settings.json` and if you make a copy of the following json block of code, please remove all "comments"

```json
{
   "fps": 24, // fps of the video
   "output folder": "ussr_vid", // should be full path if change
   "stop key": "alt+q", // must know about Python module keyboard
   "date format": "%d_%m_%Y_%H_%M_%S", // must know about Python module datetime
   "tail": ".avi", // must know about Python module opencv
   "fourcc": "XVID" // must know about Python module opencv
}
```

### `ussr -s -i`

Or `py ussr.py -s -i` if you use Python LVM

To show your settings

### `ussr -r`

Or `py ussr.py -r` if you use Python LVM

To record your screen fully.

Press "Alt+Q" to stop this process.
