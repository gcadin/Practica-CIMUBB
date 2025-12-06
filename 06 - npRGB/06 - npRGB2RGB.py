import cv2
import numpy as np

bgr = cv2.imread("prueba.jpg")
canal1 = bgr[:,:,0]
canal2 = bgr[:,:,1]
canal3 = bgr[:,:,2]
cv2.imshow("BGR", np.hstack([canal1,canal2,canal3]))

rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
canal1 = rgb[:,:,0]
canal2 = rgb[:,:,1]
canal3 = rgb[:,:,2]
cv2.imshow("RGB", np.hstack([canal1,canal2,canal3]))

gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
cv2.imshow("GRAY", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()