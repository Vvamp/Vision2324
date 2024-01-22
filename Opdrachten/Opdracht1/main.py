from Parts.opdracht_a import opdracht_a
from Parts.opdracht_b import opdracht_b
from skimage.viewer import ImageViewer
from matplotlib import pyplot as plt

if __name__ == "__main__":    
    print("[ Vision 23/24 by Vincent van Setten (Vvamp) ]")
    opdracht_a_result = opdracht_a("Images/kleurfoto2.jpg")
    print("> Now Showing Opdracht 1A result")
    ImageViewer(opdracht_a_result).show()

    opdracht_b_result_1, opdracht_b_result_2 = opdracht_b("Images/kleurfoto2.jpg")
    print("> Now Showing Opdracht 1B results")
    print(">> Showing opdracht 1B with original image data")
    opdracht_b_result_1.show()
    print(">> Showing opdracht 1B with image data after opdracht 1A")
    opdracht_b_result_2.show()
    plt.show()