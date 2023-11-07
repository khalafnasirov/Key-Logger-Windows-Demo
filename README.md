# KEY LOGGER FOR WINDOWS

## WHAT IS IT?
Keyboard input logger for windows which sends information through google email service to any email in every selected time interval

## REQUIREMENTS
For python
`pip install keyboard`
`pip install pygetwindow pynput`

* It only works on windows system

## HOW IS IT WORKING?
Once you run this script it starts run on background silently tracking your every keyboard input and collect them in one data. It also record what is your active window.
So every 120 seconds (you can modify that) it creates new .txt file and sends it to your selected email, and then removes that file from system.
Program can be seen on task manager, so you can end task from that.

## SCREENSHOTS
Exported log file
![](https://github.com/khalafnasirov/Media-of-Repositories/blob/82ec63e4c884e01207cbe092d5a3b2eddf7a717c/Key-Logger/Screenshot%202023-11-07%20100417.png)

## MODIFABLE PARTS
  * `sender_email` - Email you use to send to other email
  * `recipient_email` - Email you send file to
  * `password` - Go to your google email account and search for *App Passwords* in search tab (!If it doesn't appear make you sure enable two-factor authontication)
  * `task_interval` - Time interval program sends file to email 

## HOW TO TURN THIS INTO EXECUTABLE FILE
First install this module
`pip install pyinstaller`
Then run this command to make .exe file
`python3 -m PyInstaller --onefile --noconsole ./yourscript.py`
