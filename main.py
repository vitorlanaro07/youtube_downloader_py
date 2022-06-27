import PySimpleGUI as sg
from modulos import web_scraping_youtube_link_and_label as youtube_acess
from modulos import downloader_mp3_yotube as mp3_down

url_logo = "https://logodownload.org/wp-content/uploads/2014/10/youtube-logo-0-2048x2048.png"

def main():
    font = ('Courier New', 11)
    sg.theme('DarkBlue3')
    sg.set_options(font=font)
    colunas_criadas = 1
    tamanho_resultado = 0

    column = [[sg.Text("Downloader Youtube",justification="Center")],
              [sg.Input(),sg.Button("Search")]]

    layout_frame1 = [
        [frame_img(0), frame_txt(0)],
    ]


    layout = [[sg.Image(youtube_acess.transform_img(url_logo, 300, 150), visible=False, key="LOGO_PEQ"),
               sg.Column(column, vertical_alignment="center", justification="center")],
              #[sg.Column(column_two, vertical_alignment="bottom", justification="center")],
              [sg.Text('RESULTADO',key="RES", justification='center',background_color='#424f5e', expand_x=True,visible=False),sg.FileBrowse(visible=False, key="DIR")],
              [sg.Image(youtube_acess.transform_img(url_logo, 1000, 400), visible=True, key="LOGO"),sg.Column(layout_frame1, scrollable=True, vertical_scroll_only=True, size=(1000, 300*3), key='COLUMN', expand_x=True,visible=False)]
              ]


    window = sg.Window("Downloader MP3 YOUTUBE", layout, finalize=True, size=(1000,600), font=(50), resizable=True)


    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == "Search":
            data = youtube_acess.get_data(values[0])
            tamanho_resultado = len(data)
            print(f"Foram encontrados {tamanho_resultado} resultados")
            colunas_criadas = criar_colunas(window, tamanho_resultado, colunas_criadas)
            atualiza_tela(data, window, tamanho_resultado)


        if event == f"Baixar":
            print(data[0]["link"])
            mp3_down.baixar(data[0]["link"])

        for index in range(0,tamanho_resultado):
            if event == f"Baixar{index}":
                print(data[index+1]["title"])
                print(data[index+1]["link"])
                mp3_down.baixar(data[index+1]["link"])

    window.close()


def atualiza_tela(data, window, tamanho_resultado):
    for index in range(tamanho_resultado):
        print(index, tamanho_resultado)
        window[f"-IMG-{index}"].update(data[index]["thumb"])
    for index in range(tamanho_resultado):
        window[f"-TEXT-{index}"].update(data[index]["title"])
    for index in range(tamanho_resultado):
        window[f"-LINK-{index}"].update(data[index]["link"])
    window.visibility_changed()
    window['COLUMN'].contents_changed()
    window['LOGO'].update(visible=False)
    window['LOGO_PEQ'].update(visible=True)
    window['RES'].update(visible=True)
    window['COLUMN'].update(visible=True)



def criar_colunas(window, tamanho_resultado, colunas_criadas):
    if tamanho_resultado > colunas_criadas:
        for index in range(colunas_criadas, tamanho_resultado):
            print(f"Criou {index} coluna(s)")
            layout = [[frame_img(index), frame_txt(index)]]
            window.extend_layout(window["COLUMN"], layout)
    else:
        print("As colunas que estão criadas, já são suficiente")

    return tamanho_resultado


def frame_img(indice):
    return sg.Frame("", [[sg.Image(youtube_acess.transform_img(),key=f"-IMG-{indice}")]], pad=(5, 3), border_width=0)


def frame_txt(indice):
    return sg.Frame("", [[sg.Text("Video",key=f"-TEXT-{indice}")],
                         [sg.Text("Link:", key=f"-LINK-{indice}")],
                          [sg.Button("Baixar")]],pad=(5, 3),border_width=0, expand_x=True)


if __name__ == "__main__":
    main()