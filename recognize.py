import os
import cv2
from capture import capture_one_frame

def recognize_face():
    """
    Recognize the face by comparing it with the saved images.

    Returns:
        str: Name of the recognized user.
    """
    frame = capture_one_frame()

    # Path to the directory containing captured images
    captured_images_dir = 'captured_images'

    # Load the cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # If no face is detected, return None
    if len(faces) == 0:
        return None

    # Iterate through each face detected
    for (x, y, w, h) in faces:
        # Extract the face region from the frame
        roi_gray = gray[y:y+h, x:x+w]

        # Compare the extracted face with saved images
        for image_name in os.listdir(captured_images_dir):
            image_path = os.path.join(captured_images_dir, image_name)
            saved_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Resize saved image to match the size of the detected face
            saved_image = cv2.resize(saved_image, (w, h))

            # Compare the two images using the mean squared error
            mse = ((roi_gray - saved_image) ** 2).mean()

            # If the mean squared error is below a certain threshold, consider it a match
            if mse < 100:
                return image_name.split('_')[0]  # Return the name of the recognized user

    return None  # If no match is found, return None
