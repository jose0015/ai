# import the necessary packages
import cv2
import numpy as np
# Reading input image to be processed
baseball_image_x = cv2.imread('IMG14.bmp')
baseball_image_y = cv2.imread('IMG13.bmp')
baseball_image_diff = baseball_image_x - baseball_image_y
output_image = baseball_image_x.copy()
baseball_image_blurr_diff = cv2.medianBlur(baseball_image_diff,  5)
gray_image = cv2.cvtColor(baseball_image_blurr_diff, cv2.COLOR_BGR2GRAY)
Resized_image = cv2.resize(gray_image, (640,512))
cv2.imshow("Rp_CircleDetection_ImageDiff_Logic.py: DIFFERENCE BETWEEN CONSECUTIVE IMAGES", Resized_image)
# detect circles in the image
image_circles = cv2.HoughCircles(gray_image, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=35)
# Draw circles in the image with colour Green
if image_circles is not None:
    detected_circles = np.uint16(np.around(image_circles))
    print (detected_circles)
    for (x, y, r) in detected_circles[0,:]:
        cv2.circle(output_image, (x, y), r, (0, 255, 0), 3)
        cv2.circle(output_image, (x, y), 2, (0, 255, 0), 3)
# Display circles in the image if there is any
Resized_image = cv2.resize(output_image, (640,512))
cv2.imshow("Rp_CircleDetection_ImageDiff_Logic.py: DETECTED BALL LOCATIONS IN CONSECUTIVE IMAGES", Resized_image)
cv2.waitKey(0)