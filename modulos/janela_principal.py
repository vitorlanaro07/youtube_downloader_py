import concurrent.futures

from modulos import search_audio_video
import PySimpleGUI as sg
import os
from concurrent.futures import ThreadPoolExecutor

url_logo = os.getcwd()+"/imagem/logo.png"

layout_cre = []


def janela_principal():
    os.system('clear')
    print("Iniciando...")
    # criar_frame_com_thread()
    font = ('Courier New', 11)
    sg.theme('DarkBlue3')
    sg.set_options(font=font)

    column_search = [[sg.Input(), sg.Button("Search"),sg.Button("Opções", key="OPT", visible=False)]]

    column_title = [[sg.Text("Downloader Youtube", justification="center", key="TITULO"),
                        sg.Image(search_audio_video.transform_img(url=None, x=300, y=150, imagem=url_logo), visible=False, key="LOGO_PEQ")]
                    ]
    layout_cre = [
        [frame_img(x), frame_txt(x)] for x in range(0,31)
    ]

    layout_img = [
        [sg.Image(search_audio_video.transform_img(url=None, x=600, y=400, imagem=url_logo), visible=True, key="LOGO", pad=(0,100))]
    ]

    layout = [
                [sg.Column(column_title, justification="center", vertical_alignment="center")],
                [sg.Column(column_search, vertical_alignment="center", justification="center")],
                [sg.Text(key="RES", justification='center', background_color='#424f5e', expand_x=True, visible=False)],
                [sg.Column(layout_img, justification="center", vertical_alignment="center"),[
                    sg.pin(sg.Column(layout_cre, key=f'COLUMN', visible=False, scrollable=True, vertical_scroll_only=True, size=(1920, 1080), expand_y=True),expand_y=True)]]
            ]

    window = sg.Window("Downloader MP3 YOUTUBE", layout, finalize=True, size=(1000, 700), font=(50), resizable=True)
    return window

# def adiciona_frames_ao_layout(x):
#     layout_cre.append(frame(x))
#
#
# def criar_frame_com_thread():
#     with ThreadPoolExecutor(max_workers=31) as executor:
#         executor.map(adiciona_frames_ao_layout, range(0, 30))

# def frame(index):
#     print(index)
#     return [sg.Frame("", [[sg.Image(search_audio_video.transform_img(),key=f"-IMG-{index}")]], key=f"FRAME-IMG{index}", pad=(5, 10), border_width=0, visible=False), \
#            sg.Frame("", [[sg.Text("", key=f"-TEXT-{index}")],[sg.Text("", key=f"-CANAL-{index}")],[sg.Text("", key=f"-TIME-{index}")],[sg.Text("", key=f"-VIEWS-{index}")],[sg.Button("Baixar")]], key=f"FRAME-TXT{index}",pad=(5, 10),border_width=0, expand_x=True, visible= False)]

def frame_img(index):
    # print('img',index)
    return sg.Frame("", [[sg.Image(search_audio_video.transform_img(),key=f"-IMG-{index}")]], key=f"FRAME-IMG{index}", pad=(5, 10), border_width=0, visible=False)


def frame_txt(index):
    # print('txt',index)
    return sg.Frame("", [
                            [sg.Text("", key=f"-TEXT-{index}")],
                                [sg.Text("", key=f"-CANAL-{index}")],
                                [sg.Text("", key=f"-TIME-{index}")],
                                [sg.Text("", key=f"-VIEWS-{index}")],
                                [sg.Button("Baixar")]
                             ], key=f"FRAME-TXT{index}",pad=(5, 10),border_width=0, expand_x=True, visible= False)

if __name__ == "__main__":
    janela_principal()
    # criar_frames()
    # criar_frame_com_thread()
    # print(layout_cre)