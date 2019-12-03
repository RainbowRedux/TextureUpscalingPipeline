import cv2

def denoise_texture_opencv(inpath, outpath, workingImage, settings):
    """Runs a denoising process on the texture specified"""
    CV_Denoise_templateWindowSize = settings["CV_Denoise_templateWindowSize"]
    CV_Denoise_searchWindowSize = settings["CV_Denoise_searchWindowSize"]
    CV_Denoise_h = settings["CV_Denoise_h"]
    CV_Denoise_hColor = settings["CV_Denoise_hColor"]

    img = cv2.imread(inpath)
    dst = cv2.fastNlMeansDenoisingColored(src=img,dst=None,h=CV_Denoise_h,hColor=CV_Denoise_hColor,templateWindowSize=CV_Denoise_templateWindowSize,searchWindowSize=CV_Denoise_searchWindowSize)
    cv2.imwrite(outpath,dst)

    return True
