import tweepy as tw


class TwitterApi():


    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):

        auth = tw.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tw.API(auth, wait_on_rate_limit=True)

    def last_tweets(self, userID):
        tweets_ext = self.api.user_timeline(userID)

        return [t.text for t in tweets_ext]
