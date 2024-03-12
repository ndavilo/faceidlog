import os
import pandas as pd
from datetime import datetime
import pyautogui
from tkinter import simpledialog
from capture import capture_frames
from recognize import recognize_face
import threading
from alert import alert_user

def register_user(save_dir):
    """
    Register a new user by capturing their face and saving details.

    Args:
        save_dir (str): Directory to save captured images.

    Returns:
        None

    Notes:
        This function prompts the user to input their name and file number, 
        captures multiple frames of the user's face, saves them, and then 
        saves user details to a CSV file.
    """
    user_name = simpledialog.askstring("Input", "Enter user name:")
    if user_name:
        file_number = simpledialog.askstring("Input", "Enter file number:")
        if file_number:
            capture_frames(user_name, file_number, save_dir)
            save_user_details(user_name, file_number)

def save_user_details(user_name, file_number):
    """
    Save user details to a CSV file.

    Args:
        user_name (str): Name of the user.
        file_number (str): File number associated with the user.

    Returns:
        None

    Notes:
        This function saves the user's name and file number to a CSV file.
    """
    user_data = {'User Name': user_name, 'File Number': file_number}
    df = pd.DataFrame(user_data, index=[0])

    if not os.path.exists('user_details.csv'):
        df.to_csv('user_details.csv', index=False)
    else:
        df.to_csv('user_details.csv', mode='a', header=False, index=False)

def clock_in_out():
    """
    Clock in/out functionality.

    Args:
        None

    Returns:
        None

    Notes:
        This function prompts the user to initiate clocking, recognizes their face, 
        and logs the current time along with the user's name to a CSV file.
    """
    pyautogui.alert('Please click or move the mouse to initiate clocking.')
    user_name = recognize_face()

    if user_name:
        message = f"Welcome, {user_name}!"
        log_time(user_name)
        threading.Thread(target=alert_user, args=(message,)).start()
        
    log_time(user_name)

def log_time(user_name):
    """
    Log clock in/out time.

    Args:
        user_name (str): Name of the user.

    Returns:
        None

    Notes:
        This function logs the current clock in/out time along with the user's name 
        to a CSV file named with the current date.
    """
    today = datetime.today().strftime('%Y-%m-%d')
    now = datetime.now().strftime('%H:%M:%S')

    log_data = {'User Name': user_name, 'Clock In/Out': now}
    df = pd.DataFrame(log_data, index=[0])

    file_name = f'clock_logs_{today}.csv'
    if not os.path.exists(file_name):
        df.to_csv(file_name, index=False)
    else:
        df.to_csv(file_name, mode='a', header=False, index=False)
