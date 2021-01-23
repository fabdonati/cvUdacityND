import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2

image = cv2.imread('../ex/1_1_Image_Representation/images/wa_state_highway.jpg')

plt.imshow(image)

r = image[:,:,0]
g = image[:,:,1]
b = image[:,:,2]

f, (ax1, ax2, ax3) = plt.subplots(1,3,figsize=(20,10))
ax1.set_title('R channel')
ax1.imshow(r, cmap='gray')
ax2.set_title('G channel')
ax2.imshow(g, cmap='gray')
ax3.set_title('B channel')
ax3.imshow(b, cmap='gray')
