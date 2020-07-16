# -*- coding: utf-8 -*-
import cv2
import easygui
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QImage


class ImageManipulation(object):

    @staticmethod
    def getImage(imageWidget):
        rawImage = easygui.fileopenbox()  # open file dialog for acquiring the image
        imageData = cv2.imread(rawImage, 1)  # get the image data with OpenCV
        height, width, byteValue = imageData.shape
        byteValue = byteValue * width
        rgbImage = cv2.cvtColor(imageData, cv2.COLOR_BGR2RGB)  # convert the color format to RGB (OpenCV uses BGR)
        GUIImage = QtGui.QImage(rgbImage, width, height, byteValue,
                                QImage.Format_RGB888)  # create an UI element for showing the photo in UI
        # noinspection PyCallByClass
        pixMap = QtGui.QPixmap.fromImage(GUIImage)  # create a pixelMap from the UI Element
        imageWidget.setPixmap(pixMap.scaled(211, 211, QtCore.Qt.KeepAspectRatio))  # set the pixelMap to a UI container
