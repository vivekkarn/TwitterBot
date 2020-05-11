import tweepy
import time
from accesskeys import *
from twitterbot import TwitterBot


# Twitter restricts number of bot activites by 1000 per day as of now.
number_of_iterations = 100

# Your query to search and like the terms
query = 'doctors'

# The SECRECT_KEY, SECRET_TOKEN, ACCESS_KEY, ACESS_TOKEN
# is available at https://developer.twitter.com/en/apps

bot = TwitterBot(number_of_iterations, SECRECT_KEY,
                 SECRET_TOKEN, ACCESS_KEY, ACESS_TOKEN)

# Followback all your followers if you are not already following them
bot.follow_followers()

# Like 100 tweets from the provided query
bot.like_tweets(query)
