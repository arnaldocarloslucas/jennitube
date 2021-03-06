from pytube import YouTube
from pytube import Playlist
from tkinter.filedialog import askdirectory

def music(path):
    link = str(input("Enter the song link on youtube: "))

    counter = 0
    should_not_pass = False
    while should_not_pass == False:
        try:
            print("Downloading...")
            yt = YouTube(link).streams.filter(only_audio=True,file_extension='mp4')
            yt2 = YouTube(link).title
            for i in yt:
                i.download(path)
                print(f"{yt2} successfully downloaded!")
            should_not_pass = True
        except:
            print(f'Error 404, Trying again... COUNTER={counter}/10')
            counter+=1
        if counter == 10:
                print("Download fail :(")
                should_not_pass = True                       

def playlist(path):        
    link = str(input("Enter the playlist link on youtube: "))

    should_not_pass = False
    while should_not_pass == False:
        try:
            yt = Playlist(link)
            should_not_pass = True
        except:
            print("Error 404, Trying again...")
            
    for video in yt.videos:
        should_not_pass = False
        counter = 0
        while should_not_pass == False:
            try:
                print("Downloading...")
                yt = video.streams.filter(only_audio=True, file_extension='mp4')
                yt.first().download(path)
                yt2 = video.title
                print(f"{yt2} successfully downloaded!")
                should_not_pass = True
            except:
                print(f'Error 404, Trying again... COUNTER={counter}/10')  
                counter+=1  
            if counter == 10:
                print("Download fail :(")
                should_not_pass = True

if __name__=='__main__':
    jenni = 0
    while jenni != '1' or jenni != '2':
        jenni = input("Do you want to download a single music or an entire playlist? \n1 - Single music\n2 - Playlist\n3 - Exit program\n")
        if jenni in ('1','2'):         
            print('Select a folder to save your music(s): ')   
            path = askdirectory()
            if path == "":
                exit(0)
            if jenni == '1':
                music(path)
            if jenni == '2':
                playlist(path)
        if jenni == '3':
            exit(0)