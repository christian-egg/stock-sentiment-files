import datetime
from datetime import timedelta
from datetime import timezone
import tweepy




API_KEY = "sVXiQKBJP7PnZTlihbigp70pK"
TOKEN_SECRET = "5mBqfX43Utio4rocfLt5oZiOI3WkZE7oEyuKoiQcHJpnNTKCFh"
ACCESS_TOKEN = "1506026300527546368-g8IHal1UhJwpS2q3pvF5lub3Yt70cA"
ACCESS_TOKEN_SECRET = "KaVduS3estbEIGBYEmvIvght3HZDKMpG39eKFSYvZlz24"
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAAIfyaQEAAAAAPlui3vZivPBWFSTuhwt%2F2ROsEdA%3DaxTAohTu5pw7exnBjKgpasnvPxjADUZuDI17Bd4dbA2QSEYK3S"

client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Duration is how far back we're checking as a timedelta
def SearchRecentTweets(query, duration=None):
    tweets = None
    if duration is not None:
        tweets = client.search_recent_tweets(query=query, start_time=(datetime.datetime.now() - duration), max_results = 10)
    else:
        tweets = client.search_recent_tweets(query=query, max_results=10)
    
    result = []
    if (tweets.data != None and len(tweets) != 0):
        for tweet in tweets.data:
            obj = {}
            obj["id"] = tweet.id
            obj["text"] = tweet.text
            result.append(obj)
    
    return result



print(SearchRecentTweets("Tesla", timedelta(days=2))[1]["text"])
print(SearchRecentTweets("Tesla OR Elon Musk OR TSLA", timedelta(days=2))[1]["text"])