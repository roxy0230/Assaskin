from PyQt5 import QtCore


class QuizController(object):
    def __init__(self, addQuizResultToUser, userPageController, getUser):
        self.addQuizResultToUser = addQuizResultToUser
        self.userPageController = userPageController
        self.getUser = getUser
        self.questions = [
            'After cleansing, even if you do not put anything on, it does not feel tight.',
            'If you wipe your face with a tissue, you can see oil on your tissue.',
            'When you do not have makeup on, you can see your pores.',
            'You use oil paper at least 3 times a day.',
            'Your makeup does not last a long time, so you have to retouch every 2 hours.',
            'Your T-Zone is always shinny.',
            'If you use moisturizing cream or pack, you break out more.',
            'If you use light gel type products rather than oily ones.',
            'If you have a lot of black and white heads around your nose.',
            'Even if you wash your hair everyday, your head itches and you have dandruff.',
            'Rather than wrinkles or dead skin, you can see the oiliness of your skin first.',
            'If you do not wash your hair even for a day, it gets oily.'
        ]
        self.answers = []
        self.currentQuestionIndex = 1
        self.yesButton = None
        self.noButton = None

    def resetQuiz(self):
        self.answers = []
        self.currentQuestionIndex = 1

    def setUpQuestion(self, counterElement, questionElement, answer, yesButton, noButton, quizTitle, quizText, comboBox, changeFilter, **kwargs):
        currentIndex = self.currentQuestionIndex
        if "isFirstSetUp" not in kwargs:
            self.registerAnswer(answer, counterElement, questionElement, yesButton, noButton, quizTitle, quizText, comboBox, changeFilter)
        else:
            yesButton.setVisible(True)
            noButton.setVisible(True)

        _translate = QtCore.QCoreApplication.translate
        if currentIndex != 12:
            counterElement.setText(
                _translate("mainWindow", "Question " + str(self.currentQuestionIndex) + " out of 12"))
            questionElement.setText(_translate("mainWindow", self.questions[self.currentQuestionIndex - 1]))

    def registerAnswer(self, answer, counterElement, questionElement, yesButton, noButton, quizTitle, quizText, comboBox, changeFilter):
        _translate = QtCore.QCoreApplication.translate
        self.answers.append({'questionId': self.currentQuestionIndex, 'answer': answer})
        self.currentQuestionIndex += 1
        if self.currentQuestionIndex > 12:
            yesButton.setVisible(False)
            noButton.setVisible(False)
            yesCount = 0
            result = ''
            for answer in self.answers:
                if answer.get('answer'):
                    yesCount += 1
            if 0 <= yesCount <= 4:
                result = 'Dry Skin'
            if 5 <= yesCount <= 8:
                result = 'Normal Skin'
            if 9 <= yesCount <= 12:
                result = 'Oily Skin'
            counterElement.setText(_translate("mainWindow", "Your skin type is: "))
            questionElement.setText(_translate("mainWindow", result))
            comboBox.setVisible(True)
            self.addQuizResultToUser(result)
            self.userPageController.setQuizResult(quizTitle, quizText, self.getUser(), comboBox, changeFilter)
            self.resetQuiz()
