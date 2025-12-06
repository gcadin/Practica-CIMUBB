import cv2

img = cv2.imread('contornos.jpg')
#img = 255 - img

img_list = img.copy()
img_external = img.copy()
img_ccomp = img.copy()
img_tree = img.copy()


gray = cv2.cvtColor(img_list, cv2.COLOR_BGR2GRAY)
#_, th = cv2.threshold(img_list, 80, 255, cv2.THRESH_BINARY)
_, th = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY)

contorno_list, hierarchy1 = cv2.findContours(th, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contorno_external, hierarchy2 = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contorno_ccomp, hierarchy2 = cv2.findContours(th, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
contorno_tree, hierarchy2 = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img_list, contorno_list, -1, (0, 255, 255), 3)
cv2.drawContours(img_external, contorno_external, -1, (0, 255, 255), 3)
cv2.drawContours(img_ccomp, contorno_ccomp, -1, (0, 255, 255), 3)
cv2.drawContours(img_tree, contorno_tree, -1, (0, 255, 255), 3)

cv2.imshow('imagen tree', img_tree)
cv2.imshow('imagen ccomp', img_ccomp)
cv2.imshow('imagen external', img_external)
cv2.imshow('imagen list', img_list)
cv2.imshow('th', th)
cv2.imshow('imagen', img)

cv2.waitKey(0)
cv2.destroyAllWindows()