import os
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

    while True:
        choice = input("Choose an option:\n1. Register User\n2. Clock In/Out\n3. Exit\n")

        if choice == '1':
            register_user(save_dir)
        elif choice == '2':
            clock_in_out()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
