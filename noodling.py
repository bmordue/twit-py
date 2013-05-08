import twitter

consumer_key = "vQDyI23Jsr4Q9bCE1sBAcw"
consumer_secret = "LdlENCjzmmzWrX4xO23Gj68XZ4uITrAhA1VUbxZJUc"
request_token_URL = "https://api.twitter.com/oauth/request_token"
authorize_URL = "https://api.twitter.com/oauth/authorize"
access_token_URL = "https://api.twitter.com/oauth/access_token"

def twitter_login:
	api = twitter.Api()
	
