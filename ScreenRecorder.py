import pyautogui
import cv2
import numpy as np

resolution = pyautogui.size()
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Screen Recorder", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Screen Recorder", 720, 470)
print("Recording... Press 'q' to stop.")

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  
    out.write(frame)
    cv2.imshow("Screen Recorder", frame)
    if cv2.waitKey(1) == ord("q"):
        break

out.release()
cv2.destroyAllWindows()