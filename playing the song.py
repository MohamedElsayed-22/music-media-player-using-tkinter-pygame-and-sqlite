# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 01:02:16 2022

@author: Mohamed Elsayed
"""

import vlc
from tkinter import *
import time




class Music:
    def __init__(self, pathList):
        
        self.player = vlc.Instance()
        self.results = []
        self.songsList = []
        self.pathList = pathList
        for path in pathList:
            self.media = self.player.media_new(path)
            self.results.append(self.media)
        self.song = self.player.media_player_new() 
        for songinResults in self.results:
            self.song.set_media(songinResults) 
            self.songsList.append(self.song)
            
        # self.song = vlc.MediaPlayer(path)
        self.startTime = 0
        self.loopSong = False
        
    def play(self):
        self.songsList[1].play()
        # time.sleep(self.song.get_length())
        # Music.loop(self)
        
    def playfromCetainSecond(self):
        self.songsList[1].play()
        self.songList[1].set_time(self.startTime) 
        
    def skip5seconds(self):
        self.songList[1].play()
        self.songList[1].set_time(self.songList[1].get_time() + 5000)    
    
    def prev5seconds(self):
        self.songList[1].play()
        self.songList[1].set_time(self.songList[1].get_time() - 5000)
        
    def stop(self):
        self.songList[1].stop()
        
    def pause(self):
        self.songList[1].set_pause(1)
    
    def duration(self):
        print(str(self.songList[1].get_length()/10**3))
        
    def currentTimePart(self):
        print(self.songList[1].get_time()/10**3)
        
    def nextSong(self):
        pass
       
    
    # def loop(self):
        
        
            
            
            
        
       
    # def loop(self):
    #     reversedPath = self.path[::-1]
    #     songName = ''
    #     for char in reversedPath:
    #         if char == '.':
    #             songName += char
    #     songName = songName[1:]
    #     # creating a new media list
    #     media_list = self.player.media_list_new() 
    #     self.song = self.player.media_list_player_new()         
    #     # adding media to media list
    #     self.media = self.player.media_new(self.path)
    #     media_list.add_media(self.media)          
    #     # setting media list to the mediaplayer
    #     self.song.set_media_list(media_list)
    #     self.player.vlm_set_loop("Anime [amv] dancin_2", True)
    #     self.song.play()
        
        
            # print("test")
            # if (self.song.is_playing() == False):
            #     self.song.stop()
            #     self.song.play()
        # self.loopSong = not self.loopSong
        

        
    def isitplaying(self):
        return print(self.song.is_playing())


            


        
        
        

path1 = [r"E:\Engineering Level 3 21-22\Semester 1\CSE 314 Advanced Programming\Project\Music Player\friends_from_another_country.mp3"]
m1 = Music(path1)
m1.startTime = (196441 - 10000)


    
window = Tk()


window.geometry("700x350")

buttonPlay = Button(window, text = "play", fg = "blue", command = m1.play)
buttonStop = Button(window, text = "stop", fg = "blue", command =m1.stop)
buttonPause = Button(window, text = "pause", fg = "blue", command =m1.pause)
buttonDuration = Button(window, text = "Duration", fg = "blue", command =m1.duration)
buttonCurrentTime = Button(window, text = "Current Time", fg = "blue", command =m1.currentTimePart)
buttonplayfromCetainSecond = Button(window, text = f"play from second: {m1.startTime/1000}",\
                                    fg = "blue", command =m1.playfromCetainSecond)
buttonNext5 = Button(window, text = "+5 s", fg = "blue", command =m1.skip5seconds)
buttonPrev5 = Button(window, text = "-5 s", fg = "blue", command =m1.prev5seconds)
# buttonLoop = Button(window, text = "loop unactivated", fg = "blue", command =m1.loop)

buttonplaying = Button(window, text = "playing?", fg = "blue", command =m1.isitplaying)
buttonplaying.grid(row = 4, column = 3)

if (m1.loopSong and (not m1.isitplaying)):
    m1.stop()
    m1.play()



# if m1.loopSong == True:
#     buttonLoop.destroy()
#     buttonLoop = Button(window, text = "loop activated", fg = "blue", command =m1.loop)
#     buttonLoop.grid(row = 3, column = 3)
# else:
#     buttonLoop.destroy()
#     buttonLoop = Button(window, text = "loop unactivated", fg = "blue", command =m1.loop)
#     buttonLoop.grid(row = 3, column = 3)
    
    


buttonPlay.grid(row = 1, column = 1)
buttonStop.grid(row = 2, column = 1)
buttonDuration.grid(row = 3, column = 1)
buttonPause.grid(row = 4, column = 1)
buttonCurrentTime.grid(row = 5, column = 1)
buttonplayfromCetainSecond.grid(row = 1, column = 2)
buttonNext5.grid(row = 2, column = 2)
buttonPrev5.grid(row = 3, column = 2)
# buttonLoop.grid(row = 3, column = 3)


window.mainloop()

m1.stop()

#To Do
#loop on the song
#next song
#previous song
#slider for the volume
    
    
    
    
    
    




    
    
