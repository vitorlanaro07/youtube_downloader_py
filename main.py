import PySimpleGUI as sg
from modulos import web_scraping_youtube_link_and_label as youtube_acess
from PIL import Image
from io import BytesIO
import requests

def frame_img(x):
    return sg.Frame("", [[sg.Image(transform_img(),key=f"-IMG-{x}")]], pad=(5, 3), border_width=0)

def frame_txt(x):
    return sg.Frame("", [[sg.Text("Titulo",key=f"-TEXT-{x}")],
                          [sg.Button("Baixar")]],pad=(5, 3),border_width=0)
def main():

    font = ('Courier New', 11)
    sg.theme('DarkBlue3')
    sg.set_options(font=font)

    column_one = [[sg.Text("Dowloader Youtube")]]
    column_two = [[sg.Input(),sg.Button("Search")]]

    layout_frame1 = [
        [frame_img(0), frame_txt(0)],
    ]


    layout = [[sg.Column(column_one, vertical_alignment="center", justification="center")],
              [sg.Column(column_two, vertical_alignment="bottom", justification="center")],
              [sg.Text('RESULTADO',key="RES-", justification='center', background_color='#424f5e', expand_x=True,visible=False)],
              [sg.Column(layout_frame1, scrollable=True, vertical_scroll_only=True, size=(800, 300*3), key='COLUMN')] #, visible=False
              ]


    window = sg.Window("Downloader MP3 YOUTUBE", layout, finalize=True, size=(800,800), font=(50))


    while True:
        event, values = window.read()
        print(event, values)

        if event == sg.WINDOW_CLOSED:
            break

        if event == "Search":
            # faço a requisição dos dados
            data = youtube_acess.get_data(values[0])
            x=0
            for item in data:
                img = transform_img(item['thumb'])
                window[f"-IMG-{x}"].update(img)
                window[f"-TEXT-{x}"].update(item["title"])
                x+=1
                layout_frame = [[frame_img(x), frame_txt(x)]]
                window.extend_layout(window['COLUMN'], layout_frame)
            window.visibility_changed()
            window['COLUMN'].contents_changed()


    window.close()



def transform_img(url=None):
    if url == None:
        url = "https://img.youtube.com/vi"
    else:
        pass

    response = requests.get(url, stream=True)
    image = response.content
    pil_image = Image.open(BytesIO(image)).resize(size=(200,150))
    png_bio = BytesIO()
    pil_image.save(png_bio, format="PNG")
    png_data = png_bio.getvalue()

    return (png_data)


if __name__ == "__main__":
    main()