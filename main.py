# main.py
import cv2
from bicep_curl import BicepCurl
from shoulder_press import ShoulderPress

# Initialize exercise classifiers
bicep_curl = BicepCurl()
shoulder_press = ShoulderPress()

# Capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Classify exercises
    bicep_curl_state = bicep_curl.classify(frame)
    shoulder_press_state = shoulder_press.classify(frame)

    # Display feedback on the frame
    cv2.putText(frame, f'Bicep Curl: {bicep_curl_state}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.putText(frame, f'Shoulder Press: {shoulder_press_state}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Exercise Classification', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()