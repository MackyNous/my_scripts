'''Extract the RED portion of an image'''

#import the necessary packages
import cv2
import numpy as np

path=raw_input("Enter the path\n") # Enter the path of the image
img=cv2.imread(path)
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # Convert the image from BGR to HSV

# lower mask (0-10)
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

# upper mask (170-180)
lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

# join the masks
mask = mask0+mask1

# set my output img to zero(BLACK) everywhere except the mask
output_img = img.copy()
output_img[np.where(mask==0)] = 0
cv2.imshow("original", img)
cv2.imshow('output',output_img)
if (cv2.waitKey(0) & 0xFF == ord('q')):
	cv2.destroyAllWindows()
