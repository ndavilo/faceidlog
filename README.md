Description:

This Python code implements a system for clocking in and out using face recognition technology. The system is designed to recognize registered staff members using facial recognition and log their clock-in and clock-out times along with their user names and file numbers.

Features:

Face Recognition: Utilizes face recognition to identify registered staff members.
Registration: Allows staff members to register by capturing multiple frames of their faces and saving their details, including user names and file numbers.
Clock In/Out: Enables registered staff members to clock in and out by presenting their faces to the system, which logs their time along with their user names and file numbers.
Components:

main.py: Contains the main functionality of the clock-in and clock-out system, including user interaction and option selection.
logger.py: Provides functions for registering users, logging clock-in and clock-out times, and saving user details.
capture.py: Implements functions for capturing frames from the webcam and recognizing faces for registration and clocking in/out.
Usage:

Run main.py.
Choose an option to register a new user or to clock in/out.
Follow the prompts to register or to perform clock in/out operations.
Dependencies:

opencv-python: OpenCV library for computer vision tasks, including face recognition.
pandas: Library for data manipulation and analysis, used for handling user details and log data.