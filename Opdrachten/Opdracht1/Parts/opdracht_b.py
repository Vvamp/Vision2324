from skimage import data, io
from skimage.viewer import ImageViewer
from skimage.color import rgb2hsv, hsv2rgb
from matplotlib import pyplot as plt
import numpy as np
from Parts.opdracht_a import opdracht_a

def create_histogram_from_image(image : np.ndarray, title:str="Image Hue Histogram" ):
    """Generate a histogram based on image RGB data

    Args:
        image (np.ndarray): RGB Data for the image
        title (str): Optional title of the histogram
    """
    # Convert to HSV to check color ranges
    image_data_hsv = rgb2hsv(image)
    hues=[]
    
    # Make outside the range black and white
    for col in image_data_hsv:
        for row in col:
            hues.append(row[0]*360)
            
    # Creating the plot
    fig, ax = plt.subplots()
    ax.hist(hues, bins=36, color='red', edgecolor='black', range=[0,360])
    
    # Adding labels and title
    ax.set_xlabel('Hue Value')
    ax.set_ylabel('Frequency')
    ax.set_title(title)
    
    return fig


def opdracht_b(image_path : str):
    # Generate random data for the histogram
    image = io.imread(image_path)
    original_histogram = create_histogram_from_image(image, "Hue Histogram before edit")
    image_after_a = opdracht_a(image_path)
    histogram_after_edit = create_histogram_from_image(image_after_a, "Hue Histogram after edit")
    return original_histogram, histogram_after_edit