import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

while True:
    ret, img = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier('./xml/face.xml')
    eye_cascade = cv2.CascadeClassifier('./xml/eye.xml')

    faces = face_cascade.detectMultiScale(gray)

    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)

        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('frame',img)

    if cv2.waitKey(10) == 27:
        break

cap.release()
cv2.destoryAllWindows()