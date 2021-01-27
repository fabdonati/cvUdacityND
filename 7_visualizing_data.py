import cv2
import helpers
import numpy as np
import matplotlib.pyplot as plt

image_dir_training = "../ex/1_1_Image_Representation/day_night_images/training/"
image_dir_test = "../ex/1_1_Image_Representation/day_night_images/test/"

IMAGE_LIST = helpers.load_dataset(image_dir_training)
image_index = 0
selected_image = IMAGE_LIST[image_index][0]
selected_label = IMAGE_LIST[image_index][1]

print('dimensions are: ', selected_image.shape)
print('label is: ', selected_label)
plt.imshow(selected_image)

for im in IMAGE_LIST:
    if im[1] == 'night':
        break
plt.imshow(im[0])

