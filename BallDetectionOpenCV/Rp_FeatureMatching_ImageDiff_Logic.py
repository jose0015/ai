# import the necessary packages
import cv2
import numpy as np
# Reading input image to be processed
baseball_image_x = cv2.imread('IMG14.bmp')
baseball_image_y = cv2.imread('IMG13.bmp')
baseball_image_diff = baseball_image_x - baseball_image_y
output_image = baseball_image_x.copy()
baseball_image_blurr_diff = cv2.medianBlur(baseball_image_diff,  5) #   GaussianBlur
gray_image = cv2.cvtColor(baseball_image_blurr_diff, cv2.COLOR_BGR2GRAY)
Resized_image = cv2.resize(gray_image, (320,256))
cv2.imshow("Rp_Feature_Matching_ImageDiff_Logic.py: DIFFERENCE BETWEEN CONSECUTIVE IMAGES", Resized_image)

#feature matching steps
baseball_WHITE = cv2.imread('cropped_white.bmp')
baseball_GRAY = cv2.imread('cropped_gray.bmp')
WHITE_gray_template = cv2.cvtColor(baseball_WHITE, cv2.COLOR_BGR2GRAY)
GRAY_gray_template = cv2.cvtColor(baseball_GRAY, cv2.COLOR_BGR2GRAY)
result_image_WHITE = cv2.matchTemplate(gray_image, WHITE_gray_template, cv2.TM_CCOEFF_NORMED)
result_image_GRAY = cv2.matchTemplate(gray_image, GRAY_gray_template, cv2.TM_CCOEFF_NORMED)
loc_WHITE = np.where(result_image_WHITE >= 0.70)
loc_GRAY = np.where(result_image_GRAY >= 0.70)
print(loc_WHITE)
print(loc_GRAY)
# Draw circles in the image with colour Green
for pt_white in zip(*loc_WHITE):
    print(pt_white)
    (y, x) = pt_white
    cv2.circle(output_image, (x+20, y+20), 1, (0, 255, 0), 3)
    cv2.circle(output_image, (x+20, y+20), 20, (0, 255, 0), 3)
# Draw circles in the image with colour Green
for pt_gray in zip(*loc_GRAY):
    print(pt_gray)
    (y, x) = pt_gray
    cv2.circle(output_image, (x+20, y+20), 1, (0, 255, 0), 3)
    cv2.circle(output_image, (x+20, y+20), 20, (0, 255, 0), 3)
# Display circles in the image if there is any
Resized_image = cv2.resize(result_image_WHITE, (320,256))
cv2.imshow("Rp_FeatureMatching_ImageDiff_Logic.py: RESULT OF WHITE MATCH TEMPLATE IN IMAGE", Resized_image)
Resized_image = cv2.resize(result_image_GRAY, (320,256))
cv2.imshow("Rp_FeatureMatching_ImageDiff_Logic.py: RESULT OF GRAY MATCH TEMPLATE IN IMAGE", Resized_image)

Resized_image = cv2.resize(output_image, (320,256))
cv2.imshow("Rp_FeatureMatching_ImageDiff_Logic.py: DETECTED BALL LOCATIONS FROM MATCH TEMPLATE METHOD", Resized_image)
cv2.waitKey(0)