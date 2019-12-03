"""
Parameters and utility functions to run ESRGAN on images within WorkingImageData's
"""

import subprocess
from os import path
from shutil import copyfile

ESRGANPath = "TextureUpscaler/ESRGAN/"
ESRGANScript = path.join(ESRGANPath, "test.py")
ESRGANModelDefault = "RRDB_ESRGAN_x4.pth"
ESRGANSrcPath = path.join(ESRGANPath, "LR")
ESRGANDstPath = path.join(ESRGANPath, "results")

def upscale_esrgan(workingImages, workingPath, settings):
    for currImage in workingImages:
        src = currImage.lastPath
        dst = path.join(ESRGANSrcPath, currImage.workingFilename)
        copyfile(src, dst)

    ESRGANModel = settings["ESRGANModel"]

    ESRGANCommand = ["python", ESRGANScript, ESRGANModel]
    proc = subprocess.call(ESRGANCommand)

    for currImage in workingImages:
        destFilename = str(currImage.ID) + "_rlt.png"
        src = path.join(ESRGANDstPath, destFilename)
        dst = path.join(workingPath, currImage.workingFilename)
        copyfile(src, dst)
        currImage.lastPath = dst
        