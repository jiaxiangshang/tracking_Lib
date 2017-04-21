
import cv2
import numpy as np
import glob, os


from global_Var import *

def loadVideo_byName(videoName):
    video = []
    img_folder_path = dataPath + videoName + "/img/"
    for file in glob.glob(img_folder_path + "*.jpg"):
        img = cv2.imread(file)
        video.append(img)
    os.chdir("./")
    return video

def loadVideo_byPath(videopath):
    video = []
    img_folder_path = videopath
    for file in glob.glob(img_folder_path + "*.jpg"):
        img = cv2.imread(file)
        video.append(img)
    os.chdir("./")
    return video

def loadVideoFrame(videoName, frame):
    os.chdir(dataPath + videoName)
    file = glob.glob("*.jpg")

    img = cv2.imread(file[frame])
    return img

def loadVideoGt(videoName):
    # read
    gt_file_path = dataPath + videoName + "/" + gtFileName
    gt = np.loadtxt(gt_file_path,delimiter=",")
    return gt
