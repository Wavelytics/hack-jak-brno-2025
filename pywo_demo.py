"""
Demo application of face-mesh projection using Google MediaPipe
and openCV webcam video capture for Pywo
Date: 12.01.2026
Authors: Vaclav Steinbach Lubos Smolik, Jakub Sulda, Zdenek Kubin
"""
import cv2 # webcam
import mediapipe as mp # face-mesh

def main():
    # Initialize webcam
    cam = cv2.VideoCapture(0)

    # Initialize MediaPipe face-mesh
    mp_face = mp.solutions.face_mesh
    face_mesh = mp_face.FaceMesh(
        max_num_faces=2,
        refine_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    )

    # Webcam capture main loop
    while True:
        success, frame = cam.read()
        if not success or frame is None:
            print("Ignoring empty camera frame.")
            continue

        # Mirror effect correction
        frame = cv2.flip(frame, 1)

        # Convert to RGB for MediaPipe
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # MediaPipe projection
        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                h, w, _ = frame.shape
                  
                # Draw all landmarks on Webcam Feed
                for lm in face_landmarks.landmark:
                    x, y = int(lm.x * w), int(lm.y * h)
                    cv2.circle(frame, (x, y), 1, (0, 255, 0), -1)

        cv2.imshow("Demo", frame)
            
        # Exit on ESC key
        if cv2.waitKey(5) & 0xFF == 27:
            break
    
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()