# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstWindow.ui'
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
        self.FirstScreen = QtWidgets.QFrame(self.layoutWidget)
        self.FirstScreen.setEnabled(True)
        self.FirstScreen.setStyleSheet("")
        self.FirstScreen.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.FirstScreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FirstScreen.setLineWidth(0)
        self.FirstScreen.setObjectName("FirstScreen")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.FirstScreen)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 931, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.LogoLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.LogoLayout.setContentsMargins(0, 0, 0, 0)
        self.LogoLayout.setSpacing(0)
        self.LogoLayout.setObjectName("LogoLayout")
        self.ImageLogo = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.ImageLogo.setMaximumSize(QtCore.QSize(170, 245))
        self.ImageLogo.setText("")
        self.ImageLogo.setPixmap(QtGui.QPixmap(":/images/C:/Users/Sebastian/PycharmProjects/FaceAI/Assets/Branding/faceUUI.png"))
        self.ImageLogo.setScaledContents(True)
        self.ImageLogo.setIndent(0)
        self.ImageLogo.setObjectName("ImageLogo")
        self.LogoLayout.addWidget(self.ImageLogo, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.TextLogo = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TextLogo.sizePolicy().hasHeightForWidth())
        self.TextLogo.setSizePolicy(sizePolicy)
        self.TextLogo.setMaximumSize(QtCore.QSize(270, 59))
        self.TextLogo.setAutoFillBackground(False)
        self.TextLogo.setText("")
        self.TextLogo.setPixmap(QtGui.QPixmap(":/images/C:/Users/Sebastian/PycharmProjects/FaceAI/Assets/Branding/logo.png"))
        self.TextLogo.setScaledContents(True)
        self.TextLogo.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.TextLogo.setWordWrap(False)
        self.TextLogo.setIndent(0)
        self.TextLogo.setObjectName("TextLogo")
        self.LogoLayout.addWidget(self.TextLogo, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.FirstScreen)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 380, 931, 341))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.LogInRegisterLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.LogInRegisterLayout.setContentsMargins(0, 0, 0, 0)
        self.LogInRegisterLayout.setSpacing(0)
        self.LogInRegisterLayout.setObjectName("LogInRegisterLayout")
        self.LogInLayout = QtWidgets.QVBoxLayout()
        self.LogInLayout.setContentsMargins(29, 0, 29, 0)
        self.LogInLayout.setSpacing(41)
        self.LogInLayout.setObjectName("LogInLayout")
        self.LogInLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(15)
        self.LogInLabel.setFont(font)
        self.LogInLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LogInLabel.setAutoFillBackground(False)
        self.LogInLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;")
        self.LogInLabel.setLineWidth(1)
        self.LogInLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LogInLabel.setWordWrap(False)
        self.LogInLabel.setObjectName("LogInLabel")
        self.LogInLayout.addWidget(self.LogInLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.UserNameLogInLayout = QtWidgets.QHBoxLayout()
        self.UserNameLogInLayout.setSpacing(23)
        self.UserNameLogInLayout.setObjectName("UserNameLogInLayout")
        self.UserLogInLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.UserLogInLabel.setFont(font)
        self.UserLogInLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;")
        self.UserLogInLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UserLogInLabel.setObjectName("UserLogInLabel")
        self.UserNameLogInLayout.addWidget(self.UserLogInLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.UserLogInEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.UserLogInEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"font-family: \"Futurist Fixed-width\"")
        self.UserLogInEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.UserLogInEdit.setObjectName("UserLogInEdit")
        self.UserNameLogInLayout.addWidget(self.UserLogInEdit)
        self.LogInLayout.addLayout(self.UserNameLogInLayout)
        self.PasswordLogInLayout = QtWidgets.QHBoxLayout()
        self.PasswordLogInLayout.setSpacing(36)
        self.PasswordLogInLayout.setObjectName("PasswordLogInLayout")
        self.PasswordLogInLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.PasswordLogInLabel.setFont(font)
        self.PasswordLogInLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;")
        self.PasswordLogInLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PasswordLogInLabel.setObjectName("PasswordLogInLabel")
        self.PasswordLogInLayout.addWidget(self.PasswordLogInLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PasswordLogInEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.PasswordLogInEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"font-family: \"Futurist Fixed-width\"")
        self.PasswordLogInEdit.setInputMask("")
        self.PasswordLogInEdit.setText("")
        self.PasswordLogInEdit.setFrame(True)
        self.PasswordLogInEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordLogInEdit.setObjectName("PasswordLogInEdit")
        self.PasswordLogInLayout.addWidget(self.PasswordLogInEdit)
        self.LogInLayout.addLayout(self.PasswordLogInLayout)
        self.SubmitButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubmitButton.sizePolicy().hasHeightForWidth())
        self.SubmitButton.setSizePolicy(sizePolicy)
        self.SubmitButton.setMinimumSize(QtCore.QSize(120, 40))
        self.SubmitButton.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(11)
        self.SubmitButton.setFont(font)
        self.SubmitButton.setStyleSheet("color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.SubmitButton.setAutoDefault(False)
        self.SubmitButton.setDefault(False)
        self.SubmitButton.setFlat(True)
        self.SubmitButton.setObjectName("SubmitButton")
        self.LogInLayout.addWidget(self.SubmitButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.LogInRegisterLayout.addLayout(self.LogInLayout)
        self.divider = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.divider.setMinimumSize(QtCore.QSize(1, 250))
        self.divider.setMaximumSize(QtCore.QSize(1, 250))
        self.divider.setStyleSheet("background-color: white;\n"
"")
        self.divider.setFrameShape(QtWidgets.QFrame.VLine)
        self.divider.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.divider.setObjectName("divider")
        self.LogInRegisterLayout.addWidget(self.divider)
        self.RegisterLayout = QtWidgets.QVBoxLayout()
        self.RegisterLayout.setContentsMargins(29, 0, 29, 0)
        self.RegisterLayout.setSpacing(41)
        self.RegisterLayout.setObjectName("RegisterLayout")
        self.RegisterLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(15)
        self.RegisterLabel.setFont(font)
        self.RegisterLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RegisterLabel.setAutoFillBackground(False)
        self.RegisterLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;")
        self.RegisterLabel.setLineWidth(1)
        self.RegisterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.RegisterLabel.setWordWrap(False)
        self.RegisterLabel.setObjectName("RegisterLabel")
        self.RegisterLayout.addWidget(self.RegisterLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.UserRegisterLayout = QtWidgets.QHBoxLayout()
        self.UserRegisterLayout.setSpacing(23)
        self.UserRegisterLayout.setObjectName("UserRegisterLayout")
        self.UserRegisterLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.UserRegisterLabel.setFont(font)
        self.UserRegisterLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;")
        self.UserRegisterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.UserRegisterLabel.setObjectName("UserRegisterLabel")
        self.UserRegisterLayout.addWidget(self.UserRegisterLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.UserRegisterEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.UserRegisterEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"font-family: \"Futurist Fixed-width\"")
        self.UserRegisterEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.UserRegisterEdit.setObjectName("UserRegisterEdit")
        self.UserRegisterLayout.addWidget(self.UserRegisterEdit)
        self.RegisterLayout.addLayout(self.UserRegisterLayout)
        self.EmailLayout = QtWidgets.QHBoxLayout()
        self.EmailLayout.setSpacing(68)
        self.EmailLayout.setObjectName("EmailLayout")
        self.EmailLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.EmailLabel.setFont(font)
        self.EmailLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;")
        self.EmailLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EmailLabel.setObjectName("EmailLabel")
        self.EmailLayout.addWidget(self.EmailLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.EmailEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.EmailEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"font-family: \"Futurist Fixed-width\"")
        self.EmailEdit.setInputMethodHints(QtCore.Qt.ImhEmailCharactersOnly)
        self.EmailEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.EmailEdit.setObjectName("EmailEdit")
        self.EmailLayout.addWidget(self.EmailEdit)
        self.RegisterLayout.addLayout(self.EmailLayout)
        self.PasswordRegisterLayout = QtWidgets.QHBoxLayout()
        self.PasswordRegisterLayout.setSpacing(36)
        self.PasswordRegisterLayout.setObjectName("PasswordRegisterLayout")
        self.PasswordRegisterLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.PasswordRegisterLabel.setFont(font)
        self.PasswordRegisterLabel.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;")
        self.PasswordRegisterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PasswordRegisterLabel.setObjectName("PasswordRegisterLabel")
        self.PasswordRegisterLayout.addWidget(self.PasswordRegisterLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.PasswordRegisterEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.PasswordRegisterEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;\n"
"font-family: \"Futurist Fixed-width\"")
        self.PasswordRegisterEdit.setInputMask("")
        self.PasswordRegisterEdit.setText("")
        self.PasswordRegisterEdit.setFrame(True)
        self.PasswordRegisterEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordRegisterEdit.setObjectName("PasswordRegisterEdit")
        self.PasswordRegisterLayout.addWidget(self.PasswordRegisterEdit)
        self.RegisterLayout.addLayout(self.PasswordRegisterLayout)
        self.JoinButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.JoinButton.sizePolicy().hasHeightForWidth())
        self.JoinButton.setSizePolicy(sizePolicy)
        self.JoinButton.setMinimumSize(QtCore.QSize(120, 40))
        self.JoinButton.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(11)
        self.JoinButton.setFont(font)
        self.JoinButton.setStyleSheet("color: white;\n"
"border: 1px solid white;\n"
"border-radius: 5px;")
        self.JoinButton.setAutoDefault(False)
        self.JoinButton.setDefault(False)
        self.JoinButton.setFlat(True)
        self.JoinButton.setObjectName("JoinButton")
        self.RegisterLayout.addWidget(self.JoinButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.LogInRegisterLayout.addLayout(self.RegisterLayout)
        self.horizontalLayout.addWidget(self.FirstScreen)
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
        self.LogInLabel.setText(_translate("mainWindow", "Log In"))
        self.UserLogInLabel.setText(_translate("mainWindow", "User Name:"))
        self.PasswordLogInLabel.setText(_translate("mainWindow", "Password:"))
        self.SubmitButton.setText(_translate("mainWindow", "Submit"))
        self.RegisterLabel.setText(_translate("mainWindow", "Register"))
        self.UserRegisterLabel.setText(_translate("mainWindow", "User Name:"))
        self.EmailLabel.setText(_translate("mainWindow", "E-mail:"))
        self.PasswordRegisterLabel.setText(_translate("mainWindow", "Password:"))
        self.JoinButton.setText(_translate("mainWindow", "Join Us"))
import Assets_rc