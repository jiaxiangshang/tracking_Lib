import cv2
import sys

from DataIOLib.dataIO_OTB import *
from DataIOLib.dataProcess_OTB import *
from tracker_template_sildeWin_HOG.tracker_template_sildeWin_HOG import *

import sys
sys.path.append(otbPath)
sys.path.append(otbPath + "scripts\\butil")
print(sys.path)
from seq_config import *

videoName_list = butil.get_seq_names(LOADSEQS_OTB)
videoInfo_list = butil.load_seq_configs(videoName_list)


for idx in range(len(videoName_list)):
    subSeqs, subAnno = butil.get_sub_seqs(videoInfo_list[idx], 20.0, EVALTYPE)

    videoPath = dataPath + videoName_list[idx] + "/img/"
    video = loadVideo_byName(videoName_list[idx])
    video_gt = loadVideoGt(videoName_list[idx])

    tic = time.clock()
    res = tracker_template_sildeWin_HOG(videoPath, 1, len(video), video_gt[0][0], video_gt[0][1], video_gt[0][2], video_gt[0][3])
    duration = time.clock() - tic
    print(videoName_list[idx], duration)

    for frame in range(0, len(video)):
        img = video[frame]
        rect = rectBase(res[frame], "Geom")
        cv2.rectangle(img, rect.GetLeftTop_Int_(), rect.GetRightBottom_Int_(), (255, 0, 0), 2)
        cv2.imshow('frame', img)
        cv2.waitKey(100)
    cv2.destroyAllWindows()
