import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube

class YoutubeDownloaderGUI:
    def __init__(self, master):
        self.master = master
        master.title("Youtube Downloader")

        self.label_url = tk.Label(master, text="Enter the YouTube video URL:")
        self.label_url.pack()

        self.entry_url = tk.Entry(master, width=50)
        self.entry_url.pack()

        self.label_path = tk.Label(master, text="Select output directory:")
        self.label_path.pack()

        self.btn_path = tk.Button(master, text="Select Directory", command=self.select_directory)
        self.btn_path.pack()

        self.label_status = tk.Label(master, text="")
        self.label_status.pack()

        self.btn_download = tk.Button(master, text="Download", command=self.download_video)
        self.btn_download.pack()

    def select_directory(self):
        self.directory = filedialog.askdirectory(initialdir=os.getcwd(), title="Select directory")
        self.label_status.config(text="Selected directory: " + self.directory)

    def download_video(self):
        url = self.entry_url.get().strip()
        path = self.directory

        if url == "":
            self.label_status.config(text="Error: Please enter a valid YouTube video URL.")
            return
        if path is None:
            self.label_status.config(text="Error: Please select an output directory.")
            return

        try:
            YouTube(url).streams.first().download(path)
            self.label_status.config(text="Video downloaded successfully.")
        except Exception as e:
            self.label_status.config(text="Error: " + str(e))

root = tk.Tk()
gui = YoutubeDownloaderGUI(root)
root.mainloop()
