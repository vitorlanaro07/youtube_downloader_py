import youtube_dl

url = "https://www.youtube.com/watch?v=V1Pl8CzNzCw"

ydl_opts = {
    'format': 'bestaudio/best',
    'ratelimit': 5000000,
    'verbose': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
        'preferredquality': '192',
    }],

}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])