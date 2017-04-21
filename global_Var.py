import os

proPath = "D:\\Program\\Tracking\\Project\\"
cwdPath = proPath + "tracking_Staple_cvpr16\\"
otbPath = proPath + "tracker_benchmark_OTB_Python\\"

############################################################ OTB
# dataIO
dataPath = "../../Data/OTB_Python/"
# dataIO OTB
gtFileName = "groundtruth_rect.txt"

LOADSEQS_OTB = "TB50"
RESULTPATH = "./"
SAVE_IMAGE = False
EVALTYPE = "OPE"


############################################################ tracker_template_sildeWin_HOG
img_templateSize = 48
img_templateScale = 2.5
img_searchSize = img_templateSize * img_templateScale
img_heatmapSize = 31

for i in range(img_heatmapSize):
    if (img_searchSize + i - img_templateSize) % 31 == 0:
        img_searchStrideSize = (img_searchSize + i - img_templateSize) % 31
        img_searchAddSize = i / 2
        img_searchAddedSize = img_searchSize + i
        break


# tracker
ApperanceModel = "HOG"
#ApperanceModel = "HOG"