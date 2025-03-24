import cv2
import time
import threading
from twilio_alert import make_phone_call

# Load OpenCV face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

last_call_time = 0
face_disappeared_time = None
CALL_INTERVAL = 1 * 60  # 15 minutes
detection_running = False  # Flag to control detection


def detect_face():
    global last_call_time, face_disappeared_time, detection_running

    cap = cv2.VideoCapture(0)  # Use system camera
    detection_running = True  # Set running flag

    while detection_running:  # Check this flag to stop detection
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            face_disappeared_time = None
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, "Face Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        else:
            if face_disappeared_time is None:
                face_disappeared_time = time.time()

            time_elapsed = time.time() - face_disappeared_time

            if time_elapsed > 5:
                cv2.putText(frame, "Face Covered!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                current_time = time.time()
                if current_time - last_call_time > CALL_INTERVAL:
                    threading.Thread(target=make_phone_call, daemon=True).start()
                    last_call_time = current_time

        cv2.imshow("Face Obstruction Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def stop_detection():
    global detection_running
    detection_running = False  # Set flag to stop detection
