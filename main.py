import tkinter as tk
from pytube import YouTube
from tkinter import filedialog, messagebox
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")

        # Variables
        self.output_path = tk.StringVar()
        self.video_url = tk.StringVar()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Video URL Entry
        tk.Label(self.root, text="Video URL:").pack(pady=10)
        tk.Entry(self.root, textvariable=self.video_url, width=50).pack(pady=5)

        # Output Path Entry
        tk.Label(self.root, text="Output Path:").pack(pady=10)
        tk.Entry(self.root, textvariable=self.output_path, width=50, state="disabled").pack(pady=5)
        tk.Button(self.root, text="Browse", command=self.browse_output_path).pack(pady=10)

        # Download Button
        tk.Button(self.root, text="Download Video", command=self.download_video).pack(pady=20)

    def browse_output_path(self):
        output_path = filedialog.askdirectory()
        self.output_path.set(output_path)

    def download_video(self):
        # Check if video URL and output path are selected
        if not self.video_url.get():
            messagebox.showerror("Error", "Please enter the video URL.")
            return
        if not self.output_path.get():
            messagebox.showerror("Error", "Please select the output path.")
            return

        # Replace this part with your video download logic using the YouTube API
        yt = YouTube(self.video_url.get())
        video = yt.streams.get_highest_resolution()

        # download the video
        video.download(self.output_path.get())
        # Example: Display a message with the selected output path and video URL
        messagebox.showinfo("Info", f"Downloading video from {self.video_url.get()} to {self.output_path.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()


def download_video_from_youtube(link, path):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()

    # download the video
    video.download(path)