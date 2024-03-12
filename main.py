import os
import tkinter as tk
from logger import register_user, clock_in_out

def main():
    """
    Main function to interact with the user and provide options.

    Args:
        None

    Returns:
        None

    Notes:
        This function continuously prompts the user to choose an option: 
        registering a user, clocking in/out, or exiting the program.
    """
    save_dir = 'captured_images'
    os.makedirs(save_dir, exist_ok=True)

    def register_user_callback():
        register_user(save_dir)

    def clock_in_out_callback():
        clock_in_out()

    root = tk.Tk()
    root.title("User Registration and Time Logging System")

    label = tk.Label(root, text="Choose an option:")
    label.pack()

    register_button = tk.Button(root, text="Register User", command=register_user_callback)
    register_button.pack()

    clock_button = tk.Button(root, text="Clock In/Out", command=clock_in_out_callback)
    clock_button.pack()

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
