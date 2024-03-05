import json
import scrapetube
from youtube_transcript_api import YouTubeTranscriptApi
from time import sleep
import os
from pathlib import Path

config_file = Path(r"scripts/scrape-xmpro-yt-transcripts-config.json")

config = None

with open(config_file, "rb") as file:
    config = json.load(file)

if config is None:
    raise Exception(f"No config defined in file at {config_file}")


os.makedirs(config["folderPath"], exist_ok=True)

import re

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

def make_windows_compatible_filename(filename):
    # Replace reserved characters
    replacements = {
        '<': '[',
        '>': ']',
        ':': '-',
        '"': "'",
        '/': '-',
        '\\': '-',
        '|': '_',
        '?': '!',
        '*': 'x',
    }
    for old_char, new_char in replacements.items():
        filename = filename.replace(old_char, new_char)
    
    # Remove control characters (integer values < 31)
    filename = ''.join(char for char in filename if ord(char) > 31)
    
    # Trim spaces and periods from the end
    filename = filename.rstrip('. ')
    filename = filename.replace(" ", "-").lower()
    
    return filename


# YT

videos = scrapetube.get_channel(channel_username="XMPRO")

for video in videos:
    title = video['title']['runs'][0]['text']
    title = title.replace('|', '-').replace('?', '-')
    title = emoji_pattern.sub(r'', title)
    description = video['descriptionSnippet']['runs'][0]['text'] if 'descriptionSnippet' in video else ''
    video_id = video['videoId']

    title = make_windows_compatible_filename(title)
    filename = f'{config["folderPath"]}/{title}.md'

    
    if os.path.exists(filename) and config["clean"]:
        continue

    


    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except Exception as e: 
        print(e)
        continue

    
    text = '\n\n'.join([t['text'] for t in transcript])


    with open (filename, 'w', encoding="utf-8") as f:
        try:
            print(f'[NEW]\t{title}')
            f.write("# " + title + "\n")  
            f.write('{% embed url="' + f'https://www.youtube.com/watch?v={video_id}' + '" %}\n\n')
            #f.write(f'[![Watch the video](https://img.youtube.com/vi/{video_id}/hqdefault.jpg)](https://www.youtube.com/watch?v={video_id})\n')
            # f.write(f'https://www.youtube.com/watch?v={video_id}\n')
            f.write('\n\n')
            f.write(description)
            f.write('\n')
            f.write('<details>\n')
            f.write('<summary>Transcript</summary>')
            f.write(description)
            f.write('\n')
            f.write(text)
            f.write('\n')
            f.write('</details>')
        except Exception as e:
            print(e)
            print(title)
            print(description)
            print(text)
            continue    


    sleep(0.5)
