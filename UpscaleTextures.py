import json
import pprint

from TextureUpscaler.TextureProcessing import gather_textures, run_processing_stage, save_hires_image
from TextureUpscaler.UpscaleESRGAN import upscale_esrgan
from TextureUpscaler.DenoiseImages import denoise_texture_opencv
from TextureUpscaler.DownsampleImages import downsample_half
from TextureUpscaler.AlphaChannelUpscale import alpha_channel_upscale
from TextureUpscaler.UpscaleNGX import upscale_ngx

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

    images = gather_textures(SourcePath, WorkingPath, ExtensionsToFind)
    print("Number of images gathered: " + str(len(images)))

    run_processing_stage(denoise_texture_opencv, images, settings)
    run_processing_stage(upscale_ngx, images, settings)
    #upscale_esrgan(images, WorkingPath, settings)
    run_processing_stage(alpha_channel_upscale, images, settings)
    run_processing_stage(downsample_half, images, settings)
    run_processing_stage(save_hires_image, images, settings)

if __name__ == "__main__":
    run_texture_processing_pipeline()
