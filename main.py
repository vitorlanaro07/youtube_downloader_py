import PySimpleGUI as sg
from modulos import web_scraping_youtube_link_and_label as youtube_acess
from modulos import downloader_mp3_yotube as mp3_down

url_logo = "https://logodownload.org/wp-content/uploads/2014/10/youtube-logo-0-2048x2048.png"

def main():
    font = ('Courier New', 11)
    sg.theme('DarkBlue3')
    sg.set_options(font=font)
    colunas_criadas = 30
    tamanho_resultado = 0

    column = [[sg.Text("Downloader Youtube",justification="Center")],
              [sg.Input(),sg.Button("Search")]]

    print("Criando Colunas...")
    layout_cre = [
        [frame_img(x), frame_txt(x)] for x in range(0,30)
    ]

    layout = [[sg.Image(youtube_acess.transform_img(url_logo, 300, 150), visible=False, key="LOGO_PEQ"), sg.Column(column, vertical_alignment="center", justification="center")],
              [sg.Text(key="RES", justification='center',background_color='#424f5e', expand_x=True,visible=False)],
              [sg.Image(youtube_acess.transform_img(url_logo, 1000, 400), visible=True, key="LOGO"),
               [sg.Column(layout_cre, key=f'COLUMN',visible=False,  scrollable=True, vertical_scroll_only=True, size=(1200, 300*3))]] #, expand_x=True,visible=False
              ]

    window = sg.Window("Downloader MP3 YOUTUBE", layout, finalize=True, size=(1000,600), font=(50), resizable=True)


    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == "Search":
            data = youtube_acess.get_data(values[0])
            print("Requisição feita!")
            tamanho_resultado = len(data)
            atualiza_tela(data, window, tamanho_resultado, colunas_criadas)


        if event == f"Baixar":
            print(data[0]["link"])
            mp3_down.baixar(data[0]["link"])

        for index in range(0,tamanho_resultado):
            if event == f"Baixar{index}":
                print(data[index+1]["title"])
                print(data[index+1]["link"])
                mp3_down.baixar(data[index+1]["link"])

    window.close()



def atualiza_tela(data, window, tamanho_resultado, tamanho_colunas):
    for index in range(0,tamanho_resultado):
        window[f"-IMG-{index}"].update(data[index]["thumb"])

    for index in range(0,tamanho_resultado):
        window[f"-TEXT-{index}"].update(data[index]["title"])
        window[f"-LINK-{index}"].update(f"Link: {data[index]['link']}")
        window[f"-TIME-{index}"].update(f"Duração: {data[index]['duration']}")
    #for index in range(0,tamanho_resultado):



    for index in range(0, tamanho_resultado):
        window[f"FRAME-IMG{index}"].update(visible=True)
        window[f"FRAME-TXT{index}"].update(visible=True)

    for index in range(tamanho_resultado, tamanho_colunas):
        window[f"FRAME-IMG{index}"].update(visible=False)
        window[f"FRAME-TXT{index}"].update(visible=False)

    window.visibility_changed()
    window[f'COLUMN'].contents_changed()
    window[f'COLUMN'].update(visible=True)
    window['LOGO'].update(visible=False)
    window['LOGO_PEQ'].update(visible=True)
    window['RES'].update(f"RESULTADO: {tamanho_resultado}",visible=True)




def frame_img(index):
    return sg.Frame("", [[sg.Image(youtube_acess.transform_img(),key=f"-IMG-{index}")]], key=f"FRAME-IMG{index}", pad=(5, 3), border_width=0, visible=False)


def frame_txt(index):
    return sg.Frame("", [[sg.Text("",key=f"-TEXT-{index}")],
                         [sg.Text("",key=f"-LINK-{index}")],
                         [sg.Text("",key=f"-TIME-{index}")],
                          [sg.Button("Baixar")]], key=f"FRAME-TXT{index}",pad=(5, 3),border_width=0, expand_x=True, visible= False)


if __name__ == "__main__":
    main()