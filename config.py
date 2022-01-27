import os
from telethon import TelegramClient
import tweepy

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
reddit_personal_use_script = os.environ.get('REDDIT_PERSONAL_USE_SCRIPT')
reddit_secret = os.environ.get('REDDIT_SECRET')
agent = os.environ.get('AGENT')
subreddit = os.environ.get('SUBREDDIT')
channel_id = os.environ.get('APPROVAL_CHANNEL_ID')
main_channel_id = os.environ.get('MAIN_CHANNEL_ID')
flair = os.environ.get('FLAIR')
twitter_api_key = os.environ.get('TWITTER_API_KEY')
twitter_api_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_secret = os.environ.get('ACCESS_SECRET')


auth = tweepy.OAuthHandler(twitter_api_key,twitter_api_secret)
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

