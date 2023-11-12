from pytube import YouTube

def download_video_from_youtube(link, path):
    yt = YouTube(link)
    video = yt.streams.get_highest_resolution()

    # download the video
    video.download(path)

# example usage:
download_video_from_youtube(r"https://www.youtube.com/watch?v=ra7JbtToVYU&ab_channel=GeorgeWassouf-Topic", r'C:\Users\rani-pc\Desktop')