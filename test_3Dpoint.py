import cv2
import numpy as np

image = cv2.imread('uzumaki_naruto.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

depth_map = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

h, w = depth_map.shape[:2]
X, Y = np.meshgrid(np.arange(w), np.arange(h))
Z = gray.astype(np.float32)

points_3d = np.dstack((X, Y, Z))

cv2.imwrite("output_image.jpg", depth_map)

cv2.imshow('Depth Map', depth_map)
cv2.waitKey(0)
cv2.destroyAllWindows()