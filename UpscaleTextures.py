import json
import pprint

from TextureUpscaler.TextureProcessing import gather_textures, run_processing_stage, save_hires_image
from TextureUpscaler.UpscaleESRGAN import upscale_esrgan
from TextureUpscaler.DenoiseImages import denoise_texture_opencv
from TextureUpscaler.AlphaChannelUpscale import alpha_channel_upscale

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

    run_processing_stage(denoise_texture_opencv, images)
    upscale_esrgan(images, WorkingPath, ESRGANModel)
    run_processing_stage(alpha_channel_upscale, images)
    run_processing_stage(save_hires_image, images)

if __name__ == "__main__":
    run_texture_processing_pipeline()
