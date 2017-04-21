
import cv2
import numpy as np
import matplotlib.pyplot as plt

def opencvHog(img):
    # gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # hog_h = cv2.HOGDescriptor()
    # hist_template = hog_h.compute(img)

    winSize = (16, 16)
    blockSize = (8, 8)
    blockStride = (4, 4)
    cellSize = (4, 4)
    nbins = 9
    derivAperture = 1
    winSigma = 4.
    histogramNormType = 0
    L2HysThreshold = 2.0000000000000001e-01
    gammaCorrection = 0
    nlevels = 64
    hog_h = cv2.HOGDescriptor(winSize, blockSize, blockStride, cellSize, nbins, derivAperture, winSigma,
                              histogramNormType, L2HysThreshold, gammaCorrection, nlevels)

    winStride = (8, 8)
    padding = (8, 8)
    locations = ((10, 20),)
    hist_template = hog_h.compute(img, winStride, padding, locations)

    #plt.bar(np.arange(hist_template.shape[0]), hist_template, 1, 1)
    #plt.show()

    return hist_template
