from pytube import YouTube
url = 'https://www.youtube.com/watch?v=7fcP64w7eBE'
my_video = YouTube(url)
print("**********************Video Title********************")
# get Video Title
print(my_video.title)
print("**********************Tumbnail Image*****************")
# get Thumbnail Image
print(my_video.thumbnail_url)
print("*********************Download Video******************")
my_video = my_video.streams.get_highest_resolution()
my_video.download()
