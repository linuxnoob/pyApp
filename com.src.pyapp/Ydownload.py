import pytube

#directory saved

download_loc ="D:\Music"

#url video
video_url = input("Enter URL : ")

#create an instance of youtube vid

video_instance = pytube.YouTube(video_url)
stream = video_instance.streams.get_highest_resolution()

#download
stream.download()

