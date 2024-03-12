import cv2
import os

# Create a directory to save images if it doesn't exist
save_dir = 'captured_images'
os.makedirs(save_dir, exist_ok=True)

# Initialize the camera
cam = cv2.VideoCapture(0)

while True:
    # Read frame from the camera
    ret, image = cam.read()
    
    # Display the frame
    cv2.imshow('Imagetest', image)
    
    # Check for key press
    k = cv2.waitKey(1)
    
    # If any key is pressed, break the loop
    if k != -1:
        break

# Save the captured image in the specified directory
image_path = os.path.join(save_dir, 'testimage.jpg')
cv2.imwrite(image_path, image)

# Release the camera
cam.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
