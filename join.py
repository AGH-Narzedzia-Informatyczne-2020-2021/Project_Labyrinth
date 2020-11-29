import labirynth_generator as bk_lab
import PySimpleGUI as sg

sg.theme('Topanga')


def bartek():
    layout = [[sg.Text("Prosty BFS bez argumentów", justification='center', font='Helvetica 15')],
              [sg.Button("Generuj labirynt 10x10", size=(15, 1), font='Helvetica 18')],
              [sg.Button("Zamknij okno", size=(10, 1), font='Helvetica 18')]
              ]
    # Create the Window
    window = sg.Window('Generator labiryntów', layout, size=(500, 200), element_justification='c')
    # Event Loop to process "events"
    while True:
        event, values = window.read()
        print(event, values)
        if event in (None, 'Zamknij okno'):
            break
        if event in (None, 'Generuj labirynt 10x10'):
            bk_lab.generate()
    window.close()


layout = [
    [sg.Text("Witaj! Wybierz jeden z poniższych generatorów labiryntów.", justification='center', font='Helvetica 15')],
    [sg.Text("Naciśnięcie jednego z poniższych przycisków otworzy nowe okno konfiguracji", justification='center',
             font='Helvetica 15')],
    [sg.Button('Prosty BFS bez argumentów', size=(15, 1), font='Helvetica 18')],
    [sg.Button("Zakończ program", size=(10, 1), font='Helvetica 18')]
]
# Create the Window
window = sg.Window('Wybór generatora', layout, size=(550, 280), element_justification='c')
# Event Loop to process "events"
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Zakończ program'):
        break
    if event in (None, 'Prosty BFS bez argumentów'):
        bartek()
window.close()
