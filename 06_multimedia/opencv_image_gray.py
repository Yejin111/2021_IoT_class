import cv2

img = cv2.imread('wiwiwi.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('wiwiwi', img)
cv2.imshow('wiwiwi_gray', gray)

while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('wiwiwi_gray.jpg', gray)



cv2.destroyAllwindows()
