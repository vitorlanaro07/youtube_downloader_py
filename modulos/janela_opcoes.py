import PySimpleGUI as sg
import os

def janela_opcoes():

    layout = [
        [sg.T("Configurações", font="DEFAULT 25")],
        [sg.Text("Diretório", font="_ 16")],
        [sg.Input(), sg.FolderBrowse("Buscar")],
        [sg.T("Formato", font="_ 16")],
        [sg.R("Audio",1), sg.R("Video",1)],
        [sg.Button("Ok"), sg.Button("Sair")]
    ]

    window = sg.Window("Opções",layout, size=(600,300))

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Sair"):
            window.close()
            return ".m4a", os.getcwd()


        if event == "Ok":
            if values[1] == True:
                tipo = ".m4a"
            elif values[2] == True:
                tipo = ".mp4"
            diretorio = values[0]
            break

    window.close()
    return tipo, diretorio

if __name__ == "main":
    janela_opcoes()