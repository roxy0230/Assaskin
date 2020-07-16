class TutorialsRep(object):

    def __init__(self):
        self.tutorials = []

    def add(self, tutorial):
        self.tutorials.append(tutorial)

    def delete(self, tutorial):
        self.tutorials.remove(tutorial)

    def change(self, tutorial):
        for i in range(0, len(self.tutorials)):
            if self.tutorials[i].getIds() == tutorial.getIds():
                self.tutorials[i] = tutorial

    def getRep(self):
        return self.tutorials
