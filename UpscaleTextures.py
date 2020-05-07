import json
import pprint
import copy

from TextureUpscaler.TextureProcessing import gather_textures, run_processing_stage, save_hires_image
from TextureUpscaler.UpscaleESRGAN import upscale_esrgan
from TextureUpscaler.DenoiseImages import denoise_texture_opencv
from TextureUpscaler.DownsampleImages import downsample
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

    images_src = copy.deepcopy(images)

    run_processing_stage(denoise_texture_opencv, images, settings) #1
    images_denoised = copy.deepcopy(images)
    images_esrgan = copy.deepcopy(images)
    images_ngx = copy.deepcopy(images)
    run_processing_stage(upscale_ngx, images_ngx, settings) #2
    run_processing_stage(upscale_ngx, images_src, settings) #3
    upscale_esrgan(images_esrgan, WorkingPath, settings) #4
    run_processing_stage(alpha_channel_upscale, images, settings) #5
    run_processing_stage(downsample, images, settings) #6
    run_processing_stage(save_hires_image, images, settings) #7

    print(images_denoised[0].lastPath)
    print(images_esrgan[0].lastPath)
    print(images_ngx[0].lastPath)

if __name__ == "__main__":
    run_texture_processing_pipeline()
