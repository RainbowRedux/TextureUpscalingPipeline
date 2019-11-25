import cv2

def denoise_texture_opencv(inpath, outpath, workingImage):
    """Runs a denoising process on the texture specified"""
    img = cv2.imread(inpath)
    dst = cv2.fastNlMeansDenoisingColored(src=img,dst=None,h=5,hColor=5,templateWindowSize=1,searchWindowSize=5)
    cv2.imwrite(outpath,dst)

    return True