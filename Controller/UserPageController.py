import urllib.request

from PyQt5 import QtWidgets, QtCore, QtGui


class UserPageController(object):
    def __init__(self, favProducts, favTutorials, favArticles, currentUser, firebaseController, productsRep,
                 tutorialsRep, articlesRep):
        self.currentUser = currentUser
        self.favProducts = favProducts
        self.favTutorials = favTutorials
        self.favArticles = favArticles
        self.firebaseController = firebaseController
        self.productsRep = productsRep
        self.tutorialsRep = tutorialsRep
        self.articlesRep = articlesRep
        self.favProductsFrames = []
        self.favTutorialsFrames = []
        self.favArticlesFrames = []
        self.quizResult = ''

    def createFavProductFrame(self, parentWidget, gridLayout, title, imageURL, id):
        favProductItem = QtWidgets.QFrame(parentWidget)
        self.favProductsFrames.append({"frame": favProductItem, "id": id})
        favProductItem.setMinimumSize(QtCore.QSize(372, 80))
        favProductItem.setMaximumSize(QtCore.QSize(372, 80))
        favProductItem.setStyleSheet("border: 1px solid white;\n"
                                     "border-top-right-radius: 0;\n"
                                     "border-bottom-right-radius: 0;")
        favProductItem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        favProductItem.setFrameShadow(QtWidgets.QFrame.Raised)
        favProductItem.setObjectName("FavProductItem")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(favProductItem)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setSpacing(0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        FavProdItemTitle = QtWidgets.QLabel(favProductItem)
        FavProdItemTitle.setMinimumSize(QtCore.QSize(270, 78))
        FavProdItemTitle.setMaximumSize(QtCore.QSize(270, 78))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        FavProdItemTitle.setFont(font)
        FavProdItemTitle.setStyleSheet("border: none;\n"
                                       "color: white;")
        FavProdItemTitle.setScaledContents(False)
        FavProdItemTitle.setAlignment(QtCore.Qt.AlignCenter)
        FavProdItemTitle.setWordWrap(True)
        FavProdItemTitle.setMargin(15)
        FavProdItemTitle.setText(str(title))
        FavProdItemTitle.setIndent(0)
        FavProdItemTitle.setObjectName("FavProdItemTitle")
        horizontalLayout_2.addWidget(FavProdItemTitle)
        FavProdItemImage = QtWidgets.QLabel(favProductItem)
        FavProdItemImage.setMinimumSize(QtCore.QSize(100, 0))
        FavProdItemImage.setMaximumSize(QtCore.QSize(100, 80))
        FavProdItemImage.setStyleSheet("border: none;")
        FavProdItemImage.setText("")
        imageData = urllib.request.urlopen(imageURL).read()
        image = QtGui.QImage()
        image.loadFromData(imageData)
        FavProdItemImage.setPixmap(QtGui.QPixmap(image))
        FavProdItemImage.setScaledContents(True)
        FavProdItemImage.setAlignment(QtCore.Qt.AlignCenter)
        FavProdItemImage.setObjectName("FavProdItemImage")
        horizontalLayout_2.addWidget(FavProdItemImage)
        gridLayout.addWidget(favProductItem)

    def createFavTutorialFrame(self, parentWidget, gridLayout, title, url, id):
        favProductItem = QtWidgets.QFrame(parentWidget)
        self.favTutorialsFrames.append({"frame": favProductItem, "id": id})
        favProductItem.setMinimumSize(QtCore.QSize(372, 80))
        favProductItem.setMaximumSize(QtCore.QSize(372, 80))
        favProductItem.setStyleSheet("border: 1px solid white;\n"
                                     "border-top-right-radius: 0;\n"
                                     "border-bottom-right-radius: 0;")
        favProductItem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        favProductItem.setFrameShadow(QtWidgets.QFrame.Raised)
        favProductItem.setObjectName("FavProductItem")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(favProductItem)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setSpacing(0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        FavProdItemTitle = QtWidgets.QLabel(favProductItem)
        FavProdItemTitle.setMinimumSize(QtCore.QSize(270, 78))
        FavProdItemTitle.setMaximumSize(QtCore.QSize(270, 78))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        FavProdItemTitle.setFont(font)
        FavProdItemTitle.setStyleSheet("border: none;\n"
                                       "color: white;")
        FavProdItemTitle.setScaledContents(False)
        FavProdItemTitle.setAlignment(QtCore.Qt.AlignCenter)
        FavProdItemTitle.setWordWrap(True)
        FavProdItemTitle.setMargin(15)
        FavProdItemTitle.setText(str(title))
        FavProdItemTitle.setIndent(0)
        FavProdItemTitle.setObjectName("FavProdItemTitle")
        horizontalLayout_2.addWidget(FavProdItemTitle)
        FavProdItemImage = QtWidgets.QLabel(favProductItem)
        FavProdItemImage.setMinimumSize(QtCore.QSize(100, 0))
        FavProdItemImage.setMaximumSize(QtCore.QSize(100, 80))
        FavProdItemImage.setStyleSheet("border: none;")
        FavProdItemImage.setText("")
        imageData = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(imageData)
        FavProdItemImage.setPixmap(QtGui.QPixmap(image))
        FavProdItemImage.setScaledContents(True)
        FavProdItemImage.setAlignment(QtCore.Qt.AlignCenter)
        FavProdItemImage.setObjectName("FavProdItemImage")
        horizontalLayout_2.addWidget(FavProdItemImage)
        gridLayout.addWidget(favProductItem)

    def createFavArticleFrame(self, parentWidget, gridLayout, title, url, id):
        favProductItem = QtWidgets.QFrame(parentWidget)
        self.favArticlesFrames.append({"frame": favProductItem, "id": id})
        favProductItem.setMinimumSize(QtCore.QSize(372, 80))
        favProductItem.setMaximumSize(QtCore.QSize(372, 80))
        favProductItem.setStyleSheet("border: 1px solid white;\n"
                                     "border-top-right-radius: 0;\n"
                                     "border-bottom-right-radius: 0;")
        favProductItem.setFrameShape(QtWidgets.QFrame.StyledPanel)
        favProductItem.setFrameShadow(QtWidgets.QFrame.Raised)
        favProductItem.setObjectName("FavProductItem")
        horizontalLayout_2 = QtWidgets.QHBoxLayout(favProductItem)
        horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        horizontalLayout_2.setSpacing(0)
        horizontalLayout_2.setObjectName("horizontalLayout_2")
        FavProdItemTitle = QtWidgets.QLabel(favProductItem)
        FavProdItemTitle.setMinimumSize(QtCore.QSize(270, 78))
        FavProdItemTitle.setMaximumSize(QtCore.QSize(270, 78))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        FavProdItemTitle.setFont(font)
        FavProdItemTitle.setStyleSheet("border: none;\n"
                                       "color: white;")
        FavProdItemTitle.setScaledContents(False)
        FavProdItemTitle.setAlignment(QtCore.Qt.AlignCenter)
        FavProdItemTitle.setWordWrap(True)
        FavProdItemTitle.setMargin(15)
        FavProdItemTitle.setText(str(title))
        FavProdItemTitle.setIndent(0)
        FavProdItemTitle.setObjectName("FavProdItemTitle")
        horizontalLayout_2.addWidget(FavProdItemTitle)
        FavProdItemImage = QtWidgets.QLabel(favProductItem)
        FavProdItemImage.setMinimumSize(QtCore.QSize(100, 0))
        FavProdItemImage.setMaximumSize(QtCore.QSize(100, 80))
        FavProdItemImage.setStyleSheet("border: none;")
        FavProdItemImage.setText("")
        imageData = urllib.request.urlopen(url).read()
        image = QtGui.QImage()
        image.loadFromData(imageData)
        FavProdItemImage.setPixmap(QtGui.QPixmap(image))
        FavProdItemImage.setScaledContents(True)
        FavProdItemImage.setAlignment(QtCore.Qt.AlignCenter)
        FavProdItemImage.setObjectName("FavProdItemImage")
        horizontalLayout_2.addWidget(FavProdItemImage)
        gridLayout.addWidget(favProductItem)

    def generateFavProductPages(self, parentWidget, gridLayout):
        for product in self.productsRep.getRep():
            self.createFavProductFrame(parentWidget, gridLayout, product.getName(),
                                       product.getImageURL(), product.getId())

    def generateFavTutorialsPages(self, parentWidget, gridLayout):
        for tutorial in self.tutorialsRep.getRep():
            self.createFavTutorialFrame(parentWidget, gridLayout, tutorial.getTitle(),
                                        tutorial.getImageUrl(), tutorial.getId())

    def generateFavArticlesPages(self, parentWidget, gridLayout):
        for article in self.articlesRep.getRep():
            self.createFavArticleFrame(parentWidget, gridLayout, article.getTitle(),
                                       article.getImageUrl(), article.getId())

    def setFavProductPages(self):
        for frame in self.favProductsFrames:
            try:
                self.favProducts.index(frame.get("id"))
            except:
                frame.get("frame").setVisible(False)
            else:
                frame.get("frame").setVisible(True)

    def setFavTutorialPages(self):
        for frame in self.favTutorialsFrames:
            try:
                self.favTutorials.index(frame.get("id"))
            except:
                frame.get("frame").setVisible(False)
            else:
                frame.get("frame").setVisible(True)

    def setFavArticlesPages(self):
        for frame in self.favArticlesFrames:
            try:
                self.favArticles.index(frame.get("id"))
            except:
                frame.get("frame").setVisible(False)
            else:
                frame.get("frame").setVisible(True)

    def setQuizResult(self, quizTitle, quizText, user, comboBox, changeFilter):
        userQuery = None
        try:
            userQuery = self.firebaseController.userDocs.where(u'UUID', u'==',
                                                               str(user.get('localId'))).stream()
        except:
            pass
        if userQuery is not None:
            for doc in userQuery:
                self.quizResult = doc.to_dict().get('QUIZ_RESULT')
                if self.quizResult != '':
                    quizTitle.setVisible(True)
                    quizText.setVisible(True)
                    comboBox.setVisible(True)
                    quizText.setText(self.quizResult)
                    text = str(comboBox.currentText())
                    if text == "All Items":
                        changeFilter("All Items")
                    else:
                        changeFilter("For your skin type")
                else:
                    quizTitle.setVisible(False)
                    quizText.setVisible(False)
                    changeFilter("All Items")
                    comboBox.setCurrentIndex(0)
                break
