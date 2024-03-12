import cv2
from tkinter import messagebox
import os

def capture_frames(user_name, file_number, save_dir):
    """
    Capture frames from webcam and save them as images.

    Args:
        user_name (str): The name of the user.
        file_number (int): The file number to start naming images.
        save_dir (str): The directory to save captured images.

    Returns:
        None

    Notes:
        This function captures 5 frames from the webcam, detects faces in each frame, 
        and saves images with rectangles drawn around detected faces.

    """
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)

    count = 1  # Initialize image count
    while count <= 5:  # Capture 5 images
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

        if len(faces) == 1:
            file_name = f'{user_name}_{file_number}_{count}.jpg'  # Image name format
            file_path = os.path.join(save_dir, file_name)  # Full file path
            cv2.imwrite(file_path, frame)
            count += 1
            
            # Display successful prompt
            cv2.putText(frame, "Image captured successfully!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        cv2.imshow('Frame', frame)
        
        # Prompt user to press any key
        print("Press any key to capture the image.")
        cv2.waitKey(0)
        
    cap.release()
    cv2.destroyAllWindows()


def capture_one_frame():
    """
    Capture a single frame from the webcam.

    Returns:
        frame: The captured frame.
    """
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if ret:
            # Convert frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Load face cascade classifier
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Detect faces in the frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            if len(faces) > 0:
                cap.release()
                return frame

        # Prompt user to try again or exit
        response = messagebox.askyesno("Face not detected", "No face detected. Do you want to try again?")

        if not response:
            cap.release()
            return None
