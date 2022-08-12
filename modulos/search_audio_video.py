import time
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
from pytube import YouTube
import datetime
from concurrent.futures import ThreadPoolExecutor

#Variaveis globais
lista = []
links = []

def iniciar_sessao(data):
    sessao = HTMLSession()
    url = f"https://www.youtube.com/results?search_query={data}"
    return sessao.get(url)

def request_url(data):
    response = iniciar_sessao(data)
    response.html.render(sleep=1)
    return response.html.html

def filtra_links(soup):
    for video in soup.find_all(id=["href", "video-title"]):
        try:
            if video.get("href") != None:
                links.append("https://www.youtube.com" + str(video.get("href")))
        except:
            pass

def video_encontrado(link):
    yt = YouTube(link)
    print(yt.title)
    lista.append({"title": yt.title, "link": link, "duration": str(datetime.timedelta(seconds=yt.length)),
            "thumb": transform_img(yt.thumbnail_url), "views": yt.views, "canal": yt.author})

def threads_filtragem_dos_videos():
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(video_encontrado, links)


def web_scrapping(busca):
    response = request_url(busca)
    soup = BeautifulSoup(markup=response, features="html.parser")
    filtra_links(soup)
    threads_filtragem_dos_videos()


def o_que_eh(data):
    if not bool(data.find("https://")):
        return "Link"
    else:
        return "Texto"

def transform_img(url=None, x=200, y=150, imagem=None):
    if bool(imagem):
        pil_image = Image.open(imagem).resize(size=(x,y))
    else:
        if url == None:
            url = "https://img.youtube.com/vi"
        else:
            pass
        response = requests.get(url, stream=True)
        image = response.content
        pil_image = Image.open(BytesIO(image)).resize(size=(x,y))

    png_bio = BytesIO()
    pil_image.save(png_bio, format="PNG")
    png_data = png_bio.getvalue()
    return (png_data)

def pesquisar(busca):
    start = time.time()
    eh = o_que_eh(busca)
    if (eh == 'Texto'):
        web_scrapping(busca)
    else:
        video_encontrado(busca)
    end = time.time()
    print("------------------------------------------------------------------")
    print(f"Foram encontados {len(lista)} resultados")
    print("Tempo de pesquisa: : {:.2f} segundos".format(end - start))


if __name__ == "__main__":
    web_scrapping("Maneva")