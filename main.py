from bs4 import BeautifulSoup
import requests
from telethon import events, Button
from config import bot, channel_id , api , reddit_personal_use_script, reddit_secret, agent, subreddit, channel_id, flair, main_channel_id
import asyncio
import yt_dlp
import shutil
import subprocess
import os
from telethon.tl.types import DocumentAttributeVideo
import asyncpraw
reddit = asyncpraw.Reddit(client_id = reddit_personal_use_script, client_secret = reddit_secret, user_agent = agent)

channel_id = int(channel_id)


def delete_files():
    folder = 'videos'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

ydl_opts = {
    'writethumbnail': True,
    'format': '136+140''398+140' '22'  'bestvideo[ext!=webm]+bestaudio[ext!=webm]/best[ext!=webm]',
    'outtmpl': 'videos/youtube.mp4'
}

def dwl_vid(url):
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def check_thumb():
    if os.path.isfile("videos/youtube.webp"):
        os.system("ffmpeg -i videos/youtube.webp videos/thumb.png")
        # return "videos/thumb.png"
    elif os.path.isfile("videos/youtube.png"):
        os.system("ffmpeg -i videos/youtube.png videos/thumb.png")
    elif os.path.isfile("videos/youtube.jpg"):
        os.system("ffmpeg -i videos/youtube.jpg videos/thumb.png")
        # return "videos/thumb.png"
    else:
        return None
    
def get_duration():
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", "videos/youtube.mp4"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
    return float(result.stdout)

async def send_message(file,title):
    channel = await bot.get_entity(f"t.me/{channel_id}")
    try:
        await bot.send_message(
        channel, 
        f"{title}\n\n@{channel_id}", 
        file=file,
    )
    except Exception as e:
        print(e)

# channel = bot.get_entity(f"t.me/{channel_id}")

def write_file(url,source):
    with open(f"{source}_link_log.txt","w") as f:
        f.write(url)


def read_file(source):
    with open(f"{source}_link_log.txt", "r") as f:
        file = f.read()
    return file



async def reddit_fetch(last):
    
    channel = await bot.get_entity(channel_id)
    # channel = channel_id
    subred = await reddit.subreddit(subreddit)
    if flair == None:
        new = subred.new(limit = 1)
    else:
        new = subred.search(f'flair:"{flair}"', sort = "new",syntax='lucene', limit=1)
    rev_list = []
    async for i in new:
        rev_list.append([i.url,i.title])
    rev_list.reverse()
    for i in rev_list:
        url = i[0]
        title = i[1]
        split = url.split("/")
        print(url)
        print("from reddit")
        if 'i.redd.it' in split:
            if url != last:
                try:
                    await bot.send_message(
                    channel, 
                    f"{title}\n\n@{main_channel_id}", 
                    file=url,
                    buttons=[Button.inline('approve', b'approve'),Button.inline('reject', b'reject')]
                )
                    write_file(url,"reddit")
                except Exception as e:
                    print(e)
        else:
            if "playlist" in url:
                print("playlist found, cancelling download")
            else:
                word_dict = ["trailer", "Trailer", "pv", "PV", "teaser", "Teaser","visual", "Visual","preview", "Preview", "Announced","announced","project", "Project","op", "OP", "ed", "ED"]
                if url != last:
                    try:
                        delete_files()
                        dwl_vid(url)
                        location = "videos/youtube.mp4"
                        file = location
                        check_thumb()
                        thumbnail = "videos/thumb.png"
                        dur = get_duration()
                        print(dur)
                        dur = int(dur)
                        print(dur)
                        new_title = f"[{title}]({url})"
                        for word in word_dict:
                            if word in title:
                                new_title = title.replace(word, f"[{word}]({url})")
                                break
                        await bot.send_message(
                        channel, 
                        f"{new_title}\n\n@{main_channel_id}", 
                        file=file,
                        thumb=thumbnail,
                        supports_streaming=True,
                        attributes=[DocumentAttributeVideo(
                        duration=dur, 
                        w=1260, 
                        h=720, 
                        supports_streaming=True,
                        )], 
                        buttons=[Button.inline('approve', b'approve'),Button.inline('reject', b'reject')]
                    )

                        print("uploaded")
                        write_file(url,"reddit")
                    except Exception as e:
                        try:
                            new_title = f"[{title}]({url})"
                            for word in word_dict:
                                if word in title:
                                    new_title = title.replace(word, f"[{word}]({url})")
                                    break
                            await bot.send_message(
                            channel, 
                            f"{new_title}\n\n@{main_channel_id}", 
                            file=url,
                            buttons=[Button.inline('approve', b'approve'),Button.inline('reject', b'reject')]
                            )
                            write_file(url,"reddit")
                        except Exception as e:
                            print(e)

async def livechart_fetch(last):
    channel = await bot.get_entity(channel_id)
    # channel = channel_id
    print("from livechart")
    url = "https://www.livechart.me/feeds/headlines"
    response = requests.get(url)
    response_html = response.content
    soup = BeautifulSoup(response_html,'xml')
    title_list = soup.find('item').title.contents
    title = title_list[0]
    link_list = soup.find('item').link.contents
    link = link_list[0]
    thumb = soup.find('media:thumbnail')["url"]
    print(thumb)
    word_dict = ["trailer", "Trailer","TRAILER", "pv", "PV", "teaser", "Teaser","visual", "Visual","preview", "Preview", "Announced","announced","project", "Project","op", "OP", "ed", "ED", "Announcement","TRAILER","anime","begins"]
    if link != last:
        try:
            new_title = f"[{title}]({link})"
            for word in word_dict:
                if word in title:
                    new_title = title.replace(word, f"[{word}]({link})")
                    break
            delete_files()
            dwl_vid(link)
            location = "videos/youtube.mp4"
            file = location
            check_thumb()
            thumbnail = "videos/thumb.png"
            dur = get_duration()
            print(dur)
            dur = int(dur)
            print(dur)
            await bot.send_message(
            channel, 
            f"{new_title}\n\n@{main_channel_id}", 
            file=file,
            thumb=thumbnail,
            supports_streaming=True,
            attributes=[DocumentAttributeVideo(
            duration=dur, 
            w=1260, 
            h=720, 
            supports_streaming=True
            )],
            buttons=[Button.inline('approve', b'approve'),Button.inline('reject', b'reject')]
        )
            print("uploaded")
            write_file(link,"livechart")

        except Exception as e:
                print(e)
                try:
                    print("video not found looking for twiiter image")
                    split = link.split('/')
                    id = split[-1]
                    status = api.get_status(id)
                    media = status.entities['media']
    
                    for image in media:
                        media_url = image['media_url']
                    new_title = f"[{title}]({media_url})"
    
                    for word in word_dict:
                        if word in title:
                            new_title = title.replace(word, f"[{word}]({media_url})")
                            break
                    await bot.send_message(
                    channel, 
                    f"{new_title}\n\n@{main_channel_id}", 
                    file=media_url,
                    buttons=[Button.inline('approve', b'approve'),Button.inline('reject', b'reject')]
                    )
                    write_file(link,"livechart")
                except Exception as e:
                    print(e)
                    try:
                        print("nothing found downloading thumbnail")
                        split = thumb.split('?')
                        img = split[0]
                        for word in word_dict:
                            if word in title:
                                new_title = title.replace(word, f"[{word}]({img})")
                                break
                        await bot.send_message(
                        channel, 
                        f"{new_title}\n\n@{main_channel_id}", 
                        file=img,
                        buttons=[Button.inline('approve', b'approve'),Button.inline('reject', b'reject')]
                        )
                        write_file(link,"livechart")
                    except Exception as e:
                        print(e)



@bot.on(events.CallbackQuery)
async def click_handler(event):
    # channel = await bot.get_entity(f"t.me/{channel_id}")
    channel = channel_id
    main_channel = await bot.get_entity(f"t.me/{main_channel_id}")
    message = event.message_id
    userid = event.query.user_id
    print(userid)
    user_info = await bot.get_entity(userid)
    messages = await bot.get_messages(channel,ids=message)
    msg_txt = messages.message
    if event.data == b'approve':
        await bot.send_message(main_channel,messages,buttons = Button.clear())
        await bot.edit_message(channel,message,f"{msg_txt}\n\nthis message was posted by @{user_info.username}")
    elif event.data == b'reject':
        await bot.edit_message(channel,message,f"{msg_txt}\n\nthis message was rejected by @{user_info.username}")


loop = asyncio.get_event_loop()
async def fetch_news():
    # channel = await bot.get_entity(f"t.me/{channel_id}")

    while True:
        livechart_last = read_file("livechart")
        reddit_last = read_file("reddit")
        await reddit_fetch(reddit_last)
        await livechart_fetch(livechart_last)
        print((reddit_last,livechart_last))
        
        
        print('going to sleep')
        await asyncio.sleep(60)    
        print("nothing")
    






loop.run_until_complete(fetch_news())

bot.start()

bot.run_until_disconnected()
