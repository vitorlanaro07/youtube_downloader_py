from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = "https://www.youtube.com/results?search_query=billie+eilish"

session = HTMLSession()
request = session.get(url)
request.html.render()


soup = BeautifulSoup(markup=request.html.html, features="html.parser")

for x in soup.find_all(id=["img","video-title"],class_=["style-scope yt-img-shadow"]):
    print(x, x.get("aria-label"))