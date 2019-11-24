import json

from TextureUpscaler.TextureProcessing import *
from TextureUpscaler.UpscaleESRGAN import *

settingsFile = open("settings.json")
settings = json.load(settingsFile)
settingsFile.close()

SourcePath = settings["SourcePath"]
WorkingPath = settings["WorkingPath"]
ExtensionsToFind = settings["ExtensionsToFind"]
ESRGANModel = settings["ESRGANModel"]

if __name__ == "__main__":
    images = gather_textures(SourcePath, WorkingPath, ExtensionsToFind)
    print(len(images))
    run_processing_stage(denoise_texture, images)
    upscale_esrgan(images, WorkingPath, ESRGANModel)
    run_processing_stage(save_hires_image, images)
