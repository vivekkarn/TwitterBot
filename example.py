import tweepy
import time
from accesskeys import *
from twitterbot import TwitterBot


# Twitter restricts number of bot activites by 1000 per day as of now.
number_of_iterations = 100

# Your query to search and like the terms
query = 'doctors'

bot = TwitterBot(number_of_iterations, SECRECT_KEY,
                 SECRET_TOKEN, ACCESS_KEY, ACESS_TOKEN)
bot.follow_followers()
bot.like_tweets(query)
