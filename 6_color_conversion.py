import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread('../ex/1_1_Image_Representation/images/car_green_screen.jpg')
plt.imshow(image)

lower_green = np.array([0,180,0])
upper_green = np.array([100,255,100])

mask = cv2.inRange(image, lower_green, upper_green)
masked_image = np.copy(image)

masked_image[mask!=0] = [0,0,0]
plt.imshow(masked_image)

hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

# f, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(20,10))
# ax1.set_title("hue")
# ax1.imshow(h, cmap='gray')
# ax2.set_title("saturation")
# ax2.imshow(h, cmap='gray')
# ax3.set_title("value")
# ax3.imshow(v, cmap='gray')

lower_green = np.array([70,0,0])
upper_green = np.array([180,255,255])
mask = cv2.inRange(hsv, lower_green, upper_green)

masked_image = np.copy(image)
masked_image[mask==0] = [0,0,0]
plt.imshow(masked_image)

