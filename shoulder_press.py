from pose_estimator import MediaPipePoseEstimator
from measure import calculate_angle

LANDMARKS = {
    'LEFT_SHOULDER': 11,
    'LEFT_ELBOW': 13,
    'LEFT_WRIST': 15,
    'LEFT_HIP': 23,
    'LEFT_KNEE': 25,
    'LEFT_ANKLE': 27,
    'RIGHT_SHOULDER': 12,
    'RIGHT_ELBOW': 14,
    'RIGHT_WRIST': 16,
    'RIGHT_HIP': 24,
    'RIGHT_KNEE': 26,
    'RIGHT_ANKLE': 28,
}

class ShoulderPress:
    def __init__(self):
        self.pose_estimator = MediaPipePoseEstimator()

    def classify(self, image):
        landmarks = self.pose_estimator.estimate(image)
        if not landmarks:
            return "No Pose Detected"

        left_shoulder_angle = self.get_angle(landmarks, 'LEFT_HIP', 'LEFT_SHOULDER', 'LEFT_ELBOW')
        if left_shoulder_angle > 160:
            return "Lower"
        elif left_shoulder_angle < 30:
            return "Raise"
        else:
            return "Hold"

    def get_angle(self, landmarks, point1, point2, point3):
        idx1 = LANDMARKS[point1]
        idx2 = LANDMARKS[point2]
        idx3 = LANDMARKS[point3]

        a = [landmarks.landmark[idx1].x, landmarks.landmark[idx1].y]
        b = [landmarks.landmark[idx2].x, landmarks.landmark[idx2].y]
        c = [landmarks.landmark[idx3].x, landmarks.landmark[idx3].y]
        return calculate_angle(a, b, c)