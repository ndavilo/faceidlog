import tkinter as tk
import threading
import time

def alert_user(message):
    """
    Display an alert message to the user.

    Args:
        message (str): The message to be displayed in the alert.

    Returns:
        None
    """
    alert_window = tk.Tk()
    alert_window.title("Alert")
    
    label = tk.Label(alert_window, text=message)
    label.pack()
    
    # Function to close the alert window after 10 seconds
    def close_alert():
        time.sleep(10)
        alert_window.destroy()

    # Start a new thread to close the alert window after 10 seconds
    threading.Thread(target=close_alert).start()

    alert_window.mainloop()
