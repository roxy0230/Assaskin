from apiclient import discovery

from Assets import firebaseConfig


class YoutubeAPI(object):
    def __init__(self):
        self.youtube = discovery.build('youtube', 'v3', developerKey=firebaseConfig.firebaseConfig.get("apiKey"))

    def getVideoThumbnail(self, url):
        request = self.youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=url
        )
        response = request.execute()
        return response.get('items')[0].get('snippet').get('thumbnails').get('medium').get('url')
