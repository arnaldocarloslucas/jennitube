from logging import NullHandler
from pytube import YouTube
from pytube import Playlist
import os

def music():
    print()
    link = str(input("Enter the song link on youtube: "))
    print()

    counter = 0
    should_not_pass = False
    while should_not_pass == False:
        try:
            print("Downloading...", '\n')
            yt = YouTube(link).streams.filter(only_audio=True,file_extension='mp4')
            yt2 = YouTube(link).title
            for i in yt:
                i.download()
                print(90*'#')
                print(f"{yt2} successfully downloaded!")
                print(90*'#', '\n')
                should_not_pass = True
        except:
            print(f'Error 404, Trying again... COUNTER={counter}/10')
            counter+=1
        if counter == 10:
                print("Download fail :(", '\n')
                should_not_pass = True                       

def playlist():        
    print()
    link = str(input("Enter the playlist link on youtube: "))
    print()

    should_not_pass = False
    while should_not_pass == False:
        try:
            yt = Playlist(link)
            should_not_pass = True
        except:
            print("Error 404, Trying again...", '\n')
            
    for video in yt.videos:
        should_not_pass = False
        counter = 0
        while should_not_pass == False:
            try:
                print("Downloading...")             
                yt = video.streams.filter(only_audio=True, file_extension='mp4')
                yt.first().download()
                yt2 = video.title
                print(f"{yt2} successfully downloaded!", '\n')
                should_not_pass = True
            except:
                print(f'Error 404, Trying again... COUNTER={counter}/10')  
                counter+=1  
            if counter == 10:
                print("Download fail :(", '\n')
                should_not_pass = True

if __name__=='__main__':
    jenni = 0
    while jenni != '1' or jenni != '2':
        jenni = input("\nDo you want to download a single music or an entire playlist? (Choose and press Enter) \n1 - Single music\n2 - Playlist\n3 - Exit program\n\n")
        if jenni in ('1','2'):         
            if jenni == '1':
                music()
            if jenni == '2':
                playlist()
        if jenni == '3':
            exit(0)