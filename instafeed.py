import instagram
from instagram.client import InstagramAPI

access_token = "6032acedc92948d9ae6454b88c69fd4c"
client_secret = "92d89e2dc3eb43a3a758efed7bf25877"

api = InstagramAPI(access_token=access_token, client_secret=client_secret)
recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
for media in recent_media:
    print(media.caption.text)
