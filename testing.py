# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 01:45:47 2022

@author: Mohamed Elsayed
"""

# from vlc import Instance
# from tkinter import *

# playlist = ['friends_from_another_country.mp3', "Anime [amv] dancin_2.mp3", 'friends_from_another_country.mp3']

# class testVLC:

#     def __init__(self):
#          self.list1 = playlist
#          self.Player = Instance('--loop')

#     def addPlaylist(self):
#         self.mediaList = self.Player.media_list_new()
#         for music in self.list1:
#             self.mediaList.add_media(self.Player.media_new(music))
#         self.listPlayer = self.Player.media_list_player_new()
#         self.listPlayer.set_media_list(self.mediaList)
#     def playPlaylist(self):
#         self.listPlayer.play()
#     def nextPlay(self):
#         self.listPlayer.next()
        
#     def stopSong(self):
#         self.listPlayer.stop()
    
    
 
        
# m1 = testVLC()
# m1.addPlaylist()
# m1.playPlaylist()
        
# window = Tk()

# window.geometry("700x350")
# buttonPlay = Button(window, text = "play", fg = "blue", command = m1.nextPlay)
# buttonPlay.grid(row = 1, column = 1)
# buttonStop = Button(window, text = "stop", fg = "blue", command = m1.stopSong)
# buttonStop.grid(row = 1, column = 2)

# # window.after(11000, m1.nextPlay())
# window.mainloop()

# m1.stopSong()



def summation(x, y):
    return x+y

results = []
for i in range(1, 6):
    x = summation(i, i+1)
    results.append(x)

print(results)























        
        
    
