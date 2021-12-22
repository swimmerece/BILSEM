import cv2
resim = cv2.imread("nasa.jpg",0)  #0 resmi gri yapar
cv2.imshow("NASA", resim)
cv2.imwrite("nasa_new", resim)
cv2.waitkey(0)
cv2.destroyAllWindows()
