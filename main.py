import os
import tkinter as tk
from pytube import YouTube
from tkinter import filedialog, messagebox


class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")

        # Variables
        self.output_path = tk.StringVar()
        self.video_url = tk.StringVar()
        self.download_option = tk.StringVar(value="video")  # Default is video

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

        # Download Option
        tk.Label(self.root, text="Download Option:").pack(pady=10)
        tk.Radiobutton(self.root, text="Video", variable=self.download_option, value="video").pack(anchor="w")
        tk.Radiobutton(self.root, text="Audio Only", variable=self.download_option, value="audio").pack(anchor="w")

        # Download Button
        tk.Button(self.root, text="Download Video", command=self.download).pack(pady=20)

    def browse_output_path(self):
        output_path = filedialog.askdirectory()
        self.output_path.set(output_path)

    def download(self):
        # Check if video URL and output path are selected
        if not self.video_url.get():
            messagebox.showerror("Error", "Please enter the video URL.")
            return
        if not self.output_path.get():
            messagebox.showerror("Error", "Please select the output path.")
            return


        download_type = self.download_option.get()

        if download_type == "video":
            yt = YouTube(self.video_url.get())
            video = yt.streams.get_highest_resolution()
            # download the video
            video.download(self.output_path.get())
            # Example: Display a message with the selected output path and video URL
            messagebox.showinfo("Info", f"Downloading video from {self.video_url.get()} to {self.output_path.get()}")

        elif download_type == "audio":
            yt = YouTube(self.video_url.get())
            audio = yt.streams.filter(only_audio=True).first()
            audio.download(self.output_path.get(),filename=f"{yt.title}.mp3")
            # Example: Display a message with the selected output path and file URL
            messagebox.showinfo("Info", f"Downloading audio from {self.video_url.get()} to {self.output_path.get()}")


if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()

def download_video_from_youtube(link, path):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()
    # download the video
    video.download(path)