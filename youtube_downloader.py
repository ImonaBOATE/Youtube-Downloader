# Importing in the pytube and sys libraries
from pytube import YouTube, Channel
from sys import argv

# Creating a variable to store the Youtube link
link = argv
yt = YouTube(link[1])

# Confirming the YouTube video title, description and number of views in the Terminal prior to downloading 
print('Title: ', yt.title)
print('Total views: ', yt.views)
print('Description: ', yt.description)

# Downloading the video and saving it to the user defined folder below.
yt_download = yt.streams.get_highest_resolution()
yt_download.download('/home/noboate/Github/YoutubeDownloader/VideoDownloads')
