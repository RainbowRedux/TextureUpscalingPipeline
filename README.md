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

## Customisation

The purpose of this program is to tie together many processing stages that can be performed before and after the upscaling step. The implementation of each stage is defined in a few modules, and the order of steps is defined in UpscaleTextures.py

### Adding a new processing step

TODO
