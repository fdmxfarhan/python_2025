import cv2

img = cv2.imread('pic.jpg')
img = cv2.blur(img, (30, 30))
cv2.imshow('img', img)


cv2.waitKey(0)
cv2.destroyAllWindows()