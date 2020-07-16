class Product(object):

    def __init__(self, id, name, description, imageURL, price, link, skinType):
        self.id = id
        self.name = name
        self.description = description
        self.imageURL = imageURL
        self.price = price
        self.link = link
        self.skinType = skinType

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getImageURL(self):
        return self.imageURL

    def getPrice(self):
        return self.price

    def getLink(self):
        return self.link

    def getSkinType(self):
        return self.skinType

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setDescription(self, description):
        self.description = description

    def setImageURL(self, imageURL):
        self.imageURL = imageURL

    def setPrice(self, price):
        self.price = price

    def setLink(self, link):
        self.link = link

    def setSkinType(self, skinType):
        self.skinType = skinType

    def __str__(self):
        return str(self.id) + " " + str(self.name) + " " + str(self.description)
