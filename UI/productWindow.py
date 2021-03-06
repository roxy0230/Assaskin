# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1230, 730)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(1230, 730))
        mainWindow.setMaximumSize(QtCore.QSize(1230, 733))
        mainWindow.setAutoFillBackground(False)
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("background-color : rgb(22, 25, 39)\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 1231, 731))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Sidebar = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Sidebar.sizePolicy().hasHeightForWidth())
        self.Sidebar.setSizePolicy(sizePolicy)
        self.Sidebar.setMaximumSize(QtCore.QSize(298, 16777215))
        self.Sidebar.setStyleSheet("background-color : rgba(101, 108, 131, 30)\n"
"")
        self.Sidebar.setFrameShape(QtWidgets.QFrame.Box)
        self.Sidebar.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Sidebar.setLineWidth(-13)
        self.Sidebar.setMidLineWidth(30)
        self.Sidebar.setObjectName("Sidebar")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.Sidebar)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-30, 100, 331, 561))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.SidebarButtons = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.SidebarButtons.setContentsMargins(0, 0, 0, 0)
        self.SidebarButtons.setSpacing(0)
        self.SidebarButtons.setObjectName("SidebarButtons")
        self.HomeButton_35 = QtWidgets.QHBoxLayout()
        self.HomeButton_35.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.HomeButton_35.setContentsMargins(0, 0, -1, -1)
        self.HomeButton_35.setSpacing(6)
        self.HomeButton_35.setObjectName("HomeButton_35")
        self.HomeButton_36 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.HomeButton_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.HomeButton_36.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.HomeButton_36.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.HomeButton_36.setIcon(icon)
        self.HomeButton_36.setIconSize(QtCore.QSize(42, 42))
        self.HomeButton_36.setObjectName("HomeButton_36")
        self.HomeButton_35.addWidget(self.HomeButton_36, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.HomeLabel_18 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.HomeLabel_18.setFont(font)
        self.HomeLabel_18.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.HomeLabel_18.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"")
        self.HomeLabel_18.setScaledContents(False)
        self.HomeLabel_18.setAlignment(QtCore.Qt.AlignCenter)
        self.HomeLabel_18.setWordWrap(False)
        self.HomeLabel_18.setIndent(0)
        self.HomeLabel_18.setObjectName("HomeLabel_18")
        self.HomeButton_35.addWidget(self.HomeLabel_18, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SidebarButtons.addLayout(self.HomeButton_35)
        self.FaceAIButton = QtWidgets.QHBoxLayout()
        self.FaceAIButton.setObjectName("FaceAIButton")
        self.FaceAIButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.FaceAIButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FaceAIButton_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.FaceAIButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/face.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.FaceAIButton_2.setIcon(icon1)
        self.FaceAIButton_2.setIconSize(QtCore.QSize(42, 42))
        self.FaceAIButton_2.setObjectName("FaceAIButton_2")
        self.FaceAIButton.addWidget(self.FaceAIButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.FaceAILabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.FaceAILabel.setFont(font)
        self.FaceAILabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.FaceAILabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"")
        self.FaceAILabel.setScaledContents(False)
        self.FaceAILabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FaceAILabel.setWordWrap(False)
        self.FaceAILabel.setIndent(0)
        self.FaceAILabel.setObjectName("FaceAILabel")
        self.FaceAIButton.addWidget(self.FaceAILabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SidebarButtons.addLayout(self.FaceAIButton)
        self.ProductsButton = QtWidgets.QHBoxLayout()
        self.ProductsButton.setObjectName("ProductsButton")
        self.ProductButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ProductButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProductButton.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.ProductButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/spa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ProductButton.setIcon(icon2)
        self.ProductButton.setIconSize(QtCore.QSize(42, 42))
        self.ProductButton.setObjectName("ProductButton")
        self.ProductsButton.addWidget(self.ProductButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ProductLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.ProductLabel.setFont(font)
        self.ProductLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ProductLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"")
        self.ProductLabel.setScaledContents(False)
        self.ProductLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ProductLabel.setWordWrap(False)
        self.ProductLabel.setIndent(0)
        self.ProductLabel.setObjectName("ProductLabel")
        self.ProductsButton.addWidget(self.ProductLabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SidebarButtons.addLayout(self.ProductsButton)
        self.TutorialsButton = QtWidgets.QHBoxLayout()
        self.TutorialsButton.setObjectName("TutorialsButton")
        self.TutorialsButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.TutorialsButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.TutorialsButton_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.TutorialsButton_2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.TutorialsButton_2.setIcon(icon3)
        self.TutorialsButton_2.setIconSize(QtCore.QSize(42, 42))
        self.TutorialsButton_2.setObjectName("TutorialsButton_2")
        self.TutorialsButton.addWidget(self.TutorialsButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.TutorialsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.TutorialsLabel.setFont(font)
        self.TutorialsLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.TutorialsLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"")
        self.TutorialsLabel.setScaledContents(False)
        self.TutorialsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TutorialsLabel.setWordWrap(False)
        self.TutorialsLabel.setIndent(0)
        self.TutorialsLabel.setObjectName("TutorialsLabel")
        self.TutorialsButton.addWidget(self.TutorialsLabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SidebarButtons.addLayout(self.TutorialsButton)
        self.ArticlesButton = QtWidgets.QHBoxLayout()
        self.ArticlesButton.setObjectName("ArticlesButton")
        self.ArticlesButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.ArticlesButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ArticlesButton_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.ArticlesButton_2.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/web.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ArticlesButton_2.setIcon(icon4)
        self.ArticlesButton_2.setIconSize(QtCore.QSize(42, 42))
        self.ArticlesButton_2.setObjectName("ArticlesButton_2")
        self.ArticlesButton.addWidget(self.ArticlesButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ArticlesLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.ArticlesLabel.setFont(font)
        self.ArticlesLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.ArticlesLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"")
        self.ArticlesLabel.setScaledContents(False)
        self.ArticlesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ArticlesLabel.setWordWrap(False)
        self.ArticlesLabel.setIndent(0)
        self.ArticlesLabel.setObjectName("ArticlesLabel")
        self.ArticlesButton.addWidget(self.ArticlesLabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SidebarButtons.addLayout(self.ArticlesButton)
        self.QuizButton = QtWidgets.QHBoxLayout()
        self.QuizButton.setObjectName("QuizButton")
        self.QuizButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.QuizButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.QuizButton_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.QuizButton_2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.QuizButton_2.setIcon(icon5)
        self.QuizButton_2.setIconSize(QtCore.QSize(42, 42))
        self.QuizButton_2.setObjectName("QuizButton_2")
        self.QuizButton.addWidget(self.QuizButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.QuizLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.QuizLabel.setFont(font)
        self.QuizLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.QuizLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"")
        self.QuizLabel.setScaledContents(False)
        self.QuizLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.QuizLabel.setWordWrap(False)
        self.QuizLabel.setIndent(0)
        self.QuizLabel.setObjectName("QuizLabel")
        self.QuizButton.addWidget(self.QuizLabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SidebarButtons.addLayout(self.QuizButton)
        self.MapButton = QtWidgets.QHBoxLayout()
        self.MapButton.setObjectName("MapButton")
        self.MapButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.MapButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MapButton_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.MapButton_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/map.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MapButton_2.setIcon(icon6)
        self.MapButton_2.setIconSize(QtCore.QSize(42, 42))
        self.MapButton_2.setObjectName("MapButton_2")
        self.MapButton.addWidget(self.MapButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.MapLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.MapLabel.setFont(font)
        self.MapLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.MapLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"")
        self.MapLabel.setScaledContents(False)
        self.MapLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MapLabel.setWordWrap(False)
        self.MapLabel.setIndent(0)
        self.MapLabel.setObjectName("MapLabel")
        self.MapButton.addWidget(self.MapLabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SidebarButtons.addLayout(self.MapButton)
        self.StatsButton = QtWidgets.QHBoxLayout()
        self.StatsButton.setObjectName("StatsButton")
        self.StatsButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.StatsButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.StatsButton_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.StatsButton_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/stats.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StatsButton_2.setIcon(icon7)
        self.StatsButton_2.setIconSize(QtCore.QSize(42, 42))
        self.StatsButton_2.setObjectName("StatsButton_2")
        self.StatsButton.addWidget(self.StatsButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.StatsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.StatsLabel.setFont(font)
        self.StatsLabel.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.StatsLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"")
        self.StatsLabel.setScaledContents(False)
        self.StatsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StatsLabel.setWordWrap(False)
        self.StatsLabel.setIndent(0)
        self.StatsLabel.setObjectName("StatsLabel")
        self.StatsButton.addWidget(self.StatsLabel, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.SidebarButtons.addLayout(self.StatsButton)
        self.SidebarIcon = QtWidgets.QLabel(self.Sidebar)
        self.SidebarIcon.setGeometry(QtCore.QRect(37, 24, 221, 48))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SidebarIcon.sizePolicy().hasHeightForWidth())
        self.SidebarIcon.setSizePolicy(sizePolicy)
        self.SidebarIcon.setMaximumSize(QtCore.QSize(400, 88))
        self.SidebarIcon.setAutoFillBackground(False)
        self.SidebarIcon.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.SidebarIcon.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SidebarIcon.setLineWidth(0)
        self.SidebarIcon.setText("")
        self.SidebarIcon.setPixmap(QtGui.QPixmap(":/images/logo.png"))
        self.SidebarIcon.setScaledContents(True)
        self.SidebarIcon.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.SidebarIcon.setWordWrap(False)
        self.SidebarIcon.setIndent(0)
        self.SidebarIcon.setObjectName("SidebarIcon")
        self.BackButton = QtWidgets.QPushButton(self.Sidebar)
        self.BackButton.setGeometry(QtCore.QRect(120, 670, 54, 50))
        self.BackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BackButton.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.BackButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BackButton.setIcon(icon8)
        self.BackButton.setIconSize(QtCore.QSize(42, 42))
        self.BackButton.setObjectName("BackButton")
        self.horizontalLayout.addWidget(self.Sidebar)
        self.ProductDescriptionPage = QtWidgets.QFrame(self.layoutWidget)
        self.ProductDescriptionPage.setEnabled(True)
        self.ProductDescriptionPage.setStyleSheet("")
        self.ProductDescriptionPage.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ProductDescriptionPage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductDescriptionPage.setLineWidth(0)
        self.ProductDescriptionPage.setObjectName("ProductDescriptionPage")
        self.ProductDesc = QtWidgets.QFrame(self.ProductDescriptionPage)
        self.ProductDesc.setEnabled(True)
        self.ProductDesc.setGeometry(QtCore.QRect(40, 30, 851, 671))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProductDesc.sizePolicy().hasHeightForWidth())
        self.ProductDesc.setSizePolicy(sizePolicy)
        self.ProductDesc.setMinimumSize(QtCore.QSize(200, 350))
        self.ProductDesc.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid white;\n"
"background-color: rgb(24, 29, 45);\n"
"")
        self.ProductDesc.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ProductDesc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ProductDesc.setLineWidth(0)
        self.ProductDesc.setMidLineWidth(0)
        self.ProductDesc.setObjectName("ProductDesc")
        self.ProductDescriptionLayout = QtWidgets.QFrame(self.ProductDesc)
        self.ProductDescriptionLayout.setGeometry(QtCore.QRect(11, 16, 831, 646))
        self.ProductDescriptionLayout.setStyleSheet("border: none;\n"
"border-radius: 0;")
        self.ProductDescriptionLayout.setObjectName("ProductDescriptionLayout")
        self.ProductDescLayout = QtWidgets.QVBoxLayout(self.ProductDescriptionLayout)
        self.ProductDescLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.ProductDescLayout.setSpacing(3)
        self.ProductDescLayout.setObjectName("ProductDescLayout")
        self.ProductImage = QtWidgets.QLabel(self.ProductDescriptionLayout)
        self.ProductImage.setMinimumSize(QtCore.QSize(200, 250))
        self.ProductImage.setMaximumSize(QtCore.QSize(200, 250))
        self.ProductImage.setStyleSheet("border: none")
        self.ProductImage.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ProductImage.setText("")
        self.ProductImage.setPixmap(QtGui.QPixmap(":/images/faceCream.png"))
        self.ProductImage.setScaledContents(True)
        self.ProductImage.setObjectName("ProductImage")
        self.ProductDescLayout.addWidget(self.ProductImage, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ProductTitle = QtWidgets.QLabel(self.ProductDescriptionLayout)
        self.ProductTitle.setMinimumSize(QtCore.QSize(600, 80))
        self.ProductTitle.setMaximumSize(QtCore.QSize(600, 40))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(16)
        self.ProductTitle.setFont(font)
        self.ProductTitle.setStyleSheet("border: none;\n"
"border-radius: 0 0;\n"
"border-top: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.ProductTitle.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ProductTitle.setScaledContents(False)
        self.ProductTitle.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.ProductTitle.setWordWrap(True)
        self.ProductTitle.setIndent(0)
        self.ProductTitle.setOpenExternalLinks(False)
        self.ProductTitle.setObjectName("ProductTitle")
        self.ProductDescLayout.addWidget(self.ProductTitle, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ProdDescTextFrame = QtWidgets.QFrame(self.ProductDescriptionLayout)
        self.ProdDescTextFrame.setMinimumSize(QtCore.QSize(0, 240))
        self.ProdDescTextFrame.setMaximumSize(QtCore.QSize(16777215, 240))
        self.ProdDescTextFrame.setObjectName("ProdDescTextFrame")
        self.ProdDescTextLayout = QtWidgets.QHBoxLayout(self.ProdDescTextFrame)
        self.ProdDescTextLayout.setContentsMargins(1, -1, -1, -1)
        self.ProdDescTextLayout.setSpacing(6)
        self.ProdDescTextLayout.setObjectName("ProdDescTextLayout")
        self.ProdDescText = QtWidgets.QLabel(self.ProdDescTextFrame)
        self.ProdDescText.setMinimumSize(QtCore.QSize(600, 250))
        self.ProdDescText.setMaximumSize(QtCore.QSize(600, 200))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(11)
        self.ProdDescText.setFont(font)
        self.ProdDescText.setStyleSheet("color: white;\n"
"border: none;\n"
"border-radius: 0;\n"
"border-right: 1px solid white;")
        self.ProdDescText.setAlignment(QtCore.Qt.AlignCenter)
        self.ProdDescText.setWordWrap(True)
        self.ProdDescText.setIndent(0)
        self.ProdDescText.setObjectName("ProdDescText")
        self.ProdDescTextLayout.addWidget(self.ProdDescText, 0, QtCore.Qt.AlignVCenter)
        self.ProdPrice = QtWidgets.QLabel(self.ProdDescTextFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProdPrice.sizePolicy().hasHeightForWidth())
        self.ProdPrice.setSizePolicy(sizePolicy)
        self.ProdPrice.setMinimumSize(QtCore.QSize(60, 60))
        self.ProdPrice.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(13)
        self.ProdPrice.setFont(font)
        self.ProdPrice.setStyleSheet("border-radius:30px 30px;\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(225, 160, 103);")
        self.ProdPrice.setFrameShadow(QtWidgets.QFrame.Plain)
        self.ProdPrice.setScaledContents(False)
        self.ProdPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.ProdPrice.setWordWrap(False)
        self.ProdPrice.setIndent(0)
        self.ProdPrice.setObjectName("ProdPrice")
        self.ProdDescTextLayout.addWidget(self.ProdPrice)
        self.ProductDescLayout.addWidget(self.ProdDescTextFrame)
        self.ProdActionsLayout = QtWidgets.QHBoxLayout()
        self.ProdActionsLayout.setContentsMargins(-1, 17, -1, -1)
        self.ProdActionsLayout.setSpacing(9)
        self.ProdActionsLayout.setObjectName("ProdActionsLayout")
        self.ProdBackButton = QtWidgets.QPushButton(self.ProductDescriptionLayout)
        self.ProdBackButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProdBackButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-radius: 0;")
        self.ProdBackButton.setText("")
        self.ProdBackButton.setIcon(icon8)
        self.ProdBackButton.setIconSize(QtCore.QSize(42, 42))
        self.ProdBackButton.setObjectName("ProdBackButton")
        self.ProdActionsLayout.addWidget(self.ProdBackButton)
        self.ProdLinkButton = QtWidgets.QPushButton(self.ProductDescriptionLayout)
        self.ProdLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProdLinkButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-radius: 0;")
        self.ProdLinkButton.setText("")
        self.ProdLinkButton.setIcon(icon8)
        self.ProdLinkButton.setIconSize(QtCore.QSize(42, 42))
        self.ProdLinkButton.setObjectName("ProdLinkButton")
        self.ProdActionsLayout.addWidget(self.ProdLinkButton, 0, QtCore.Qt.AlignHCenter)
        self.ProdFavButton = QtWidgets.QPushButton(self.ProductDescriptionLayout)
        self.ProdFavButton.setEnabled(True)
        self.ProdFavButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ProdFavButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-radius: 0;")
        self.ProdFavButton.setText("")
        self.ProdFavButton.setIcon(icon8)
        self.ProdFavButton.setIconSize(QtCore.QSize(42, 42))
        self.ProdFavButton.setObjectName("ProdFavButton")
        self.ProdActionsLayout.addWidget(self.ProdFavButton, 0, QtCore.Qt.AlignHCenter)
        self.ProductDescLayout.addLayout(self.ProdActionsLayout)
        self.horizontalLayout.addWidget(self.ProductDescriptionPage)
        mainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Face AI"))
        self.HomeLabel_18.setText(_translate("mainWindow", "HOME"))
        self.FaceAILabel.setText(_translate("mainWindow", "FACE SCAN"))
        self.ProductLabel.setText(_translate("mainWindow", "PRODUCTS"))
        self.TutorialsLabel.setText(_translate("mainWindow", "TUTORIALS"))
        self.ArticlesLabel.setText(_translate("mainWindow", "ARTICLES"))
        self.QuizLabel.setText(_translate("mainWindow", "QUIZ"))
        self.MapLabel.setText(_translate("mainWindow", "HELP MAP"))
        self.StatsLabel.setText(_translate("mainWindow", "STATS"))
        self.ProductTitle.setText(_translate("mainWindow", "Sesderma C-VitSesderma C-VitSesderma C-Vit"))
        self.ProdDescText.setText(_translate("mainWindow", "The unscented toner is the essential oil-free version of the original toner. The irritation-free natural essential oils were removed from the original toner to accommodate customers who prefer non-scented products."))
        self.ProdPrice.setText(_translate("mainWindow", "6$"))
import Assets_rc
