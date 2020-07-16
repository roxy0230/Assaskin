# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
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
        self.scrollArea = QtWidgets.QScrollArea(self.FirstScreen)
        self.scrollArea.setGeometry(QtCore.QRect(20, 30, 881, 671))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.scrollArea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, -82, 864, 835))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 52, -1, -1)
        self.gridLayout.setVerticalSpacing(74)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(200, 350))
        self.frame_2.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid white;\n"
"background-color: rgb(24, 29, 45);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setLineWidth(0)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(50, 10, 101, 181))
        self.label_7.setStyleSheet("border: none")
        self.label_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/images/faceOil.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(20, 200, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("border: none;\n"
"border-radius: 0 0;\n"
"border-top: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.label_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_8.setScaledContents(False)
        self.label_8.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_8.setWordWrap(True)
        self.label_8.setIndent(0)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(70, 270, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("border-radius:30px 30px;\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(225, 160, 103);")
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setIndent(0)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(200, 350))
        self.frame.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid white;\n"
"background-color: rgb(24, 29, 45);\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 181))
        self.label.setStyleSheet("border: none")
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/faceCream.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: none;\n"
"border-radius: 0 0;\n"
"border-top: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(True)
        self.label_2.setIndent(0)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 270, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border-radius:30px 30px;\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(225, 160, 103);")
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setIndent(0)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(200, 350))
        self.frame_3.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid white;\n"
"background-color: rgb(24, 29, 45);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setLineWidth(0)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(10, 10, 181, 181))
        self.label_10.setStyleSheet("border: none")
        self.label_10.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap(":/images/faceCream.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(20, 200, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border: none;\n"
"border-radius: 0 0;\n"
"border-top: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_11.setScaledContents(False)
        self.label_11.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_11.setWordWrap(True)
        self.label_11.setIndent(0)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(70, 270, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border-radius:30px 30px;\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(225, 160, 103);")
        self.label_12.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_12.setScaledContents(False)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(False)
        self.label_12.setIndent(0)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.frame_3, 1, 1, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 350))
        self.frame_4.setStyleSheet("border-radius: 15px;\n"
"border: 1px solid white;\n"
"background-color: rgb(24, 29, 45);\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(0)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setGeometry(QtCore.QRect(10, 10, 181, 181))
        self.label_13.setStyleSheet("border: none")
        self.label_13.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap(":/images/faceCream.png"))
        self.label_13.setScaledContents(True)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setGeometry(QtCore.QRect(20, 200, 161, 141))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border: none;\n"
"border-radius: 0 0;\n"
"border-top: 1px solid white;\n"
"color: rgb(255, 255, 255);")
        self.label_14.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_14.setScaledContents(False)
        self.label_14.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_14.setWordWrap(True)
        self.label_14.setIndent(0)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setGeometry(QtCore.QRect(70, 270, 60, 60))
        font = QtGui.QFont()
        font.setFamily("Futurist Fixed-width")
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border-radius:30px 30px;\n"
"color: rgb(255, 255, 255);\n"
"border: none;\n"
"background-color: rgb(225, 160, 103);")
        self.label_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setWordWrap(False)
        self.label_15.setIndent(0)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
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
        self.label_8.setText(_translate("mainWindow", "Wrinkle Coenzyme Q10"))
        self.label_9.setText(_translate("mainWindow", "4$"))
        self.label_2.setText(_translate("mainWindow", "Sesderma C-Vit"))
        self.label_3.setText(_translate("mainWindow", "6$"))
        self.label_11.setText(_translate("mainWindow", "Sesderma C-Vit"))
        self.label_12.setText(_translate("mainWindow", "6$"))
        self.label_14.setText(_translate("mainWindow", "Sesderma C-Vit"))
        self.label_15.setText(_translate("mainWindow", "6$"))
