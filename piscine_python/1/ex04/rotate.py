from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def zoom(img_array: np.ndarray, X: int, Y: int) -> np.ndarray:
    """Zoom into the center of the image by a zoom factor."""
    # notice that zoom is already cutting a square of 400*400 in animal
    new_centre_x, new_center_y = 450, 100
    # Slice the image
    zoomed_image = img_array[new_center_y: new_center_y + Y,
                             new_centre_x:new_centre_x + X]
    return zoomed_image


def rgb2gray(img_array: np.ndarray) -> np.ndarray:
    """Convert an RGB image to grayscale."""
    if len(img_array.shape) == 3 and img_array.shape[2] == 3:
        # Using the standard weighted conversion to grayscale
        # apply the formula grey = R*0.2989 + G*0.5870 + B*0.1140
        # np.dot apply this formula to the list
        return np.dot(img_array[..., :3], [0.2989, 0.5870, 0.1140])
    else:
        return img_array  # Return unchanged if already grayscale


def ft_transpose(img: np.ndarray) -> np.ndarray:
    """
    Transpose an image (swap rows with columns).
    """
    # If the image is grayscale (2D)
    if len(img.shape) == 2:
        return img.T  # Simply transpose the 2D array

    # If the image is color (3D)
    h, w, channels = img.shape
    transposed_img = np.zeros((w, h, channels), dtype=img.dtype)

    # Swap rows and columns for each channel
    for i in range(h):
        for j in range(w):
            transposed_img[j, i] = img[i, j]

    return transposed_img


def main():
    ''' main function '''
    img = ft_load("../animal.jpeg")
    print(img)
    # Get and print the pixel value at (400, 400)
    zoomed_img = zoom(img, 400, 400)
    grey_img = rgb2gray(zoomed_img)
    plt.imshow(grey_img, cmap=plt.cm.gray)
    plt.show()
    print("New shape after slicing :", grey_img)
    print(grey_img)
    transpose_img = ft_transpose(grey_img)
    plt.imshow(transpose_img, cmap=plt.cm.gray)
    plt.show()
    print("New shape after new transpose :", transpose_img)
    print(transpose_img)


if __name__ == "__main__":
    main()
