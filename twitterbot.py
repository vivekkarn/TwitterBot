import tweepy
import time


class TwitterBot(object):
    def __init__(self, count, SECRECT_KEY, SECRET_TOKEN, ACCESS_KEY, ACESS_TOKEN):
        self.count = count
        auth = tweepy.OAuthHandler(SECRECT_KEY, SECRET_TOKEN)
        auth.set_access_token(ACCESS_KEY, ACESS_TOKEN)
        self.api = tweepy.API(auth, wait_on_rate_limit=True,
                              wait_on_rate_limit_notify=True)
        user = self.api.me()
        print("Checking your username ", user.screen_name)

    def follow_followers(self):
        api = self.api
        for follower in tweepy.Cursor(api.followers).items(self.count):
            try:
                if not follower.following:
                    follower.follow()
                    print("Follower followed is ", follower.name)
                time.sleep(10)
                print("Follower checked is ", follower.name)
            except tweepy.TweepError as e:
                print(e.reason)
                break

    def like_tweets(self, search_query):
        api = self.api
        file = open('tweet.json', 'w+')
        for tweet in tweepy.Cursor(api.search, search_query).items(self.count):
            try:
                if not tweet.favorited:
                    print("Tweek Liked")
                    tweet.favorite()
                time.sleep(10)

            except tweepy.TweepError as e:
                if e.api_code == 139 or e.api_code == 144:
                    print("Tweet already liked")
                else:
                    print(e.reason)
                    break

    def follow_from_tweets(self, search_query):
        api = self.api
        file = open('tweet.json', 'w+')
        for tweet in tweepy.Cursor(api.search, search_query).items(self.count):
            try:
                if not tweet.user.following:
                    tweet.user.follow()
                    print("Followed from tweet is ", tweet.user.name)

                time.sleep(10)
            except tweepy.TweepError as e:
                if e.api_code == 139 or e.api_code == 144:
                    print("Tweet already liked")
                else:
                    print(e.reason)
                    break
