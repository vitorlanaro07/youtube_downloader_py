import time
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image
import requests
from pytube import YouTube
import datetime

#Inico a sessão
def init_sesion():
    session = HTMLSession()
    return session


#Busco um vídeo no youtube
def pesquisa(data):
    url = f"https://www.youtube.com/results?search_query={data}"
    return url


#Request + Converte para HTML
def request_pesq(data):
    url = pesquisa(data)
    session = init_sesion()
    r = session.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(markup=r.html.html, features="html.parser")
    return soup


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


def get_soup(data):
    links = []
    inicio3 = time.time()
    soup = request_pesq(data)
    for video in soup.find_all(id=["href", "video-title"]):
        try:
            if video.get("href") != None:
                links.append("https://www.youtube.com" + str(video.get("href")))
        except:
            pass
    fim3 = time.time()
    print("Tempo de request: : {:.2f} segundos".format(fim3 - inicio3))
    return links


def fazer_request(link):
    yt = YouTube(link)
    print(yt.title)
    return {"title": yt.title, "link": link, "duration": str(datetime.timedelta(seconds=yt.length)),
            "thumb": transform_img(yt.thumbnail_url), "views": yt.views, "canal": yt.author}



def get_data(data):
    inicio = time.time()
    is_a = what_is(data)
    list = []

    if is_a == "Text":
        links = get_soup(data)
        for link in links:
            list.append(fazer_request(link))

    else:
        yt = YouTube(data)
        list.append({"title": yt.title, "link": data, "duration": str(datetime.timedelta(seconds=yt.length)),
                     "thumb": transform_img(yt.thumbnail_url), "views":yt.views, "canal": yt.author})

    fim = time.time()

    print("------------------------------------------------------------------")
    print(f"Foram encontados {len(list)} resultados")
    print("Tempo de pesquisa: : {:.2f} segundos".format(fim - inicio))
    return list

def what_is(data):
    if not bool(data.find("https://")):
        return "Link"
    else:
        return "Text"

if __name__ == "__main__":
    data = get_data("Maneva")
    # for item in data:
    #     print(item["link"])