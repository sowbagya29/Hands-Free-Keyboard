import cv2
import numpy as np

# All alphabets
keys = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
selected_key = 0
typed_text = ""

# Open webcam and set resolution
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    height, width = frame.shape[:2]

    # Show typed text
    cv2.putText(frame, "Typed: " + typed_text, (50, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 3)

    # Draw keyboard in 3 rows
    for i, key in enumerate(keys):
        if i < 9:
            row = 0
            col = i
        elif i < 18:
            row = 1
            col = i - 9
        else:
            row = 2
            col = i - 18

        key_width = 80
        key_height = 80
        spacing_x = 100
        spacing_y = 100

        x = 100 + col * spacing_x
        y = 200 + row * spacing_y

        color = (0, 255, 0) if i == selected_key else (200, 200, 200)
        cv2.rectangle(frame, (x, y), (x + key_width, y + key_height), color, -1)
        cv2.putText(frame, key, (x + 25, y + 55),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 3)

    # Simulated eye region
    roi = frame[100:200, width//2 - 50:width//2 + 50]
    avg_color = np.mean(roi)

    # Move selection
    if avg_color > 120:
        selected_key = (selected_key + 1) % len(keys)
    else:
        selected_key = (selected_key - 1) % len(keys)

    # Highlight selection
    cv2.rectangle(frame, (width//2 - 50, 100), (width//2 + 50, 200), (255, 0, 0), 2)
    cv2.putText(frame, f"Selected: {keys[selected_key]}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    # Show final frame
    cv2.imshow("3-Line Eye-Controlled Keyboard", frame)

    key = cv2.waitKey(200) & 0xFF
    if key == 27:  # ESC to exit
        break
    elif key == 32:  # Spacebar to select
        typed_text += keys[selected_key]

cap.release()
cv2.destroyAllWindows()
