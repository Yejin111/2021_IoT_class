import cv2

face_cascade = cv2.CascadeClassifier('./xml/face.xml')

img = cv2.imread('Jun Ha.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#이미지에서 얼굴 식별하기
faces = face_cascade.detectMultiScale(gray)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
