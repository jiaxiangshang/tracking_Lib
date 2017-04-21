from DataIOLib.dataIO_OTB import *
from DataIOLib.dataProcess_OTB import *
from MotionLib.slideWindow import *

def tracker_template_sildeWin_HOG(videopath, stFrame, edFrame, x, y, w, h):
    ApperanceModel = "HOG"

    tem_pro_lib = []
    video = loadVideo_byPath(videopath)
    rect_gt = rectBase([x, y, w, h], "Geom")
    #
    tem_pro_lib.append(tem_generateTem(video[0], rect_gt))


    res = []
    res.append(rect_gt.GetGeom_())
    #
    rect_last = rect_gt
    for img_ori_index in range(1, len(video)):
        img_ori = video[img_ori_index]
        #
        rect_sear = rect_last.GenerateScaleRect_(img_searchScale)
        rect_sear_net = rectBase([img_searchAddSize,
                                  img_searchAddSize,
                                  img_searchSize + img_searchAddSize,
                                  img_searchSize + img_searchAddSize], "Rect")
        img_sear_net = imgPro_sear(img_ori, rect_sear, rect_sear_net)

        rect_tem_net = tem_slideWin_HOG(tem_pro_lib, img_sear_net)

        rect_tem = rectPro_sear_Inverse(rect_tem_net, rect_sear_net, rect_sear)

        if img_ori_index % 50 == 0:
            tem_pro_lib.append(tem_generateTem(img_ori, rect_tem));

        rect_last = rect_tem
        res.append(rect_last.GetGeom_())
    return res[stFrame-1:edFrame]

def tem_generateTem(img_ori, rect_tem):
    rect_tem_net = rectBase([0,0,48,48], "Rect")
    return imgPro_sear(img_ori, rect_tem, rect_tem_net)

def tem_slideWin_HOG(tem_pro_lib, img_sear_net):
    rect_tar_net_list = []
    predict_score_min_list = []
    for img_template_pro in tem_pro_lib:
        # slide window
        heatmap = slideWindow(img_sear_net, img_template_pro)
        rect_tar_net_temTmp, predict_score_min = slideWindow_FindPredictMinScore_Rect(heatmap)

        rect_tar_net_list.append(rect_tar_net_temTmp)
        predict_score_min_list.append(predict_score_min)

    predict_score_min = min(predict_score_min_list)
    rect_tar_net_temTmp = rect_tar_net_list[predict_score_min_list.index(predict_score_min)]

    return rect_tar_net_temTmp;