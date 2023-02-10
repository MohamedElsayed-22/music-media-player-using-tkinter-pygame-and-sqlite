import sqlite3
import os 
import eyed3

music_dir = "/home/mohamed/Downloads"

for file_ in os.listdir(music_dir):
    if file_.split('.')[-1] in ["mp3","wav","ogg"]:
        audiofile = eyed3.load(music_dir + '/' + file_)
        tags = audiofile.tag
        print(tags.title)
        print(tags.artist)
        print(audiofile.info.time_secs)
