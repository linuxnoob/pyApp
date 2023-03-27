from pytube import YouTube
import moviepy.editor as mp
import os

# function to download YouTube video
def download_video(url, path):
    yt = YouTube(url)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path=path, filename=yt.title+ '.mp4')
    print("Video downloaded successfully.")

# function to convert video to MP3
def convert_to_mp3(path):
    video = mp.VideoFileClip(path)
    mp3_path = os.path.splitext(path)[0] + ".mp3"
    video.audio.write_audiofile(mp3_path)
    print("Conversion to MP3 complete.")

# download and convert video
if __name__ == '__main__':
    url = input("Enter the YouTube video URL : ")
    path = input("Enter the output path: ")

    # download video
    download_video(url, path)

    # convert to MP3
    video_path = os.path.join(path, YouTube(url).title + '.mp4')
    convert_to_mp3(video_path)
