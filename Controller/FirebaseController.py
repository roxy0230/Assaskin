import firebase_admin
from firebase_admin import credentials, firestore
import pyrebase

from Assets import firebaseConfig


class FirebaseController(object):
    def __init__(self):
        cred = credentials.Certificate("Assets/firebaseKey.json")
        firebase_admin.initialize_app(cred)
        self.pyrebase = pyrebase.initialize_app(firebaseConfig.firebaseConfig)
        self.db = firestore.client()
        self.productDocs = None
        self.articleDocs = None
        self.tutorialDocs = None
        self.userDocs = None
        self.auth = None

    def setup(self):
        self.productDocs = self.db.collection(u'products').stream()
        self.articleDocs = self.db.collection(u'articles').stream()
        self.tutorialDocs = self.db.collection(u'tutorials').stream()
        self.userDocs = self.db.collection(u'users')
        self.auth = self.pyrebase.auth()
