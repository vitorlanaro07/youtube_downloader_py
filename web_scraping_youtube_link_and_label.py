from requests_html import HTMLSession
from bs4 import BeautifulSoup

#List para armazenar as informações filtradas
list = []

#Inico a sessão
session = HTMLSession()

#Busco um vídeo no youtube
search = input("O que você procura:")
url = f"https://www.youtube.com/results?search_query={search}"

#Request + Converte para HTML
r = session.get(url)
r.html.render(sleep=1)
soup = BeautifulSoup(markup=r.html.html, features="html.parser")

# Faz a filtragem do que está sendo buscado
# guarda na lista e apresenta na tela
for video in soup.find_all(id=["href", "video-title", "text"]):
    try:
        list.append({"label": video.get("aria-label"), "link": str("https://www.youtube.com"+video.get("href"))})
        print(video.get("aria-label"), str("https://www.youtube.com"+video.get("href")))
    except:
        pass