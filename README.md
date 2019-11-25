# Texture Upscaling Pipeline

[![CodeFactor](https://www.codefactor.io/repository/github/boristsr/textureupscalingpipeline/badge)](https://www.codefactor.io/repository/github/boristsr/textureupscalingpipeline)

A framework to perform multiple processing passes on textures in order to upscale them.

## Requirements

* Python 3
* Pillow
* OpenCV
* ESRGAN (my branch with some changes to the commandline usage)
  * CUDA
  * Torch
  * TorchVision

## Setup

1. Clone the repo
2. Setup submodules
3. Install the requirements from requirements.txt
4. Install [CUDA](https://developer.nvidia.com/cuda-downloads)
5. Install [PyTorch and torchvision from the website](https://pytorch.org/get-started/locally/#start-locally)
6. Place desired [ESRGAN models from the authors page](https://github.com/xinntao/ESRGAN) into the directory
```
TextureUpscaler/ESRGAN/models
```
7. Configure settings.json


## Usage

All images need to be in a format that pillow can read. Preferably this is PNG so it can be lossless.

Configure settings.json with the search path and extensions to search for.

```json
{
  "searchPath": "D:/gamedata",
  "extensions": [".CACHE.PNG"]
}
```

Run the program

```batch
python UpscaleTextures.py
```

When the process has finished successfully all images will be saved alongside the originals with .HIRES.extension

## Customization

The purpose of this program is to tie together many processing stages that can be performed before and after the upscaling step. The implementation of each stage is defined in a few modules under TextureUpscaler directory, and the order of steps is defined in UpscaleTextures.py

### Adding a new processing step

The simplest way to add a new step is to add a custom function which works on a single image and can be passed to 

```python
run_processing_stage(invert_texture, images)
```

Any function passed to run_processing_stage should take 3 parameters:
inpath: the file to be processed
outpath: where the file should be saved once finished
workingImage: the WorkingImageData instance for this image which contains all information related to this image, including original path etc

When a function completes successfully it should return True so that run_processing_stage updates the paths correctly in the pipeline.

invert_texture is a simple example used for testing the pipeline and makes a good learning example. Below you can see it.

```python
from PIL import Image
import PIL.ImageOps

def invert_texture(inpath, outpath, workingImage):
    """Inverts the colors on the texture specified"""
    print("Inverting texture: " + inpath)
    image = Image.open(inpath)
    inverted_image = None
    try:
        inverted_image = PIL.ImageOps.invert(image)
    except:
        return False
    inverted_image.save(outpath)
    return True
```
