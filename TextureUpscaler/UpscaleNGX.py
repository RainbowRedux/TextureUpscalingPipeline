import subprocess

def upscale_ngx(inpath, outpath, workingImage, settings):
    """Runs a denoising process on the texture specified"""
    workingDir = ""
    if settings["WorkingPath"]:
        workingImage = settings["WorkingPath"]

    ISRExe = settings["NGX_ISR_Exe"]
    ISRScalingFactor = settings["NGX_ISR_ScalingFactor"]
    
    cmd = [ISRExe, "--input", inpath, "--output", outpath, "--factor", str(ISRScalingFactor), "--wd", workingDir]
    proc = subprocess.call(cmd)

    return True
