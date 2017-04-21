
import cv2
import numpy as np

from global_Var import *
from GeomLib.rectDefine import *

def Generate_warpMtx(pt_ori, pt_tar):
    pts_search = np.float32(pt_ori)
    pts_search_add = np.float32(pt_tar)

    Mtx = cv2.getAffineTransform(pts_search, pts_search_add)

    return Mtx

def imgPro_sear(img_ori, rect_ori, rect_tar):
    pt_ori = [rect_ori.GetLeftTop_Int_(), rect_ori.GetRightBottom_Int_(), rect_ori.GetRightTop_Int_()]
    pt_tar = [rect_tar.GetLeftTop_Int_(), rect_tar.GetRightBottom_Int_(), rect_tar.GetRightTop_Int_()]

    Mtx = Generate_warpMtx(pt_ori, pt_tar)

    img_search_re_added = cv2.warpAffine(img_ori, Mtx, (img_searchAddedSize, img_searchAddedSize))

    return img_search_re_added

def rectPro_sear_Inverse(rect, rect_ori, rect_tar):
    pt_ori = [rect_ori.GetLeftTop_Int_(), rect_ori.GetRightBottom_Int_(), rect_ori.GetRightTop_Int_()]
    pt_tar = [rect_tar.GetLeftTop_Int_(), rect_tar.GetRightBottom_Int_(), rect_tar.GetRightTop_Int_()]

    Mtx = Generate_warpMtx(pt_ori, pt_tar)
    rect.GetRect_()
    rect_Mtx = np.ones((3,1))
    rect_Mtx[0,0] = rect.left
    rect_Mtx[1,0] = rect.top
    rect_lt = np.dot(Mtx, rect_Mtx)
    rect_lt = rect_lt.tolist()
    rect_Mtx[0,0] = rect.right
    rect_Mtx[1,0] = rect.bottom
    rect_rb = np.dot(Mtx, rect_Mtx)
    rect_rb = rect_rb.tolist()

    return rectBase([rect_lt[0][0],rect_lt[1][0],rect_rb[0][0],rect_rb[1][0]],"Rect")