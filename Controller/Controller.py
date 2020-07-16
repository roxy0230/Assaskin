import json

import requests
from PyQt5 import QtCore, QtGui
from google.cloud import firestore

from Controller.FirebaseController import FirebaseController
from Controller.QuizController import QuizController
from Controller.UIController import UIController
from Controller.UserPageController import UserPageController
from Controller.YoutubeAPI import YoutubeAPI
from Domains.Product import Product
from Domains.Tutorial import Tutorial
from Repository.ArticlesRep import ArticlesRep
from Repository.ProductsRep import ProductsRep
from Repository.TutorialsRep import TutorialsRep


class Controller(object):
    def __init__(self):
        self.uiController = UIController(self.getVideoController)
        self.firebaseController = FirebaseController()
        self.firebaseController.setup()
        self.youtubeController = YoutubeAPI()
        self.productsRep = ProductsRep()
        self.tutorialsRep = TutorialsRep()
        self.articlesRep = ArticlesRep()
        self.VideoPlayerController = None
        self.currentUser = None
        self.favProducts = []
        self.favTutorials = []
        self.favArticles = []
        self.userPageController = UserPageController(self.favProducts, self.favTutorials, self.favArticles,
                                                     self.currentUser,
                                                     self.firebaseController,
                                                     self.productsRep, self.tutorialsRep, self.articlesRep)
        self.quizController = QuizController(self.addQuizResultToUser, self.userPageController, self.getUser)
        self.comboBox = None
        self.productFrames = []

    def generateProductPages(self, parentWidget, gridLayout, productWindow, pagesList, productTitle, productDescription,
                             productPrice, productImage, linkButton, favButton):
        row = 0
        column = 0
        for doc in self.firebaseController.productDocs:
            newProduct = Product(doc.to_dict().get("ID"), doc.to_dict().get("NAME"), doc.to_dict().get("DESCRIPTION"),
                                 doc.to_dict().get("IMAGE_URL"), doc.to_dict().get("PRICE"), doc.to_dict().get("LINK"), doc.to_dict().get("SKIN_TYPE"))
            self.productsRep.add(newProduct)
            self.uiController.createProductFrame(parentWidget, gridLayout, row, column, newProduct, productWindow,
                                                 pagesList, productTitle, productDescription, productPrice,
                                                 productImage, linkButton, favButton, self.getUserName,
                                                 self.favProducts, self.modifyFavList,
                                                 self.userPageController.setFavProductPages, self.productFrames)
            column += 1
            if column > 1:
                row += 1
                column = 0

    def modifyFavList(self, listName, editType, value):
        userQuery = None
        try:
            userQuery = self.firebaseController.userDocs.where(u'UUID', u'==',
                                                               str(self.currentUser.get('localId'))).get()
        except:
            pass
        if userQuery is not None:
            for item in userQuery:
                doc = self.firebaseController.userDocs.document(item.id)
                if editType == 'add':
                    doc.update({str(listName): firestore.ArrayUnion([value])})
                else:
                    doc.update({str(listName): firestore.ArrayRemove([value])})
                break

    def addQuizResultToUser(self, result):
        userQuery = None
        try:
            userQuery = self.firebaseController.userDocs.where(u'UUID', u'==',
                                                               str(self.currentUser.get('localId'))).get()
        except:
            pass
        if userQuery is not None:
            for item in userQuery:
                doc = self.firebaseController.userDocs.document(item.id)
                doc.update({str('QUIZ_RESULT'): str(result)})
                break

    def generateTutorialPages(self, parentWidget, gridLayout, tutorialWindow, pagesList, favButton):
        row = 0
        column = 0
        for doc in self.firebaseController.tutorialDocs:
            imageURL = self.youtubeController.getVideoThumbnail(doc.to_dict().get("URL"))
            newTutorial = Tutorial(doc.to_dict().get("ID"), doc.to_dict().get("TITLE"), doc.to_dict().get("URL"),
                                   imageURL)
            self.tutorialsRep.add(newTutorial)
            self.uiController.createTutorialPage(parentWidget, gridLayout, row, column, doc.to_dict().get("TITLE"),
                                                 imageURL, tutorialWindow, pagesList, favButton, self.favTutorials,
                                                 newTutorial, self.modifyFavList,
                                                 self.userPageController.setFavTutorialPages, self.getUserName,
                                                 self.getVideoController)
            column += 1
            if column > 1:
                row += 1
                column = 0

    def generateArticlesPages(self, parentWidget, gridLayout):
        for doc in self.firebaseController.articleDocs:
            newArticle = Tutorial(doc.to_dict().get("ID"), doc.to_dict().get("TITLE"), doc.to_dict().get("LINK"),
                                  doc.to_dict().get("IMAGE_URL"))
            self.articlesRep.add(newArticle)
            self.uiController.createArticleFrame(parentWidget, gridLayout, newArticle, self.getUserName,
                                                 self.favArticles,
                                                 self.modifyFavList,
                                                 self.userPageController.setFavArticlesPages)

    def register(self, userElement, emailElement, passwordElement, sidebarButtons, welcomeScreen, pagesList,
                 welcomeLabel, homeButton, userPage, userPageName):
        _translate = QtCore.QCoreApplication.translate
        user = None
        try:
            user = self.firebaseController.auth.create_user_with_email_and_password(emailElement.text(),
                                                                                    passwordElement.text())
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']['message']
            if error == "EMAIL_EXISTS":
                self.uiController.showDialog("Register Failed", "Email already exists")
            else:
                self.uiController.showDialog("Register Failed",
                                             "It seems there is an error on this register attempt. Please try again later")
        if user is not None:
            data = {
                u'UUID': str(user.get('localId')),
                u'NAME': str(userElement.text()),
                u'PRODUCTS': [],
                u'TUTORIALS': [],
                u'ARTICLES': [],
                u'QUIZ_RESULT': ''
            }
            self.firebaseController.userDocs.add(data)
            self.currentUser = user
            self.favProducts.clear()
            self.favTutorials.clear()
            self.favArticles.clear()
            self.userPageController.setFavProductPages()
            self.userPageController.setFavTutorialPages()
            self.userPageController.setFavArticlesPages()
            self.setArticleFavButtons()
            self.uiController.showUserButton(sidebarButtons, self.getUserName(), userPage, pagesList)
            self.uiController.showUi(welcomeScreen, pagesList)
            homeButton.clicked.connect(lambda: controller.uiController.showUi(welcomeScreen, pagesList))
            welcomeLabel.setText(_translate("mainWindow", "Welcome, " + str(self.getUserName())))
            userPageName.setText(_translate("mainWindow", str(self.getUserName())))
        userElement.setText('')
        emailElement.setText('')
        passwordElement.setText('')

    def logIn(self, userElement, passwordElement, sidebarButtons, welcomeScreen, pagesList, welcomeLabel, homeButton,
              userPage, userPageName, quizTitle, quizText):
        _translate = QtCore.QCoreApplication.translate
        user = None
        try:
            user = self.firebaseController.auth.sign_in_with_email_and_password(userElement.text(),
                                                                                passwordElement.text())
        except:
            self.uiController.showDialog("Login Failed", "Email or Password is Incorrect")
        if user is not None:
            self.currentUser = user
            self.getFavs()
            self.userPageController.setFavProductPages()
            self.userPageController.setFavTutorialPages()
            self.userPageController.setFavArticlesPages()
            self.setArticleFavButtons()
            self.uiController.showUserButton(sidebarButtons, self.getUserName(), userPage, pagesList)
            self.uiController.showUi(welcomeScreen, pagesList)
            self.userPageController.setQuizResult(quizTitle, quizText, user, self.comboBox, self.changeFilter)
            homeButton.clicked.connect(lambda: controller.uiController.showUi(welcomeScreen, pagesList))
            welcomeLabel.setText(_translate("mainWindow", "Welcome, " + str(self.getUserName())))
            userPageName.setText(_translate("mainWindow", str(self.getUserName())))

        userElement.setText('')
        passwordElement.setText('')

    def logOut(self, firstScreen, pagesList, homeButton):
        self.uiController.hideUserButton()
        self.currentUser = None
        self.uiController.showUi(firstScreen, pagesList)
        self.comboBox.setVisible(False)
        self.changeFilter('All Items')
        self.comboBox.setCurrentIndex(0)
        self.setArticleFavButtons()
        homeButton.clicked.connect(lambda: controller.uiController.showUi(firstScreen, pagesList))

    def getUserName(self):
        userQuery = None
        try:
            userQuery = self.firebaseController.userDocs.where(u'UUID', u'==',
                                                               str(self.currentUser.get('localId'))).stream()
        except:
            pass
        userName = None
        if userQuery is not None:
            for doc in userQuery:
                userName = doc.to_dict().get('NAME')
        return userName

    def getSkinType(self):
        userQuery = None
        try:
            userQuery = self.firebaseController.userDocs.where(u'UUID', u'==',
                                                               str(self.currentUser.get('localId'))).stream()
        except:
            pass
        type = None
        if userQuery is not None:
            for doc in userQuery:
                type = doc.to_dict().get('QUIZ_RESULT')
        return type

    def getFavs(self):
        userQuery = None
        self.favProducts.clear()
        self.favTutorials.clear()
        self.favArticles.clear()
        try:
            userQuery = self.firebaseController.userDocs.where(u'UUID', u'==',
                                                               str(self.currentUser.get('localId'))).stream()
        except:
            pass
        if userQuery is not None:
            for doc in userQuery:
                for key in doc.to_dict().get('PRODUCTS'):
                    self.favProducts.append(key)
                for key in doc.to_dict().get('TUTORIALS'):
                    self.favTutorials.append(key)
                for key in doc.to_dict().get('ARTICLES'):
                    self.favArticles.append(key)
                break

    def getUser(self):
        return self.currentUser

    def getVideoController(self):
        return self.VideoPlayerController

    def setArticleFavButtons(self):
        for buttonData in self.uiController.articleFavButtons:
            isFavorite = False
            if self.getUserName() is None:
                buttonData.get("button").setVisible(False)
            else:
                favIcon = QtGui.QIcon()
                buttonData.get("button").setVisible(True)
                for index in self.favArticles:
                    if index == int(buttonData.get("id")):
                        isFavorite = True
                        break
                if isFavorite:
                    favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/favorite.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                else:
                    favIcon.addPixmap(QtGui.QPixmap("Assets/Icons/not_favorite.png"), QtGui.QIcon.Normal,
                                      QtGui.QIcon.Off)
                buttonData.get("button").setIcon(favIcon)

    def changeFilter(self, value):
        skinType = self.getSkinType()
        allOptions = 'All Items'
        userOptions = 'For your skin type'
        for frameData in self.productFrames:
            if value == allOptions:
                frameData.get("frame").setVisible(True)
            else:
                if frameData.get("type") == skinType:
                    frameData.get("frame").setVisible(True)
                else:
                    frameData.get("frame").setVisible(False)




controller = Controller()
