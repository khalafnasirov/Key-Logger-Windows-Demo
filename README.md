# Key-Logger-Windows-Demo
Educational Purpose

## WHAT IS IT?

## REQUIREMENTS
Run these commands
`pip install keyboard`
`pip install pygetwindow pynput`

## HOW IS IT WORKING?
Once you run this script it starts run on background silently tracking your every keyboard input and collect them in one data. It also record what is your active window.
So every 120 seconds (you can modify that) it creates new .txt file and sends it to your selected email, and then removes that file from system.
Program can be seen on task manager, so you can end task from that.

## SCREENSHOTS


## HOW TO TURN THIS INTO EXECUTABLE FILE
First install this module
`pip install pyinstaller`
Then run this command to make .exe file
`python3 -m PyInstaller --onefile --noconsole ./yourscript.py`
