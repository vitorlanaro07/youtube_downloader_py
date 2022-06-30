from pytube import YouTube
import os
import time
import sys

def baixar(url,dir, tipo):
    yt = YouTube(url)

    inico = time.time()
    if tipo == ".m4a":
        arquivo = yt.streams.filter(only_audio=True).first().download(output_path=dir)
        size = yt.streams.get_audio_only().filesize / 2654041
        print(size)
    else:
        arquivo = yt.streams.get_highest_resolution().download(output_path=dir)
        size = yt.streams.get_highest_resolution().filesize / 1000000

    fim = time.time()

    print("Tempo de download: {:.2f} segundos".format(fim - inico), "/ File size: {:.2f}MB".format(size))

    # 182879557
    # 68906078

    # save the file
    base, ext = os.path.splitext(arquivo)
    new_file = base + tipo
    os.rename(arquivo, new_file)

    # result of success
    print(yt.title + " foi baixado com sucesso.")

if __name__ == "__main__":
   baixar("https://www.youtube.com/watch?v=EsbTBaPA_7w",  "/home/vitorlanaro/Music", ".m4a")