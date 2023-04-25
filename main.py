import os
from threading import Thread
import PySimpleGUI as sg
from modulos import download_audio_video as audio_video
from modulos import janela_principal, janela_opcoes, search_audio_video
from modulos.search_audio_video import pesquisar


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

        os.system('clear')

        if event == "Search":
            zera_lista_de_links()
            tamanho_resultado, data = realiza_busca(values[0])
            sg.PopupAnimated(None)
            atualiza_tela(data, window, tamanho_resultado, colunas_criadas)

        if event == f"Baixar":
            baixar_video(data[0]["link"], dir, tipo)

        for index in range(0,tamanho_resultado):
            if event == f"Baixar{index}":
                baixar_video(data[index+1]["link"], dir, tipo)

        if event == "OPT":
            tipo, dir = janela_opcoes.janela_opcoes()

    window.close()


def baixar_video(data, dir, tipo):
    Thread(target=audio_video.baixar, args=(data, dir, tipo, )).start()

def atualizar_visibilidade_da_janela(window, endereco, visibilidade):
    window[endereco].update(visible=visibilidade)

def atualizar_dados_da_janela(window, endereco, conteudo):
    window[endereco].update(conteudo)

# def buscando(args):
#     sg.PopupAnimated(sg.DEFAULT_BASE64_LOADING_GIF, background_color='white', time_between_frames=100)

def realiza_busca(busca):
    pesquisar(busca)
    tamanho_resultado = len(search_audio_video.lista)
    data = search_audio_video.lista
    return tamanho_resultado, data

def zera_lista_de_links():
    search_audio_video.lista = []
    search_audio_video.links = []

def atualiza_tela(data, window, tamanho_resultado, tamanho_colunas):
    for index in range(0,tamanho_resultado):
        atualizar_dados_da_janela(window, f"-IMG-{index}", data[index]["thumb"])

    for index in range(0,tamanho_resultado):
        atualizar_dados_da_janela(window, f"-TEXT-{index}", data[index]["title"])
        atualizar_dados_da_janela(window, f"-CANAL-{index}", f"Canal: {data[index]['canal']}")
        atualizar_dados_da_janela(window, f"-TIME-{index}", f"Duração: {data[index]['duration']}")
        atualizar_dados_da_janela(window, f"-VIEWS-{index}", "Views: {:,}".format(data[index]['views']))

    for index in range(0, tamanho_resultado):
        atualizar_visibilidade_da_janela(window, f"FRAME-IMG{index}", True)
        atualizar_visibilidade_da_janela(window, f"FRAME-TXT{index}", True)

    for index in range(tamanho_resultado, tamanho_colunas):
        atualizar_visibilidade_da_janela(window, f"FRAME-IMG{index}", False)
        atualizar_visibilidade_da_janela(window, f"FRAME-TXT{index}", False)


    window.visibility_changed()
    window[f'COLUMN'].contents_changed()
    atualizar_visibilidade_da_janela(window, f'COLUMN', True)
    atualizar_visibilidade_da_janela(window, 'LOGO', False)
    atualizar_visibilidade_da_janela(window, 'LOGO_PEQ', True)
    atualizar_visibilidade_da_janela(window, f'OPT', True)
    atualizar_visibilidade_da_janela(window,'TITULO', False)
    window['RES'].update(f"RESULTADO: {tamanho_resultado}",visible=True)


if __name__ == "__main__":
    main()


