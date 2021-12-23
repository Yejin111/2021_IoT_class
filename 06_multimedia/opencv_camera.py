import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Camera open failed')
    exit()

# ret, frame = cap.read()
# cv2.imshow('frame', frame)
# cv2.waitKey(0)
# cv2.imwrite('output.jpg', frame)

# 동영상 촬영하기

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('frame', frame)
    # 1000 -> 1초, 10 -> 0.01초

    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllwindows()