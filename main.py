import PySimpleGUI as sg

sg.theme("DarkAmber")

column_one = [
    [sg.Text("Dowloader Youtube")]
]

column_two = [
    [sg.Input(),sg.Button("Search")]
]

layout = [
    [sg.Column(column_one, vertical_alignment="center", justification="center")],
    [sg.Column(column_two, vertical_alignment="bottom", justification="center")],
    [sg.Text(key="-RESULT-")]
]

window = sg.Window("Downloader MP3 YOUTUBE", layout, finalize=True, size=(800,600), font=(50))

while True:
    event, values = window.read()
    print(event, values)

    if event == sg.WINDOW_CLOSED:
        break

    if event == "Search":
        window["-RESULT-"].update(values[0])


window.close()