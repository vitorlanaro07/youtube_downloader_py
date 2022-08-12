import os
from threading import Thread
import PySimpleGUI as sg
from modulos import download_audio_video as audio_video
from modulos import janela_principal, janela_opcoes, search_audio_video
from modulos.search_audio_video import pesquisar


def baixar_video(data, dir, tipo):
    Thread(target=audio_video.baixar, args=(data, dir, tipo, )).start()


def main():
    #default
    dir = os.getcwd()
    tipo = ".m4a"
    data = None
    window = janela_principal.janela_principal() #janela_principal.janela_principal()

    colunas_criadas = 30
    tamanho_resultado = 0

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        # os.system('clear')


        if event == "Search":
            zera_lista_de_links()
            tamanho_resultado = realiza_busca(values[0])
            data = search_audio_video.lista
            atualiza_tela(data, window, tamanho_resultado, colunas_criadas)

        if event == f"Baixar":
            baixar_video(data[0]["link"], dir, tipo)


        for index in range(0,tamanho_resultado):
            if event == f"Baixar{index}":
                baixar_video(data[index+1]["link"], dir, tipo)

        if event == "OPT":
            tipo, dir = janela_opcoes.janela_opcoes()

    window.close()

# def apresentar_gif():
#     sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', time_between_frames=100)
#     sg.PopupAnimated(None)
def realiza_busca(busca):
    pesquisar(busca)
    tamanho_resultado = len(search_audio_video.lista)
    return tamanho_resultado
def zera_lista_de_links():
    search_audio_video.lista = []
    search_audio_video.links = []

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

    # for index in range()

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


