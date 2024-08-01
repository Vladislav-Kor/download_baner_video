# -*- coding: utf-8 -*-
from pytube import YouTube
from tkinter import *
import os
import requests

def download_thumbnail():
    url = entry.get()
    yt = YouTube(url)
    thumbnail_url = yt.thumbnail_url
    print(f"Downloading thumbnail from: {thumbnail_url}")
    
    # Specify the path to save the thumbnail
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    thumbnail_path = os.path.join(desktop_path, "thumbnail.jpg")
    
    # Download the thumbnail image
    response = requests.get(thumbnail_url)
    if response.status_code == 200:
        with open(thumbnail_path, 'wb') as f:
            f.write(response.content)
        print("Thumbnail downloaded successfully!")
    else:
        print("Failed to download thumbnail.")

root = Tk()
root.title("YouTube Thumbnail Downloader")

label = Label(root, text="Enter YouTube video URL:")
label.pack(pady=10)

entry = Entry(root, width=50)
entry.pack(pady=10)

download_button = Button(root, text="Download Thumbnail", command=download_thumbnail)
download_button.pack(pady=10)

root.mainloop()
