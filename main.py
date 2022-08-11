import os
import threading, queue
import PySimpleGUI as sg
from modulos import download_audio_video as audio_video
from modulos import janela_principal, janela_opcoes
from modulos import search_audio_video
from modulos.search_audio_video import lista

def main():
    #default
    dir = os.getcwd()
    tipo = ".m4a"


    window = janela_principal.janela_principal() #janela_principal.janela_principal()

    colunas_criadas = 30
    tamanho_resultado = 0

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        os.system('clear')

        if event == "Search":
            search_audio_video.lista = []
            data = search_audio_video.get_data(values[0])
            tamanho_resultado = len(data)
            atualiza_tela(data, window, tamanho_resultado, colunas_criadas)

        if event == f"Baixar":
            threading.Thread(target=audio_video.baixar, args=[data[0]["link"], dir, tipo, ]).start()

        for index in range(0,tamanho_resultado):
            if event == f"Baixar{index}":
                threading.Thread(target=audio_video.baixar, args=[data[index+1]["link"], dir, tipo, ]).start()

        if event == "OPT":
            tipo, dir = janela_opcoes.janela_opcoes()

    window.close()


def atualiza_tela(data, window, tamanho_resultado, tamanho_colunas):
    for index in range(0,tamanho_resultado):
        window[f"-IMG-{index}"].update(data[index]["thumb"])

    for index in range(0,tamanho_resultado):
        window[f"-TEXT-{index}"].update(data[index]["title"])
        window[f"-CANAL-{index}"].update(f"Canal: {data[index]['canal']}")
        window[f"-TIME-{index}"].update(f"Duração: {data[index]['duration']}")
        window[f"-VIEWS-{index}"].update("Views: {:,}".format(data[index]['views']))

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
    window['OPT'].update(visible=True)
    window["TITULO"].update(visible=False)
    window['RES'].update(f"RESULTADO: {tamanho_resultado}",visible=True)




if __name__ == "__main__":
    main()


