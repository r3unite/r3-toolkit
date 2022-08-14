import urllib.request
import re
from yt_dlp import YoutubeDL
import urllib.parse
import os
SAVE_PATH = os.path.expanduser('~/Documents/Youtube-Downloads-R3/');


searchString = input("Search phrase:")
query = urllib.parse.quote_plus(searchString)
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

print("Found link: " + "https://www.youtube.com/watch?v=" + video_ids[0])
print("Starting Download!")
with YoutubeDL({'outtmpl':SAVE_PATH + '%(title)s.%(ext)s'}) as ydl:
  ydl.download("https://www.youtube.com/watch?v=" + video_ids[0])

  
  
  
  
  