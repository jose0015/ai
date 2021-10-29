# import the necessary packages
import cv2
import numpy as np
# Reading input image to be processed
baseball_image = cv2.imread('IMG14.bmp')
output_image = baseball_image.copy()
baseball_image_blurr = cv2.medianBlur(baseball_image, 7)
gray_image = cv2.cvtColor(baseball_image_blurr, cv2.COLOR_BGR2GRAY)
# detect circles in the image
image_circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=15, maxRadius=30)
# Draw circles in the image with colour Green
if image_circles is not None:
    detected_circles = np.uint16(np.around(image_circles))
    print (detected_circles)
    for (x, y, r) in detected_circles[0,:]:
        cv2.circle(output_image, (x, y), r, (0, 255, 0), 3)
        cv2.circle(output_image, (x, y), 2, (0, 255, 0), 3)
# Display circles in the image if there is any
Resized_image = cv2.resize(output_image, (640,512))
cv2.imshow("Rp_CircleDetection_Logic.py: DETECTED BALL LOCATIONS IN THE IMAGE", Resized_image)
cv2.waitKey(0)