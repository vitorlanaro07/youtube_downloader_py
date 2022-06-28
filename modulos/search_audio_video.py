import time
from io import BytesIO
from PIL import Image
import requests
from pytube import YouTube, Search
import datetime

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


def get_data(data):
    inicio = time.time()
    is_a = what_is(data)
    print("Buscando...")
    list = []
    if is_a == "Text":
        yt = Search(data)
        for v in yt.results:
            print(v.title)
            list.append({"title": v.title, "link": v.watch_url, "duration": str(datetime.timedelta(seconds=v.length)),
                         "thumb": transform_img(v.thumbnail_url), "views":v.views, "canal": v.author})
    else:
        yt = YouTube(data)
        list.append({"title": yt.title, "link": data, "duration": str(datetime.timedelta(seconds=yt.length)),
                     "thumb": transform_img(yt.thumbnail_url), "views":yt.views, "canal": yt.author})
    fim = time.time()
    print("------------------------------------------------------------------")
    print(f"Foram encontados {len(list)} resultados")
    print(f"Tempo de pesquisa: {fim - inicio}")
    return list



def what_is(data):
    if not bool(data.find("https://")):
        return "Link"
    else:
        return "Text"

if __name__ == "__main__":
    get_data("Billie Elish")
