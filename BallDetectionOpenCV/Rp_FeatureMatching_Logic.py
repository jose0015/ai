# import the necessary packages
import cv2
import numpy as np
# Reading input image to be processed
baseball_image_x = cv2.imread('IMG13.bmp')
# Keeping a copy of input image to output image
output_image = baseball_image_x.copy()
grey_img = cv2.cvtColor(baseball_image_x, cv2.COLOR_BGR2GRAY)
#feature matching steps
baseball_template = cv2.imread('cropped_baseball_small.bmp')
grey_template = cv2.cvtColor(baseball_template, cv2.COLOR_BGR2GRAY)
result_image = cv2.matchTemplate(grey_img, grey_template, cv2.TM_CCOEFF_NORMED)
loc = np.where(result_image >= 0.90)
print(loc)
# Draw circles in the image with colour Green
for pt in zip(*loc):
    print(pt)
    (y, x) = pt
    cv2.circle(output_image, (x+20, y+20), 1, (0, 255, 0), 3)
    cv2.circle(output_image, (x+20, y+20), 20, (0, 255, 0), 3)
# Display circles in the image if there is any
Resized_image = cv2.resize(result_image, (640,512))
cv2.imshow("Rp_FeatureMatching_Logic.py: RESULT OF MATCH TEMPLATE ALGORITHM IN AN IMAGE", Resized_image)
Resized_image = cv2.resize(output_image, (640,512))
cv2.imshow("Rp_FeatureMatching_Logic.py: DETECTED BALL LOCATIONS FROM MATCH TEMPLATE METHOD", Resized_image)
cv2.waitKey(0)