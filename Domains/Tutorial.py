class Tutorial(object):

    def __init__(self, id, title, url, imageUrl):
        self.id = id
        self.title = title
        self.url = url
        self.imageUrl = imageUrl

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getUrl(self):
        return self.url

    def getImageUrl(self):
        return self.imageUrl

    def setId(self, id):
        self.id = id

    def setTitle(self, title):
        self.title = title

    def setUrl(self, url):
        self.url = url

    def setImageUrl(self, imageUrl):
        self.imageUrl = imageUrl

    def __str__(self):
        return str(self.id) + " " + str(self.title) + " " + str(self.url)
