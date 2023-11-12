import tkinter as tk
from tkinter import filedialog
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")

        # Variables
        self.output_path = tk.StringVar()

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
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
        # Check if output path is selected
        if not self.output_path.get():
            tk.messagebox.showerror("Error", "Please select the output path.")
            return

        # Replace this part with your video download logic using the YouTube API
        # Example: Display a message with the selected output path
        tk.messagebox.showinfo("Info", f"Video will be downloaded to: {self.output_path.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()
