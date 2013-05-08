import twitter

request_token_URL = "https://api.twitter.com/oauth/request_token"
authorize_URL = "https://api.twitter.com/oauth/authorize"
access_token_URL = "https://api.twitter.com/oauth/access_token"

def twitter_login:
	api = twitter.Api()
	
