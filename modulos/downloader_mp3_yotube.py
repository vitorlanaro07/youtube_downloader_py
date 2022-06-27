from pytube import YouTube
import os
import datetime

def baixar(url):

    # url input from user
    yt = YouTube(url)

    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    print(yt.thumbnail_url, str(datetime.timedelta(seconds=yt.length)), yt.author, "{:d}".format(yt.views))
    # check for destination to save file

    destination = os.getcwd()

    # download the file
    out_file = video.download(output_path=destination)

    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.m4a'
    os.rename(out_file, new_file)

    # result of success
    print(yt.title + " has been successfully downloaded.")

if __name__ == "__main__":
    baixar("https://www.youtube.com/watch?v=5GJWxDKyk3A")