import numpy as np
import time

def detect_iris(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    # Increase contrast
    alpha = 2.0  # Contrast control
    beta = 0     # Brightness control
    gray = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)
   
    # Use GaussianBlur to reduce noise and improve circle detection
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)
   
    #Apply adaptive thresholding
    adaptive_thresh = cv2.adaptiveThreshold(
         blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
         cv2.THRESH_BINARY, 11, 2
    )
   
    # Use Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(
        blurred,
        cv2.HOUGH_GRADIENT, dp=1, minDist=20,
        param1=50, param2=50,  # Adjusted parameter for higher selectivity
        minRadius=20, maxRadius=60  # Adjusted radius range
    )
   
    iris_locations = []

    # Draw the detected circles on the original image
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            cx, cy, radius = circle
            # Filter out circles that are too small or too large
            if 20 < radius < 60:
                # Draw the circle for the iris
                cv2.circle(image, (cx, cy), radius, (255, 0, 0), 2)
                cv2.putText(image, f"Center: ({cx}, {cy})",
                            (cx - radius, cy - radius - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                iris_locations.append((cx, cy))
   
    return image, iris_locations

# Initialize both camera inputs
left_eye_camera = cv2.VideoCapture(0)  # Camera for left eye
right_eye_camera = cv2.VideoCapture(1)  # Camera for right eye

# Function to switch between cameras
def switch_camera(cam_num):
    if cam_num == 0:
        return left_eye_camera
    elif cam_num == 1:
        return right_eye_camera
    return None

# Start with left eye camera (0 for left, 1 for right)
current_eye = 0

# Time tracking for output interval
last_time = time.time()
last_printed_locations = []

while True:
    # Switch between left and right eye cameras
    camera = switch_camera(current_eye)
    ret, frame = camera.read()

    if not ret:
        break

    # Detect iris and get the location
    processed_frame, iris_locations = detect_iris(frame)
   
    # Display the frame with detected iris
    if current_eye == 0:
        cv2.imshow('Left Eye Iris Detection', processed_frame)
    else:
        cv2.imshow('Right Eye Iris Detection', processed_frame)
   
    # Print the iris locations to the console once per second
    current_time = time.time()
    if current_time - last_time >= 1:  # Check if one second has passed
        if iris_locations != last_printed_locations:
            if iris_locations:
                print(f"Iris locations: {iris_locations}")
                last_printed_locations = iris_locations
        last_time = current_time
   
    # Switch eyes based on user input (press 'l' for left, 'r' for right, 'q' to quit)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('l'):  # Switch to left eye camera
        current_eye = 0
    elif key == ord('r'):  # Switch to right eye camera
        current_eye = 1
    elif key == ord('q'):  # Quit the program
        break

# Release both cameras and close windows
left_eye_camera.release()
right_eye_camera.release()
cv2.destroyAllWindows()
