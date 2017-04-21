
class rectBase:
    # param
    # left top right bottom width height
    def __init__(self, param, mode):
        if mode == "Rect":
            self.left = param[0]
            self.top = param[1]

            self.right = param[2]
            self.bottom = param[3]

            self.width = self.right - self.left
            self.height = self.bottom - self.top
        elif mode == "Geom":
            self.left = param[0]
            self.top = param[1]

            self.width = param[2]
            self.height = param[3]

            self.right = self.left + self.width
            self.bottom = self.top + self.height
        elif mode == "Center":
            self.left = param[0] - param[2] / 2
            self.top = param[1] - param[3] / 2

            self.width = param[2]
            self.height = param[3]

            self.right = self.left + self.width
            self.bottom = self.top + self.height
        else:
            self.left = 0.0
            self.top = 0.0

            self.right = 0.0
            self.bottom = 0.0

            self.width = 0.0
            self.height = 0.0

        self.center_x = self.left + self.width / 2
        self.center_y = self.top + self.height / 2

    def GetLeftTop_Int_(self):
        return int(self.left), int(self.top)

    def GetRightTop_Int_(self):
        return int(self.right), int(self.top)

    def GetRightBottom_Int_(self):
        return int(self.right), int(self.bottom)

    def GetWidthHeight_Int_(self):
        return int(self.width), int(self.height)

    def GetCenter_Int_(self):
        return int(self.center_x), int(self.center_y)

    def GetRect_(self):
        return self.left, self.top, self.right, self.bottom

    def GetRect_Int_(self):
        return int(self.left), int(self.top), int(self.right), int(self.bottom)

    def GetGeom_(self):
        return self.left, self.top, self.width, self.height

    def GetGeom_Int_(self):
        return int(self.left), int(self.top), int(self.width), int(self.height)

    def GetImgROI_(self, img_ori):
        return img_ori[int(self.top):int(self.bottom),int(self.left):int(self.right)]

    def GenerateScaleRect_(self, scale):
        leftscale = self.center_x - self.width * scale / 2
        topscale = self.center_y - self.height * scale / 2
        rightscale = self.center_x + self.width * scale  / 2
        bottomscale = self.center_y + self.height * scale/ 2
        return rectBase([leftscale, topscale, rightscale, bottomscale], "Rect")