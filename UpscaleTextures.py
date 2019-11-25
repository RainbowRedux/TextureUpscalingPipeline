import json
import pprint

from TextureUpscaler.TextureProcessing import *
from TextureUpscaler.UpscaleESRGAN import *

def load_settings():
    settingsFile = open("settings.json")
    settings = json.load(settingsFile)
    settingsFile.close()
    return settings

def print_settings(settings):
    pprint.pprint(settings)

def run_texture_processing_pipeline():
    settings = load_settings()
    print_settings(settings)

    SourcePath = settings["SourcePath"]
    WorkingPath = settings["WorkingPath"]
    ExtensionsToFind = settings["ExtensionsToFind"]
    ESRGANModel = settings["ESRGANModel"]

    images = gather_textures(SourcePath, WorkingPath, ExtensionsToFind)
    print("Number of images gathered: " + str(len(images)))

    run_processing_stage(denoise_texture, images)
    upscale_esrgan(images, WorkingPath, ESRGANModel)
    run_processing_stage(save_hires_image, images)

if __name__ == "__main__":
    run_texture_processing_pipeline()
