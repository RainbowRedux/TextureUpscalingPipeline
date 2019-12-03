from PIL import Image
from shutil import move

def downsample(inpath, outpath, workingImage, settings):
    """Downsamples the current texture by half"""

    Downsample_Factor = settings["Downsample_Factor"]

    currentImage = Image.open(inpath)

    newDimensions = [int(x / Downsample_Factor) for x in currentImage.size]
    newDimensions = tuple(newDimensions)

    resizedImage = currentImage.resize(newDimensions, Image.BICUBIC)
    resizedImage.save(outpath, 'PNG')

    return True
