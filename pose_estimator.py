# pose_estimator.py
import cv2
import mediapipe as mp

class MediaPipePoseEstimator:
    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose()

    def estimate(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.pose.process(image_rgb)
        return results.pose_landmarks

    def draw_landmarks(self, image, landmarks):
        mp_drawing = mp.solutions.drawing_utils
        mp_drawing.draw_landmarks(image, landmarks, self.mp_pose.POSE_CONNECTIONS)