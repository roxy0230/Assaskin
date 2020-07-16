import urllib.request
import webbrowser

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QObject, pyqtSignal, QEvent
from PyQt5.QtWidgets import QMessageBox


class UIController(object):
    def __init__(self, videoController):
        self.StatsButton = None
        self.StatsLabel = None
        self.StatsButton_2 = None
        self.videoController = videoController
        self.articleFavButtons = []

    def clickable(self, widget):

        class Filter(QObject):

            clicked = pyqtSignal()

            def eventFilter(self, obj, event):

                if obj == widget:
                    if event.type() == QEvent.MouseButtonRelease:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            return True
                return False

        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked

    def showUi(self, uiElement, pagesList):
        for element in pagesList:
            if element == uiElement:
                element.setVisible(True)
            else:
                element.setVisible(False)

    def backToTutorials(self, uiElement, pagesList):
        self.videoController().reloadVideo('')
        self.showUi(uiElement, pagesList)

    def createTutorialPage(self, parentWidget, gridLayout, row, column, title, imageURL, tutorialWindow, pagesList,
                           favButton, favTutorials, tutorialData, modifyFavList, setFavList, getUserName,
                           videoController):
        _translate = QtCore.QCoreApplication.translate
        TutorialFrame = QtWidgets.QFrame(parentWidget)
        TutorialFrame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TutorialFrame.sizePolicy().hasHeightForWidth())
        TutorialFrame.setSizePolicy(sizePolicy)
        TutorialFrame.setMinimumSize(QtCore.QSize(320, 350))
        TutorialFrame.setStyleSheet("border-radius: 15px;\n"
                                    "border-top-left-radius: 0;\n"
                                    "border-top-right-radius: 0;\n"
                                    "border: 1px solid white;\n"
                                    "background-color: rgb(24, 29, 45);\n"
                                    "")
        TutorialFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        TutorialFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        TutorialFrame.setLineWidth(0)
        TutorialFrame.setMidLineWidth(0)
        TutorialFrame.setObjectName("TutorialFrame")
        imageData = urllib.request.urlopen(imageURL).read()
        image = QtGui.QImage()
        image.loadFromData(imageData)
        TutorialThumbnail = QtWidgets.QLabel(TutorialFrame)
        TutorialThumbnail.setGeometry(QtCore.QRect(0, 0, 320, 180))
        TutorialThumbnail.setStyleSheet("border-bottom: none;\n"
                                        "border-bottom-left-radius: 0;\n"
                                        "border-bottom-right-radius: 0;\n"
                                        "")
        TutorialThumbnail.setFrameShadow(QtWidgets.QFrame.Plain)
        TutorialThumbnail.setText("")
        TutorialThumbnail.setPixmap(QtGui.QPixmap(image))
        TutorialThumbnail.setScaledContents(True)
        TutorialThumbnail.setAlignment(QtCore.Qt.AlignCenter)
        TutorialThumbnail.setWordWrap(False)
        TutorialThumbnail.setObjectName("TutorialThumbnail")
        TutorialTitle = QtWidgets.QLabel(TutorialFrame)
        TutorialTitle.setGeometry(QtCore.QRect(10, 200, 300, 140))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(9)
        TutorialTitle.setFont(font)
        TutorialTitle.setStyleSheet("border: none;\n"
                                    "color: rgb(255, 255, 255);")
        TutorialTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        TutorialTitle.setScaledContents(False)
        TutorialTitle.setAlignment(QtCore.Qt.AlignCenter)
        TutorialTitle.setWordWrap(True)
        TutorialTitle.setIndent(0)
        TutorialTitle.setMargin(10)
        TutorialTitle.setObjectName("TutorialTitle")
        self.line = QtWidgets.QFrame(TutorialFrame)
        self.line.setGeometry(QtCore.QRect(60, 200, 201, 3))
        self.line.setStyleSheet("border: none;\n"
                                "border-top: 1px solid white;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        gridLayout.addWidget(TutorialFrame, row, column, 1, 1)
        TutorialTitle.setText(_translate("mainWindow", title))
        self.clickable(TutorialFrame).connect(
            lambda: self.changeToTutorialPage(tutorialWindow, pagesList, favButton, favTutorials, tutorialData,
                                              modifyFavList, setFavList, getUserName, videoController))

    def changeToTutorialPage(self, tutorialWindow, pagesList, favButton, favTutorials, tutorialData, modifyFavList,
                             setFavList, getUserName, videoController):
        self.showUi(tutorialWindow, pagesList)
        videoController().reloadVideo(tutorialData.getUrl())
        try:
            favButton.disconnect()
        except Exception:
            pass
        favButton.clicked.connect(
            lambda: self.favoriteUtilityTutorials(favButton, favTutorials, tutorialData.getId(), modifyFavList,
                                                  setFavList))
        isFavorite = False
        if getUserName() is None:
            favButton.setVisible(False)
        else:
            favIcon = QtGui.QIcon()
            favButton.setVisible(True)
            for index in favTutorials:
                if index == int(tutorialData.getId()):
                    isFavorite = True
                    break
            if isFavorite:
                favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            else:
                favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/not_favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            favButton.setIcon(favIcon)

    def createProductFrame(self, parentWidget, gridLayout, row, column, productData, productWindow, pagesList,
                           productTitle, productDescription, productPrice, productImage, linkButton, favButton,
                           getUserName, favProducts, modifyFavList, setFavList, productFrames):
        _translate = QtCore.QCoreApplication.translate
        newProductFrame = QtWidgets.QFrame(parentWidget)
        productFrames.append({"frame": newProductFrame, "type": productData.getSkinType()})
        newProductFrame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(newProductFrame.sizePolicy().hasHeightForWidth())
        newProductFrame.setSizePolicy(sizePolicy)
        newProductFrame.setMinimumSize(QtCore.QSize(200, 350))
        newProductFrame.setStyleSheet("border-radius: 15px;\n"
                                      "border: 1px solid white;\n"
                                      "background-color: rgb(24, 29, 45);\n"
                                      "")
        newProductFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        newProductFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        newProductFrame.setLineWidth(0)
        newProductFrame.setMidLineWidth(0)
        newProductFrame.setObjectName("frame_2")
        imageData = urllib.request.urlopen(productData.getImageURL()).read()
        image = QtGui.QImage()
        image.loadFromData(imageData)
        imageLabel = QtWidgets.QLabel(newProductFrame)
        imageLabel.setGeometry(QtCore.QRect(50, 10, 101, 181))
        imageLabel.setStyleSheet("border: none")
        imageLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        imageLabel.setText("")
        imageLabel.setPixmap(QtGui.QPixmap(image))
        imageLabel.setScaledContents(True)
        imageLabel.setObjectName("label_7")
        nameLabel = QtWidgets.QLabel(newProductFrame)
        nameLabel.setGeometry(QtCore.QRect(20, 200, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(7)
        nameLabel.setFont(font)
        nameLabel.setStyleSheet("border: none;\n"
                                "border-radius: 0 0;\n"
                                "border-top: 1px solid white;\n"
                                "color: rgb(255, 255, 255);")
        nameLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        nameLabel.setScaledContents(False)
        nameLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        nameLabel.setWordWrap(True)
        nameLabel.setIndent(0)
        nameLabel.setMargin(16)
        nameLabel.setObjectName("label_8")
        priceLabel = QtWidgets.QLabel(newProductFrame)
        priceLabel.setGeometry(QtCore.QRect(70, 270, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(11)
        priceLabel.setFont(font)
        priceLabel.setStyleSheet("border-radius:30px 30px;\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "border: none;\n"
                                 "background-color: rgb(225, 160, 103);")
        priceLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        priceLabel.setScaledContents(False)
        priceLabel.setAlignment(QtCore.Qt.AlignCenter)
        priceLabel.setWordWrap(False)
        priceLabel.setIndent(0)
        priceLabel.setObjectName("label_9")
        gridLayout.addWidget(newProductFrame, row, column, 1, 1)
        nameLabel.setText(_translate("mainWindow", productData.getName()))
        priceLabel.setText(_translate("mainWindow", str(productData.getPrice()) + "$"))
        self.clickable(newProductFrame).connect(
            lambda: self.changeToProductPage(productData, productWindow, pagesList, productTitle, productDescription,
                                             productPrice, productImage, linkButton, favButton, getUserName,
                                             favProducts, modifyFavList, setFavList))

    def changeToProductPage(self, productData, productWindow, pagesList, productTitle, productDescription, productPrice,
                            productImage, linkButton, favButton, getUserName, favProducts, modifyFavList, setFavList):
        self.showUi(productWindow, pagesList)
        productTitle.setText(productData.getName())
        productDescription.setText(productData.getDescription())
        productPrice.setText(str(productData.getPrice()) + "$")
        imageData = urllib.request.urlopen(productData.getImageURL()).read()
        image = QtGui.QImage()
        image.loadFromData(imageData)
        productImage.setPixmap(QtGui.QPixmap(image))
        try:
            linkButton.disconnect()
            favButton.disconnect()
        except Exception:
            pass
        linkButton.clicked.connect(lambda: self.openLink(productData.getLink()))
        favButton.clicked.connect(
            lambda: self.favoriteUtilityProducts(favButton, favProducts, productData.getId(), modifyFavList,
                                                 setFavList))
        isFavorite = False
        if getUserName() is None:
            favButton.setVisible(False)
        else:
            favIcon = QtGui.QIcon()
            favButton.setVisible(True)
            for index in favProducts:
                if index == int(productData.getId()):
                    isFavorite = True
                    break
            if isFavorite:
                favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            else:
                favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/not_favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            favButton.setIcon(favIcon)

    def createArticleFrame(self, parentWidget, gridLayout, articleData, getUserName, favArticles, modifyFavList,
                           setFavList):
        _translate = QtCore.QCoreApplication.translate
        exampleArticle = QtWidgets.QFrame(parentWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(exampleArticle.sizePolicy().hasHeightForWidth())
        exampleArticle.setSizePolicy(sizePolicy)
        exampleArticle.setMinimumSize(QtCore.QSize(800, 300))
        exampleArticle.setMaximumSize(QtCore.QSize(800, 300))
        font = QtGui.QFont()
        font.setFamily("MS UI Gothic")
        exampleArticle.setFont(font)
        exampleArticle.setStyleSheet("border-radius: 15px;\n"
                                     "border: 1px solid white;\n"
                                     "background-color: rgb(24, 29, 45);\n"
                                     "")
        exampleArticle.setFrameShape(QtWidgets.QFrame.NoFrame)
        exampleArticle.setFrameShadow(QtWidgets.QFrame.Raised)
        exampleArticle.setLineWidth(0)
        exampleArticle.setMidLineWidth(0)
        exampleArticle.setObjectName("exampleArticle")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(exampleArticle)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setSpacing(0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        ArticleTitle = QtWidgets.QLabel(exampleArticle)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(11)
        ArticleTitle.setFont(font)
        ArticleTitle.setStyleSheet("border: none;\n"
                                   "border-top-right-radius: 0;\n"
                                   "border-bottom-right-radius: 0;\n"
                                   "color: white;")
        ArticleTitle.setAlignment(QtCore.Qt.AlignCenter)
        ArticleTitle.setWordWrap(True)
        ArticleTitle.setMargin(25)
        ArticleTitle.setIndent(0)
        ArticleTitle.setObjectName("ArticleTitle")
        horizontalLayout_2.addWidget(ArticleTitle)
        ArticleImage = QtWidgets.QLabel(exampleArticle)
        ArticleImage.setStyleSheet("border: none")
        ArticleImage.setMinimumSize(QtCore.QSize(360, 0))
        ArticleImage.setMaximumSize(QtCore.QSize(360, 16777215))

        ArticleImage.setFrameShadow(QtWidgets.QFrame.Plain)
        ArticleImage.setText("")
        imageData = urllib.request.urlopen(articleData.getImageUrl()).read()
        image = QtGui.QImage()
        image.loadFromData(imageData)
        ArticleImage.setPixmap(QtGui.QPixmap(image))
        ArticleImage.setScaledContents(False)
        ArticleImage.setAlignment(QtCore.Qt.AlignCenter)
        ArticleImage.setWordWrap(False)
        ArticleImage.setObjectName("ArticleImage")
        horizontalLayout_2.addWidget(ArticleImage)
        LinkButtonFrame = QtWidgets.QFrame(exampleArticle)
        LinkButtonFrame.setMinimumSize(QtCore.QSize(67, 0))
        LinkButtonFrame.setMaximumSize(QtCore.QSize(40, 16777215))
        LinkButtonFrame.setStyleSheet("border: none;\n"
                                      "background-color : rgba(101, 108, 131, 30);\n"
                                      "border-top-left-radius: 0;\n"
                                      "border-bottom-left-radius: 0;\n"
                                      "")
        LinkButtonFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        LinkButtonFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        LinkButtonFrame.setObjectName("LinkButtonFrame")
        verticalLayout_2 = QtWidgets.QVBoxLayout(LinkButtonFrame)
        verticalLayout_2.setObjectName("verticalLayout_2")

        BackButton_2 = QtWidgets.QPushButton(LinkButtonFrame)
        BackButton_2.setGeometry(QtCore.QRect(9, 130, 48, 44))
        BackButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        BackButton_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        BackButton_2.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Assets/Icons/go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BackButton_2.setIcon(icon9)
        BackButton_2.setIconSize(QtCore.QSize(42, 42))
        BackButton_2.setObjectName("BackButton_2")
        BackButton_2.clicked.connect(lambda: self.openLink(articleData.getUrl()))
        verticalLayout_2.addWidget(BackButton_2)

        favButton = QtWidgets.QPushButton(LinkButtonFrame)
        self.articleFavButtons.append({"button": favButton, "id": articleData.getId()})
        favButton.setGeometry(QtCore.QRect(9, 130, 48, 44))
        favButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        favButton.setStyleSheet("background-color: rgba(0,0,0,0)")
        favButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("Assets/Icons/go.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        favButton.setIcon(icon9)
        favButton.setIconSize(QtCore.QSize(42, 42))
        favButton.setObjectName("favButton")
        verticalLayout_2.addWidget(favButton)

        favButton.clicked.connect(
            lambda: self.favoriteUtilityArticles(favButton, favArticles, articleData.getId(), modifyFavList,
                                                 setFavList))
        favButton.setVisible(False)

        horizontalLayout_2.addWidget(LinkButtonFrame)
        gridLayout.addWidget(exampleArticle)
        ArticleTitle.setText(_translate("mainWindow", articleData.getTitle()))

        return exampleArticle

    def createUserButton(self, layoutWidget, sidebarButtons):
        self.StatsButton = QtWidgets.QHBoxLayout()
        self.StatsButton.setObjectName("StatsButton")
        self.StatsButton_2 = QtWidgets.QPushButton(layoutWidget)
        self.StatsButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StatsButton_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.StatsButton_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("Assets/Icons/userIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StatsButton_2.setIcon(icon7)
        self.StatsButton_2.setIconSize(QtCore.QSize(42, 42))
        self.StatsButton_2.setObjectName("StatsButton_2")
        self.StatsButton.addWidget(self.StatsButton_2, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.StatsLabel = QtWidgets.QLabel(layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.StatsLabel.setFont(font)
        self.StatsLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.StatsLabel.setStyleSheet("background-color: rgba(0,0,0,0);\ncolor: white")
        self.StatsLabel.setScaledContents(False)
        self.StatsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StatsLabel.setWordWrap(False)
        self.StatsLabel.setIndent(0)
        self.StatsLabel.setObjectName("StatsLabel")
        self.StatsButton.addWidget(self.StatsLabel, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        sidebarButtons.addLayout(self.StatsButton)
        self.hideUserButton()

    def showUserButton(self, sidebarButtons, userName, userPage, pagesList):
        _translate = QtCore.QCoreApplication.translate
        sidebarButtons.addLayout(self.StatsButton)
        try:
            self.StatsButton_2.disconnect()
        except Exception:
            pass
        self.StatsButton_2.clicked.connect(lambda: self.showUi(userPage, pagesList))
        self.StatsButton_2.setVisible(True)
        self.StatsLabel.setVisible(True)
        self.StatsLabel.setText(_translate("mainWindow", str(userName)))

    def hideUserButton(self):
        self.StatsButton.setParent(None)
        self.StatsButton_2.setVisible(False)
        self.StatsLabel.setVisible(False)

    def showDialog(self, title, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)

        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def openLink(self, link):
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(link)

    def favoriteUtilityProducts(self, favButton, favProducts, id, modifyFavList, setFavList):
        favIcon = QtGui.QIcon()
        isFavorite = False
        for index in favProducts:
            if index == id:
                isFavorite = True
                break

        if isFavorite:
            favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/not_favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            favProducts.remove(int(id))
            modifyFavList('PRODUCTS', 'remove', int(id))
        else:
            favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            favProducts.append(int(id))
            modifyFavList('PRODUCTS', 'add', int(id))
        favButton.setIcon(favIcon)
        setFavList()

    def favoriteUtilityTutorials(self, favButton, favTutorials, id, modifyFavList, setFavList):
        favIcon = QtGui.QIcon()
        isFavorite = False
        for index in favTutorials:
            if index == id:
                isFavorite = True
                break

        if isFavorite:
            favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/not_favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            favTutorials.remove(int(id))
            modifyFavList('TUTORIALS', 'remove', int(id))
        else:
            favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            favTutorials.append(int(id))
            modifyFavList('TUTORIALS', 'add', int(id))
        favButton.setIcon(favIcon)
        setFavList()

    def favoriteUtilityArticles(self, favButton, favArticles, id, modifyFavList, setFavList):
        favIcon = QtGui.QIcon()
        isFavorite = False
        for index in favArticles:
            if index == id:
                isFavorite = True
                break

        if isFavorite:
            favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/not_favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            favArticles.remove(int(id))
            modifyFavList('ARTICLES', 'remove', int(id))
        else:
            favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            favArticles.append(int(id))
            modifyFavList('ARTICLES', 'add', int(id))
        favButton.setIcon(favIcon)
        setFavList()
