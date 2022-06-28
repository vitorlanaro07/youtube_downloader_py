from pytube import YouTube
import os
import time

def baixar(url,dir, tipo):
    yt = YouTube(url)

    inico = time.time()
    if tipo == ".m4a":
        arquivo = yt.streams.filter(only_audio=True).first().download(output_path=dir)
    else:
        arquivo = yt.streams.get_highest_resolution().download(output_path=dir)

    fim = time.time()

    print(f"Tempo de download: {fim - inico}")

    # save the file
    base, ext = os.path.splitext(arquivo)
    new_file = base + tipo
    os.rename(arquivo, new_file)

    # result of success
    print(yt.title + " foi baixado com sucesso.")

if __name__ == "__main__":
   baixar("https://www.youtube.com/watch?v=SxEjHAlCqmo",  "/home/vitorlanaro/Music", ".mp4")