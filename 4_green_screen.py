import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import cv2

image = cv2.imread('../ex/1_1_Image_Representation/images/car_green_screen.jpg')
plt.imshow(image)

lower_green = np.array([0,200,0])
upper_green = np.array([250,255,250])

mask = cv2.inRange(image, lower_green, upper_green)
image[mask!=0] = [0,0,0]
plt.imshow(mask, cmap='gray')

background_image = cv2.imread('../ex/1_1_Image_Representation/images/sky.jpg')
background_image = background_image[0:mask.shape[0], 0:mask.shape[1]]
background_image[mask==0]=[0,0,0]

plt.imshow(background_image+image)

