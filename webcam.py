import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 for default webcam, change to 1 for external webcam

while True:
    ret, frame = cap.read()  # Read a frame from the webcam

    cv2.imshow('Webcam Stream', frame)  # Display the frame

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()  # Release the VideoCapture object
cv2.destroyAllWindows()  # Close all OpenCV windows