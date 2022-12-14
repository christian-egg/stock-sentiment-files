import datetime
from datetime import timedelta
from datetime import timezone
import tweepy
import pandas
import re
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
TOKEN_SECRET = os.getenv('TOKEN_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

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

def SearchTimePeriodTweets(query, start_time, end_time):
    tweets = client.search_recent_tweets(query=query, start_time=start_time, end_time=end_time, max_results=10)
    
    result = []
    if (tweets.data != None and len(tweets) != 0):
        for tweet in tweets.data:
            result.append((tweet.id, tweet.text))
    
    return result

def CleanTweets(tweets):
    for tweet in tweets:
        tweet["text"] = re.sub(" +", " ", re.sub("#[A-Za-z0-9_]+", "", re.sub("@[A-Za-z0-9_]+", "", tweet["text"])))
    return tweets

#print(SearchRecentTweets("Tesla", timedelta(days=2))[1][1])
#print(SearchRecentTweets("Tesla OR Elon Musk OR TSLA", timedelta(days=2))[1][1])
#print(SearchRecentTweets("#Tesla", timedelta(days=2))[1][1])
#print(SearchRecentTweets("#Tesla OR #ElonMusk", datetime.datetime(day=1, month=3, year=2022), datetime.datetime(day=1, month=3, year=2022))
#print(SearchTimePeriodTweets("#Tesla OR #ElonMusk", datetime.datetime(day=1, month=3, year=2022), datetime.datetime(day=1, month=3, year=2022)))
data = SearchRecentTweets("#Tesla", timedelta(days=2))
data = CleanTweets(data)
df = pandas.DataFrame.from_records(data)

df.to_csv("./data.csv")
w