from PyQt5 import QtCore, QtWebEngineWidgets, QtWebChannel, QtNetwork

from Assets import firebaseConfig

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="initial-scale=1.0, user-scalable=no"/>
    <style type="text/css">
        html {
            height: 100%;
         zo   width: 100%;
        }
        body {
            height: 100%;
            margin: 0;
            padding: 0
            width: 100%;
        }
        #video {
        height: 100%;
        margin: 0;
        padding: 0
        width: 100%;
        }
    </style>
    <script type="text/javascript" src="qrc:///qtwebchannel/qwebchannel.js"></script>
    <script type="text/javascript">
    function reload(link) {
    document.getElementById('video').src = 'https://www.youtube.com/embed/' + link;
    }
    </script>
</head>
<body>
<iframe frameborder="0"  width="560" height="315" id="video" style="width:100%; height:100%;"
src="https://www.youtube.com/embed/LINK">
</iframe>
</body>
</html>
'''

class YoutubePlayer(QtWebEngineWidgets.QWebEngineView):
    def __init__(self, parent=None, link=''):
        super(YoutubePlayer, self).__init__(parent)
        channel = QtWebChannel.QWebChannel(self)
        self.page().setWebChannel(channel)
        channel.registerObject("YoutubePlayer", self)
        html = HTML.replace("LINK", link)
        self.setHtml(html)
        self._manager = QtNetwork.QNetworkAccessManager(self)

    def runScript(self, script, callback=None):
        if callback is None:
            self.page().runJavaScript(script)
        else:
            self.page().runJavaScript(script, callback)

    def reloadVideo(self, link):
        html = HTML.replace("LINK", link)
        self.setHtml(html)

