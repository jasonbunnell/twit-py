import tweepy
from textblob import TextBlob

consumer_key = 'lOQqd21ewxvS4AOniUPOIQ'
consumer_secret = 'euI5dSqInMaGy1z3YWrX0cPTR9BxwXaVwmnsFI2N0kc'

access_token = '14446071-yoW0YpbBqbNVfenvPvh9huq2uMest0bg57PdRhvHX'
access_token_secret = 'eT6a74X2OjYRmy4NLZlWkDJccyWCu0VuSqGJQIEvrtLqi'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Dallas')

for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)


## TODO list
# follow user using set hashtag
# vote on speaker vie there user handle