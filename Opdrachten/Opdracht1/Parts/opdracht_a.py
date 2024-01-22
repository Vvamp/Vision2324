from skimage import data, io
from skimage.color import rgb2hsv, hsv2rgb
import numpy as np

def deg_to_percentage(deg : int) -> float:
    """Converts a degree to a percentage (between 0 and 1)

    Args:
        deg (int): The degrees(0-360)

    Returns:
        float: A value between 0 and 1 corresponding to the degree
    """
    return deg / 360

def greyscale(image : np.ndarray, range : tuple) -> np.ndarray:
    """Convert an image to greyscale, except for a given color range (based on HSV values)

    Args:
        image (np.ndarray): The image in RGB format
        range (tuple): A min and max value of the color range to exclude from greyscale (in degrees)

    Returns:
        np.ndarray: The greyscaled image(in RGB format)
    """
    # Convert to HSV to check color ranges
    image_data_hsv = rgb2hsv(image)
    
    # Make outside the range black and white
    for col in image_data_hsv:
        for row in col:
            if row[0] < deg_to_percentage(range[0]) or row[0] > deg_to_percentage(range[1]):
                row[1] = 0 # Set saturation to 0 to make the pixel black/white

    # Return RGB image
    return hsv2rgb(image_data_hsv)

def opdracht_a(image_path : str):
    """Opdracht A (Part of of assignment 1), greyscaling an image except for a certain color range
    """
    image = io.imread(image_path)
    greyscaled_image = greyscale(image, (160,240)) # Grab blue as range(hsv between 160 degrees and 240 degrees Hue)
    return greyscaled_image

