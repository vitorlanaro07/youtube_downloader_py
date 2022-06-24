from requests_html import HTMLSession
from bs4 import BeautifulSoup

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


# Faz a filtragem do que está sendo buscado
# guarda na lista e apresenta na tela
def get_data(data):
    list = []
    soup = request_pesq(data)
    for video in soup.find_all(id=["href", "video-title", "text", "img", "thumbail", "dismissible", "contents", "primary"]):
        try:
            cod_vi = str(video.get("href")).replace("watch?v=","")
            list.append({"title": video.get("title"), "link": str("https://www.youtube.com"+video.get("href")), "thumb": "https://img.youtube.com/vi"+cod_vi+"/mqdefault.jpg"}) #"label":video.get("aria-label")
        except:
            pass

    return list


if __name__ == "__main__":
    data = get_data("Billie Elish")
    # for item in data:
    #     print(item)