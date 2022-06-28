from io import BytesIO
from PIL import Image
import requests
from pytube import YouTube, Search
import datetime

def transform_img(url=None, x=200, y=150):
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
    is_a = what_is(data)
    print("Fazendo Requisição a página!!")
    list = []
    if is_a == "Text":
        yt = Search(data)
        for v in yt.results:
            list.append({"title": v.title, "link": v.watch_url, "duration": str(datetime.timedelta(seconds=v.length)),
                         "thumb": transform_img(v.thumbnail_url)})  # "label":video.get("aria-label")
    else:
        yt = YouTube(data)
        list.append({"title": yt.title, "link": data, "duration": str(datetime.timedelta(seconds=yt.length)),
                     "thumb": transform_img(yt.thumbnail_url)})  # "label":video.get("aria-label")

    return list



def what_is(data):
    if not bool(data.find("https://")):
        return "Link"
    else:
        return "Text"

if __name__ == "__main__":
    get_data("Billie Elish")
