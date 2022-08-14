import urllib.request
import re
import os
from yt_dlp import YoutubeDL
import urllib.parse
import validators
SAVE_PATH = os.path.expanduser('~/Documents/Youtube-Downloads-R3/');
# FROM LINK

linkURL = input("URL to download:")
if(validators.url(linkURL)):

   print("Link is valid! Entered link: " + linkURL)
   print("Starting Download!")
   with YoutubeDL({'outtmpl':SAVE_PATH + '%(title)s.%(ext)s'}) as ydl:
     ydl.download(linkURL)
else:
   print("Invalid link!")

  
  
  
  
  