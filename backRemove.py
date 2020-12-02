import matplotlib.pyplot as plt
import numpy as np
import cv2


img = cv2.imread('cat.jpg')
print('this image is:', type(img),
      'with dimension:', img.shape)
image_copy = np.copy(img)
image_copy = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
cv2.imshow(" ", image_copy)
cv2.waitKey(0)

lower_blue = np.array([0, 0, 200])

upper_blue = np.array([250, 250, 255])

# Create Mask
mask = cv2.inRange(image_copy, lower_blue, upper_blue)
cv2.imshow("mask", mask)
cv2.waitKey(0)
height, width = img.shape[:2]
masked_image = np.copy(image_copy)
masked_image[mask != 0] = [0, 0, 0]
cv2.imshow(" maskedImg", masked_image)
cv2.waitKey(0)

background_image = cv2.imread('sea.jpg')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)
crop_background = background_image[0:height, 0:width]
background_image_copy = np.copy(crop_background)
background_image_copy[mask == 0] = [0, 0, 0]
cv2.imshow("maskedBack", background_image_copy)
cv2.waitKey(0)

newImage = background_image_copy + masked_image
cv2.imshow("Modified", newImage)
cv2.waitKey(0)

