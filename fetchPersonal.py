import os
from imageUtils import *
from PIL import Image

dirname = os.path.dirname(__file__)

def fetchCategory(category, targetDims, destination):
    folder = f"{dirname}/Data/Personal/{category.lower()}"

    if not os.path.exists(destination):
        os.makedirs(destination)

    if os.path.exists(folder):
        for file in os.listdir(folder):
            img = Image.open(f"{folder}/{file}")
            resizedImage = resizeImage(img, targetDims)
            resizedImage.save(f"{destination}/Personal-{file}")
            img.close()

        print(f"DONE! Processed personal images of {category}.")
    else:
        print(f"No personal images of {category}.")

