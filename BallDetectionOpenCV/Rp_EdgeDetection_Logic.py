# import the necessary packages
import cv2
import numpy as np
# Reading input image to be processed
baseball_image_x = cv2.imread('IMG14.bmp')
# Keeping a copy of input image to output image
output_image = baseball_image_x.copy()
image_edges = cv2.Canny(baseball_image_x,10,200)

resized_image_edges = cv2.resize(image_edges, (640,512))
cv2.imshow("Rp_EdgeDetection_Logic.py: EDGES DETECTED IN THE IMAGE", resized_image_edges)

# detect circles in the image
image_circles = cv2.HoughCircles(image_edges, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=10, maxRadius=31)
# Draw circles in the image with colour Green
if image_circles is not None:
    detected_circles = np.uint16(np.around(image_circles))
    for (x, y, r) in detected_circles[0,:]:
        cv2.circle(output_image, (x, y), r, (0, 255, 0), 3)
        cv2.circle(output_image, (x, y), 2, (0, 255, 0), 3)
# Display circles in the image if there is any
resized_output_image = cv2.resize(output_image, (640,512))
cv2.imshow("Rp_EdgeDetection_Logic.py: CIRCLES DETECTED IN THE EDGE IMAGE", resized_output_image)
cv2.waitKey(0)