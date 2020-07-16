class ArticlesRep(object):

    def __init__(self):
        self.articles = []

    def add(self, article):
        self.articles.append(article)

    def delete(self, article):
        self.articles.remove(article)

    def change(self, article):
        for i in range(0, len(self.articles)):
            if self.articles[i].getIds() == article.getIds():
                self.articles[i] = article

    def getRep(self):
        return self.articles
