from PIL import Image
from shutil import move

def downsample_half(inpath, outpath, workingImage, settings):
    """Downsamples the current texture by half"""
    currentImage = Image.open(inpath)

    newDimensions = [int(x / 2) for x in currentImage.size]
    newDimensions = tuple(newDimensions)

    resizedImage = currentImage.resize(newDimensions, Image.BICUBIC)
    resizedImage.save(outpath, 'PNG')

    return True
