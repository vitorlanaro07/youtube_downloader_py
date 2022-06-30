from modulos import search_audio_video
import PySimpleGUI as sg
import os


url_logo = os.getcwd()+"/imagem/logo.png"


def janela_principal():
    os.system('clear')
    print("Iniciando...")
    font = ('Courier New', 11)
    sg.theme('DarkBlue3')
    sg.set_options(font=font)

    column_search = [[sg.Input(), sg.Button("Search"),sg.Button("Opções", key="OPT", visible=False)]]

    column_title = [[sg.Text("Downloader Youtube", justification="center", key="TITULO"),
                        sg.Image(search_audio_video.transform_img(url=None, x=300, y=150, imagem=url_logo), visible=False, key="LOGO_PEQ")]
                    ]

    layout_cre = [
        [frame_img(x), frame_txt(x)] for x in range(0, 30)
    ]

    layout_img = [
        [sg.Image(search_audio_video.transform_img(url=None, x=600, y=400, imagem=url_logo), visible=True, key="LOGO", pad=(0,100))]
    ]

    layout = [
                [sg.Column(column_title, justification="center", vertical_alignment="center")],
                [sg.Column(column_search, vertical_alignment="center", justification="center")],
                [sg.Text(key="RES", justification='center', background_color='#424f5e', expand_x=True, visible=False)],
                [sg.Column(layout_img, justification="center", vertical_alignment="center"),[
                    sg.Column(layout_cre, key=f'COLUMN', visible=False, scrollable=True, vertical_scroll_only=True, size=(1200, 500), expand_y=True)]]
            ]

    window = sg.Window("Downloader MP3 YOUTUBE", layout, finalize=True, size=(1000, 700), font=(50), resizable=True)
    return window


def frame_img(index):
    return sg.Frame("", [[sg.Image(search_audio_video.transform_img(),key=f"-IMG-{index}")]], key=f"FRAME-IMG{index}", pad=(5, 10), border_width=0, visible=False)


def frame_txt(index):
    return sg.Frame("", [
                            [sg.Text("", key=f"-TEXT-{index}")],
                                [sg.Text("", key=f"-CANAL-{index}")],
                                [sg.Text("", key=f"-TIME-{index}")],
                                [sg.Text("", key=f"-VIEWS-{index}")],
                                [sg.Button("Baixar")]
                             ], key=f"FRAME-TXT{index}",pad=(5, 10),border_width=0, expand_x=True, visible= False)

if __name__ == "__main__":
    janela_principal()