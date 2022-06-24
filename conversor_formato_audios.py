from pydub import AudioSegment
import os
import PySimpleGUI as sg

sg.theme("DarkAmber")

column_two = [
    [sg.Text("Selecione o arquivo de áudio:", font=20)],
    [sg.Input(key='-IN1-', size=(70,2)), sg.FilesBrowse('Buscar')],
    [sg.Text("Arquivo:", visible=False, key="-TXT1-", font=20), sg.Text(key="-NOME-",visible=False)],
    [sg.Text("Novo Formato:", visible=False, key="-TXT2-", font=20), sg.Combo(["mp3", "wav", "m4a", "aac"], visible=False, key="-COMBO-")]
]

column_three=[
        [sg.Text("Selecione o novo diretório:", font=20)],
        [sg.Input(key='-IN2-', size=(70, 2)), sg.FolderBrowse('Buscar')],
        [sg.Button("Converter")]
]


layout = [
    [sg.Column(column_two, vertical_alignment="center", justification="center")],
    [sg.Column(column_three, vertical_alignment="bottom", justification="center",key="-COLUM3-",visible=False)],
]

window = sg.Window("Conversor de áudio", layout, finalize=True, size=(630,300))

while True:
    event, values = window.read(timeout=1000)


    if event == sg.WINDOW_CLOSED:
        break

    try:
        dir = values["-IN1-"]
        name = os.path.basename(dir)
        nome, ext = name.split(".")
        window["-NOME-"].update(name)
    except:
        pass

    if values["-IN1-"] != "":
        window["-TXT1-"].update(visible=True)
        window["-NOME-"].update(visible=True)
        window["-TXT2-"].update(visible=True)
        window["-COMBO-"].update(visible=True)
        window["-COLUM3-"].update(visible=True)

    if event == "Converter":
        ext_export = values["-COMBO-"]
        dir_export = str(values["-IN2-"] + "/" + nome + "."+ ext_export)
        audio = AudioSegment.from_file(dir, format=ext)
        audio.export(dir_export, format=ext_export)


window.close()

