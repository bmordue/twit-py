import twitter
import config

request_token_URL = "https://api.twitter.com/oauth/request_token"
authorize_URL = "https://api.twitter.com/oauth/authorize"
access_token_URL = "https://api.twitter.com/oauth/access_token"

api = twitter.Api()

def twitter_login():
	api = twitter.Api(consumer_key =      config.TWITTER_CONSUMER_KEY,
					consumer_secret =     config.TWITTER_CONSUMER_SECRET, 
					access_token_key =	  config.TWITTER_CONSUMER_KEY, 
					access_token_secret = config.TWITTER_CONSUMER_SECRET)
	print 'Logged in'


def main():
	twitter_login()
	
if __name__ == "__main__":
	main()


