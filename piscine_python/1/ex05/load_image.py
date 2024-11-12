import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


def ft_load(path: str) -> np.ndarray:  # (you can return to the desired format)
    '''ft_load take the path to a .jpg or .jpeg file, load it and print it'''
    # load the image using matplotlib
    try:
        img = mpimg.imread(path)
        # display the image using plt
        plt.imshow(img)
        plt.show()
        # print and return the image as a numpy array
        print(f"The shape of image is : {img.shape}")
        # print(img[0])  # First row
        # print("...")
        # print(img[-1])  # Last row
        return img
    except Exception as e:
        print(f"error load image: {e}")
        exit()

# image_array = ft_load("../landscape.jpg")
