
from global_Var import *
from FeatureLib.opencvHog import *
from GeomLib.rectDefine import *

def slideWindow(img_search, img_template):
    heatmap = np.zeros((img_heatmapSize, img_heatmapSize))

    if ApperanceModel == "HOG":
        hist_template = opencvHog(img_template)
    else:
        hist_template = opencvHog(img_template)

    for i in range(0,img_heatmapSize):
        for j in range(0, img_heatmapSize):
            left = j * img_searchStrideSize
            right = j * img_searchStrideSize + img_templateSize

            top = i * img_searchStrideSize
            bottom = i * img_searchStrideSize + img_templateSize

            img_search_patch = img_search[top:bottom,left:right]

            if ApperanceModel == "HOG":
                hist_patch = opencvHog(img_search_patch)
            else:
                hist_patch = opencvHog(img_search_patch)

            disL2 = np.sqrt(np.sum(np.square(hist_template - hist_patch)))

            heatmap[i,j] = disL2

    return heatmap


def slideWindow_FindPredictMinScore_Rect(heatmap):

    heatmap_min = heatmap.min()
    # find min pos
    for i in range(0, heatmap.shape[0]):
        for j in range(0, heatmap.shape[1]):
            if heatmap[i, j] == heatmap_min:
                center_x = j
                center_y = i

                heatmap[i, j] = heatmap.max()
                break

    return rectBase([center_x * 2, center_y* 2, img_templateSize, img_templateSize], "Geom"), heatmap_min