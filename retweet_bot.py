#Retweet Bot
#Adding needed libraries and the file with the API keys
import tweepy as twitter
import keys
import time, datetime

#authentication step
auth = twitter.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.SECRET_ACCESS_TOKEN)
api = twitter.API(auth)

#retweet bot function
def twitter_bot(username, delay):
    #checking the time to compare with the last thing we retweeted
    while True:
        print(f"\n{datetime.datetime.now()}\n")

        #for every tweet from user with the screen_name set in the function call
        #show 1 item every 10 sec
        for tweet in twitter.Cursor(api.user_timeline, screen_name=username, rpp=10).items(1):
            try:
                tweet_id = dict(tweet._json)["id"]
                tweet_text = dict(tweet._json)["text"]

                #print the tweet id and the text on the console
                print("id: " + str(tweet_id))
                print("text: " + str(tweet_text))

                #call the retweet method for the specific tweet_id
                api.retweet(tweet_id)

            except twitter.TweepError as error:
                print(error.reason)

        time.sleep(delay)

#Function call
twitter_bot("@user", 1)
