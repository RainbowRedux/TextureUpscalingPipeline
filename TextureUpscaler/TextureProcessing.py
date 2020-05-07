"""
Utilities to run various processing and upscaling processes on images
"""
import os
from os import path
from shutil import copyfile

STEP_COUNT = 0

def tick_step_count():
    global STEP_COUNT
    STEP_COUNT += 1

def get_step_count():
    return STEP_COUNT

class WorkingImageData:
    """Information associated with an image that is running through the processing pipeline"""
    originalPath = ""
    ID = 0
    workingPath = ""
    workingFilename = ""
    filename = ""
    lastPath = ""

    def prepare_next_step(self):
        """This function prepares a new filename based on the number of steps"""
        self.stepNumber = get_step_count()
        self.workingFilename = str(self.ID) + "_" + str(self.stepNumber) + ".PNG"
        self.workingPath = path.join(self.workingPathBase, self.workingFilename)

    def assign_file(self, filepath, ID, workingPath):
        self.originalPath = path.normpath(filepath)
        self.ID = ID
        self.stepNumber = -1
        self.workingPathBase = workingPath
        self.filename = path.basename(self.originalPath)
        self.lastPath = self.originalPath

def gather_files_in_path(extension, folder):
    """Walks a folder and it's sub directories and finds all files with matching extension, case-insensitive"""
    filesToProcess = []
    for root, dirs, files in os.walk(folder, topdown=True):
        for name in files:
            if name.upper().endswith(extension.upper()):
                filesToProcess.append(path.join(root, name))
        for name in dirs:
            pass
    return filesToProcess

def gather_textures(source_path, workingPath, extensionsToFind):
    """
    Finds all textures and returns them in the workingImage data structure
    """
    filepaths = []
    for ext in extensionsToFind:
        filepaths.extend(gather_files_in_path(ext, source_path))

    print(len(filepaths))

    workingImages = []
    lastID = 0
    for filepath in filepaths:
        procImage = WorkingImageData()
        procImage.assign_file(filepath, lastID, workingPath)
        lastID += 1
        workingImages.append(procImage)

    return workingImages

def run_processing_stage(processingFunc, workingImages, settings=None):
    """Runs the function passed to processingFunc on each working image."""
    tick_step_count()
    for workingImage in workingImages:
        print("Processing: " + str(workingImage.ID))
        workingImage.prepare_next_step()
        result = processingFunc(workingImage.lastPath, workingImage.workingPath, workingImage, settings)
        if result:
            workingImage.lastPath = workingImage.workingPath

def invert_texture(inpath, outpath, workingImage, settings):
    """Inverts the colors on the texture specified"""
    print("Inverting texture: " + inpath)
    from PIL import Image
    import PIL.ImageOps
    image = Image.open(inpath)
    inverted_image = None
    try:
        inverted_image = PIL.ImageOps.invert(image)
    except IOError:
        return False
    inverted_image.save(outpath)
    return True

def save_hires_image(inpath, outpath, workingImage, settings):
    """Takes a working image and saves it in the original place with .HIRES before the original extension"""
    src = inpath
    ext = path.splitext(workingImage.originalPath)[1]
    dst = workingImage.originalPath[:-len(ext)] + ".HIRES" + ext
    print("source: " + src)
    print("\tdest: " + dst)
    copyfile(src, dst)

    return True
