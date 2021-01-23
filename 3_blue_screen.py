import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np
import cv2

image = cv2.imread('../ex/1_1_Image_Representation/images/pizza_bluescreen.jpg')

print('this image is: ', type(image), ' with dimensions: ', image.shape)
image_copy = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

f, (ax1, ax2) = plt.subplots(1,2,figsize=(20,10))
ax1.imshow(image)
ax2.imshow(image_copy)

lower_blue = np.array([0,0,200])
upper_blue = np.array([250,250,255])

mask = cv2.inRange(image_copy, lower_blue, upper_blue)
plt.imshow(mask, cmap='gray')

masked_image = np.copy(image_copy)
masked_image[mask!=0] = [0,0,0]
plt.imshow(masked_image)

background_image = cv2.imread('../ex/1_1_Image_Representation/images/space_background.jpg')
background_image = cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB)

crop_background = background_image[0:masked_image.shape[0], 0:masked_image.shape[1]]
crop_background[mask == 0] = [0,0,0]

plt.imshow(crop_background + masked_image)