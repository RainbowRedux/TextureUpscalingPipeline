import subprocess
import os.path

def upscale_ngx(inpath, outpath, workingImage, settings):
    """Runs a denoising process on the texture specified"""

    ISRExe = settings["NGX_ISR_Exe"]
    ISRScalingFactor = settings["NGX_ISR_ScalingFactor"]
    
    cmd = [ISRExe, "--input", inpath, "--output", outpath, "--factor", str(ISRScalingFactor)]
    proc = subprocess.call(cmd)

    success = os.path.isfile(outpath)

    if not success:
        print("The image failed to generate at " + outpath)

    return success
