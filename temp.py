# import requests
# from bs4 import BeautifulSoup


# url = "https://www.livechart.me/feeds/headlines"
# response = requests.get(url)
# response_html = response.content
# soup = BeautifulSoup(response_html, features='xml')
# title = soup.find('item').title.contents
# link = soup.find('item').link.contents
# thumb = soup.find('media:thumbnail')["url"]
# img_data = requests.get(thumb).content
# with open('thumb.jpg', 'wb') as handle:
#     response = requests.get(thumb, stream=True)

#     if not response.ok:
#         print(response)

#     for block in response.iter_content(1024):
#         if not block:
#             break

#         handle.write(block)
# print(thumb)

# def test(source):
#     with open(f"{source}_link_log.txt", "r") as f:
#         file = f.read()
#     return file

# a = test("reddit")
from config import api
import tweepy
id = 1486353247677960203
# print(a)

status = api.get_status(id)

media = status.entities['media']
for image in media:
    media_url = image['media_url']

print(media_url)