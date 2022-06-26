import PySimpleGUI as sg
from modulos import web_scraping_youtube_link_and_label as youtube_acess



def frame_img(indice):
    return sg.Frame("", [[sg.Image(youtube_acess.transform_img(),key=f"-IMG-{indice}")]], pad=(5, 3), border_width=0)

def frame_txt(indice):
    return sg.Frame("", [[sg.Text("Video",key=f"-TEXT-{indice}")],
                          [sg.Button("Baixar")]],pad=(5, 3),border_width=0, expand_x=True)

def main():
    font = ('Courier New', 11)
    sg.theme('DarkBlue3')
    sg.set_options(font=font)
    tamanho_resultado = 0
    colunas_criadas = 0

    column_one = [[sg.Text("Dowloader Youtube")]]
    column_two = [[sg.Input(),sg.Button("Search")]]

    layout_frame1 = [
        [frame_img(colunas_criadas), frame_txt(colunas_criadas)],
    ]


    layout = [[sg.Column(column_one, vertical_alignment="center", justification="center")],
              [sg.Column(column_two, vertical_alignment="bottom", justification="center")],
              [sg.Text('RESULTADO',key="RES-", justification='center', background_color='#424f5e', expand_x=True,visible=False)],
              [sg.Column(layout_frame1, scrollable=True, vertical_scroll_only=True, size=(1000, 300*3), key='COLUMN', expand_x=True, visible=False)]
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


    window.close()


def atualiza_tela(data, window, tamanho_resultado):
    for index in range(tamanho_resultado):
        print(index, tamanho_resultado)
        window[f"-IMG-{index}"].update(data[index]["thumb"])
    for index in range(tamanho_resultado):
        window[f"-TEXT-{index}"].update(data[index]["title"])
    window.visibility_changed()
    window['COLUMN'].contents_changed()
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


if __name__ == "__main__":
    main()