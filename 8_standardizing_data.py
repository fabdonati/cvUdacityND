import cv2
import matplotlib.pyplot as plt
import numpy as np

standard_image =np.zeros(shape=(600,1100))
image_dir_training = "../ex/1_1_Image_Representation/day_night_images/training/"
image_dir_test = "../ex/1_1_Image_Representation/day_night_images/test/"

IMAGE_LIST = helpers.load_dataset(image_dir_training)
image_index = 0
selected_image = IMAGE_LIST[image_index][0]
selected_label = IMAGE_LIST[image_index][1]

print('dimensions are: ', selected_image.shape)
print('label is: ', selected_label)
plt.imshow(selected_image)

def standardize(ref_image_shape, image_list):
    standard_list = []
    for item in image_list:
        image = item[0]
        label = item[1]

        standardized_image = standardize_input(ref_image_shape, image)
        binary_label = encode(label)

        standard_list.append(standardized_image, binary_label)
    return standard_list

def standardize_input(ref_image_shape, image):
    # swap tuple (height, width)
    ref_image_shape = (ref_image_shape[1], ref_image_shape[0])
    image = cv2.resize(image, ref_image_shape)
    return image         

def encode(label):
    numerical_val = 0
    if label == 'day':
        numerical_val = 1
    return numerical_val
