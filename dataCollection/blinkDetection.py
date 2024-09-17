import dlib
import numpy as np
from scipy.spatial import distance as dist

# Initialize dlib's face detector and facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat\shape_predictor_68_face_landmarks.dat')

# Indices for the left and right eyes in the facial landmark predictor
(L_START, L_END) = (42, 48)
(R_START, R_END) = (36, 42)

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# Eye Aspect Ratio threshold for detecting closed eyes
EAR_THRESHOLD = 0.25

# Variable to track the previous eye state
previous_eye_state = None

# Open a video capture (webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = np.array([[p.x, p.y] for p in shape.parts()])

        # Extract the left and right eye coordinates
        leftEye = shape[L_START:L_END]
        rightEye = shape[R_START:R_END]

        # Calculate the EAR for both eyes
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # Average the EAR for both eyes
        ear = (leftEAR + rightEAR) / 2.0

        # Determine the current eye state
        if ear < EAR_THRESHOLD:
            current_eye_state = 0  # Eyes closed
            cv2.putText(frame, "Eyes Closed", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            current_eye_state = 1  # Eyes open
            cv2.putText(frame, "Eyes Open", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Only output the eye state if it has changed
        if current_eye_state != previous_eye_state:
            print(current_eye_state)
            # You could also send the current_eye_state to other devices here

            # Update the previous eye state
            previous_eye_state = current_eye_state

    # Show the video feed with the eye state annotation
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
