# mediapipe_estimator.py
import cv2
from pose_estimator import MediaPipePoseEstimator

def process_webcam():
    cap = cv2.VideoCapture(0)  # Open the default webcam
    pose_estimator = MediaPipePoseEstimator()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        landmarks = pose_estimator.estimate(frame)
        if landmarks:
            pose_estimator.draw_landmarks(frame, landmarks)

        cv2.imshow('MediaPipe Pose', frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_webcam()