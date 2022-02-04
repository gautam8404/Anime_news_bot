
# Reddit Kang Bot

A Bot which uses official Reddit api to get any new post of a specific subreddit and automatically posts to a specified channel
<br></br>
 <p align='center'>
  <a href="https://www.python.org/" alt="made-with-python"> <img src="https://img.shields.io/badge/Made%20with-Python-00ead3.svg?style=flat-square&logo=python&logoColor=00ead3&color=00ead3" /> </a>
  <a href="https://github.com/MiyukiKun/Anime_Gallery_Bot/" alt="Maintenance"> <img src="https://img.shields.io/badge/Maintained%3F-Yes-green.svg?style=flat-square&logo=serverless&logoColor=00ead3&color=00ead3" /> </a>
</p>
<br></br>

# Table of Content
- [Anime News Bot](#reddit-kang-bot)
- [Table of Content](#table-of-content)
- [Features](#features)
- [Environment Variables](#environment-variables)
- [Deployment](#deployment)
  - [Heroku](#heroku)
- [Known Issues](#known-issues)
- [Creator](#creator)

# Features

- Bot is just one time setup you can simply deploy and it will run without any more input
- Can choose any channel to post to or any subreddit to post from

# Environment Variables

To run this project, you will need to add the following environment variables to your .env file

- `API_ID` You Can Get it from [here](https://my.telegram.org/) .

- `API_HASH` You Can Get it form [here](https://my.telegram.org/) .

- `BOT_TOKEN` Search [@BotFather](https://t.me/botfather) in telegram.

- `REDDIT_PERSONAL_USE_SCRIPT` Go [here](https://github.com/reddit-archive/reddit/wiki/OAuth2) to know how to get it.

- `REDDIT_SECRET` you will get this in same process as above

- `AGENT` you will get this in same process as above

- `SUBREDDIT` Target subreddit you want to post from (dont incluce `r/` simply write memes instead of r/memes for example)

- `APPROVAL_CHANNEL_ID` approval channel username(without the @) or if its private then use channel id (Goes without saying but add the bot to the cahannel and make admin)

- `MAIN_CHANNEL_ID` main channel where post will be posted after approval

- `FLAIR` if you want to sort post of the target subreddit by flair, if you want all post then simply use `None`

- `TWITTER_API_KEY` get it from [here](https://developer.twitter.com/en/docs/twitter-api), NOTE: you need elevated access to use this bot

- `TWITTER_API_SECRET` mentioned above

- `ACCESS_TOKEN` mentioned above

- `ACCESS_SECRET` mentioned above

# Deployment 

## Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/gautam8404/Anime_news_bot)

# Known Issues

- Sometimes posts may get repeated if the newest post gets deleted on reddit or the bot restarts (I dont know how to fix it).
  
# Creator

- [Gautam8404](https://github.com/Gautam8404

