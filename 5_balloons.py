import cv2
import matplotlib.pyplot as plt
import matplotlib.image as img
import numpy as np

image = cv2.imread('../ex/1_1_Image_Representation/images/water_balloons.jpg')
image_copy = np.copy(image)

rgb = cv2.cvtColor(image_copy, cv2.COLOR_BGR2RGB)
r = image_copy[:,:,0]
g = image_copy[:,:,1]
b = image_copy[:,:,2]

f, ([ax1, ax2, ax3],[ax4, ax5, ax6]) = plt.subplots(2,3,figsize=(20,10))
ax1.imshow(r, cmap='gray')
ax2.imshow(g, cmap='gray')
ax3.imshow(b, cmap='gray')
ax1.set_title('red')
ax2.set_title('green')
ax3.set_title('blue')

hsv = cv2.cvtColor(image_copy, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]

ax4.imshow(h, cmap='gray')
ax5.imshow(s, cmap='gray')
ax6.imshow(v, cmap='gray')
ax4.set_title('hue')
ax5.set_title('saturation')
ax6.set_title('value')

lower_pink = np.array([180,0,100])
upper_pink = np.array([255,255,230])

lower_hue = np.array([160,0,0])
upper_hue = np.array([180,255,255])

mask_rgb = cv2.inRange(rgb, lower_pink, upper_pink)
mask_hue = cv2.inRange(hsv, lower_hue, upper_hue)

masked_image_rgb = np.copy(rgb)
masked_image_hue = np.copy(hsv)
masked_image_rgb[mask_rgb==0] = [0,0,0]
masked_image_hue[mask_hue==0] = [0,0,0]

f, (ax1, ax2) = plt.subplots(1,2,figsize=(20,10))
ax1.imshow(masked_image_rgb)
ax2.imshow(masked_image_hue)