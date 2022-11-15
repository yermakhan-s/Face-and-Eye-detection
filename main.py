import numpy as np

import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 5)
        roi_gray = gray[y:y + w, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        smiled=False
        for (sx, sy, sw, sh) in smiles:
            smiled=True
        if smiled:
            cv2.putText(img=frame, text='Beautiful', org=(x + w, y), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1,
                        color=(0, 0, 0), thickness=3)
        else:
            cv2.putText(img=frame, text='Smile', org=(x + w, y), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1,
                        color=(0, 0, 0), thickness=3)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
