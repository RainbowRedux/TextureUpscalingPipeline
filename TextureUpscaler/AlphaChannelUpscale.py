from PIL import Image
import PIL.ImageOps
from shutil import move

def alpha_channel_upscale(inpath, outpath, workingImage, settings):
    """Opens the current working image as well as the original image, resizes (BICUBIC) the original image and copies the alpha channel"""
    originalImage = Image.open(workingImage.originalPath)
    if originalImage.mode != 'RGBA':
        # No alpha channel existed in the original image, so no need to do anything
        # Move the file to the outpath
        move(inpath, outpath)
        return True
        
    currentImage = Image.open(inpath)

    resizedImage = originalImage.resize(currentImage.size, Image.BICUBIC)

    # Extract the alpha channel
    alpha = resizedImage.split()[-1]
    currentImage.putalpha(alpha)

    currentImage.save(outpath, 'PNG')

    return True
    
    
