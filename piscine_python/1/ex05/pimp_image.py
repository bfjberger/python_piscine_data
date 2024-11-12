import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.ndarray:  # your code here
    '''ft_invert Invert the color of ndarray'''
    # the inversion will apply to each color channel separately.
    array = 255 - array
    plt.imshow(array)
    plt.show()
    print(array.shape)
    print(array)


def ft_red(array) -> np.ndarray:  # your code here
    '''apply a red color filter to image'''
    # Create a copy of the image array for safty reason.
    # we can go back to the original in case
    red_filtered = array.copy()
    # Zero out the blue and green channel
    red_filtered[:, :, 1] = 0
    red_filtered[:, :, 2] = 0
    plt.imshow(red_filtered)
    plt.show()
    print(red_filtered.shape)
    print(red_filtered)


def ft_green(array) -> np.ndarray:  # your code here
    '''apply a green color filter to image'''
    # Create a copy of the image array
    red_filtered = array.copy()
    red_filtered[:, :, 0] = 0
    red_filtered[:, :, 2] = 0
    plt.imshow(red_filtered)
    plt.show()
    print(red_filtered.shape)
    print(red_filtered)


def ft_blue(array) -> np.ndarray:  # your code here
    '''apply a blue color filter to image'''
    # Create a copy of the image array
    red_filtered = array.copy()
    red_filtered[:, :, 0] = 0
    red_filtered[:, :, 1] = 0
    plt.imshow(red_filtered)
    plt.show()
    print(red_filtered.shape)
    print(red_filtered)


def ft_grey(array) -> np.ndarray:  # your code here
    '''apply a grey color filter to image'''
    grey_filtered = array.copy()
    # Convert each pixel's color channels to the average of the three channels
    grey_filtered[:, :, 0] = grey_filtered[:, :, 1] = grey_filtered[:, :, 2] =\
        np.mean(grey_filtered[:, :, :3], axis=2)  # Average the RGB values
    plt.imshow(grey_filtered)
    plt.show()
    print(grey_filtered.shape)
    print(grey_filtered)
