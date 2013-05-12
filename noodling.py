import twitter
import config
import ttp

request_token_URL = "https://api.twitter.com/oauth/request_token"
authorize_URL = "https://api.twitter.com/oauth/authorize"
access_token_URL = "https://api.twitter.com/oauth/access_token"

PAGE_SIZE = 20

api = twitter.Api()

favs = []

def twitter_login():
	api = twitter.Api(consumer_key =      config.TWITTER_CONSUMER_KEY,
					consumer_secret =     config.TWITTER_CONSUMER_SECRET, 
					access_token_key =	  config.TWITTER_CONSUMER_KEY, 
					access_token_secret = config.TWITTER_CONSUMER_SECRET)
	print 'Logged in'

def get_all_favs(user):
	
	theUser = api.GetUser(user)
	maxPage = theUser.favourites_count / PAGE_SIZE + 1
	favs = []
	for p in range(maxPage):		
		favs.append( api.GetFavorites(user, page = p) )
		
	print len(favs)

def get_urls(tweet):
	p = ttp.Parser
	result = p.parse(tweet.AsDict()['text'])
	return result.urls

def main():
	twitter_login()
	
if __name__ == "__main__":
	main()


