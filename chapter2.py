# ////////////////////////////important function////////////////////////////
import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

kernel = np.ones((5, 5), np.uint8)  # create kernel

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # convert to grayscale
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # blur image 7 is the blue intensity and o is the sigma
imgCanny = cv2.Canny(img, 200, 300)  # edge detection 100 is the threshold
# dilate the image when we have curev line or image is propertly detection line we us dialation
imageDialtion = cv2.dilate(imgCanny,kernel, iterations=1) # iterations is the thickness of the line
imageErorded = cv2.erode(imageDialtion,kernel,iterations=1) # erode the image oprisite of dialation

cv2.imshow("output", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dialation", imageDialtion)
cv2.imshow("Erorded", imageErorded)
cv2.waitKey(0)