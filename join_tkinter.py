from tkinter import *
import labirynth_generator as bk_lab
from tkinter import messagebox as msgbox
import PyMazeDFS
import PyMazeBFS
import DFS_generator.mazeToGraphic as mazeToGraphic
import prim as prim
import binary_tree as bintree


def on_closing():
    if msgbox.askokcancel("Quit", "Do you want to quit?"):
        root.quit()


def konrad_bfs():
    root = Tk()
    root.title('Generuj labirynt')

    # Designate Height and Width of our app
    app_width = 400
    app_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    my_label = Label(root, text=f'Labirynt generowany algorytmem BFS')
    my_label.pack(pady=10)

    my_label2 = Label(root, text=f'Podaj wymiar N labiryntu:')
    my_label2.pack(pady=10)

    canvas1 = Canvas(root, width=90, height=75)
    canvas1.pack()

    entry1 = Entry(root)
    canvas1.create_window(40, 25, window=entry1)

    B = Button(root, text="Generuj Labirynt dla NxN", command=lambda: PyMazeBFS.generate(int(entry1.get())))
    B.pack()

    D = Button(root, text="Zamknij okno", command=lambda: root.destroy())
    D.pack(pady=10)

    root.mainloop()


def konrad_dfs():
    root = Tk()
    root.title('Generuj labirynt')

    # Designate Height and Width of our app
    app_width = 400
    app_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    my_label = Label(root, text=f'Labirynt generowany algorytmem DFS')
    my_label.pack(pady=10)

    my_label2 = Label(root, text=f'Podaj wymiar N labiryntu:')
    my_label2.pack(pady=10)

    canvas1 = Canvas(root, width=90, height=75)
    canvas1.pack()

    entry1 = Entry(root)
    canvas1.create_window(40, 25, window=entry1)

    B = Button(root, text="Generuj Labirynt dla NxN", command=lambda: PyMazeDFS.generate(int(entry1.get())))
    B.pack()

    D = Button(root, text="Zamknij okno", command=lambda: root.destroy())
    D.pack(pady=10)

    root.mainloop()


def lukasz_hex():
    root = Tk()
    root.title('Generuj labirynt')

    # Designate Height and Width of our app
    app_width = 400
    app_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    my_label = Label(root, text=f'Labirynt heksagonalny generowany algorytmem DFS')
    my_label.pack(pady=10)

    my_label2 = Label(root, text=f'Podaj promien N labiryntu (2-30):')
    my_label2.pack(pady=10)

    canvas1 = Canvas(root, width=90, height=75)
    canvas1.pack()

    entry1 = Entry(root)
    canvas1.create_window(40, 25, window=entry1)

    B = Button(root, text="Generuj Labirynt dla promienia N", command=lambda: mazeToGraphic.generate(int(entry1.get())))
    B.pack()

    D = Button(root, text="Zamknij okno", command=lambda: root.destroy())
    D.pack(pady=10)

    root.mainloop()


def pawel():
    root = Tk()
    root.title('Generuj labirynt')

    # Designate Height and Width of our app
    app_width = 400
    app_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    my_label = Label(root, text=f'Labirynt generowany algorytmem BFS wersja 2')
    my_label.pack(pady=10)

    my_label2 = Label(root, text=f'Podaj wymiar N labiryntu:')
    my_label2.pack(pady=10)

    canvas1 = Canvas(root, width=90, height=75)
    canvas1.pack()

    entry1 = Entry(root)
    canvas1.create_window(40, 25, window=entry1)

    B = Button(root, text="Generuj Labirynt dla NxN", command=lambda: bintree.pawel_tree(int(entry1.get())))
    B.pack()

    D = Button(root, text="Zamknij okno", command=lambda: root.destroy())
    D.pack(pady=10)

    root.mainloop()


def hania():
    root = Tk()
    root.title('Generuj labirynt')

    # Designate Height and Width of our app
    app_width = 400
    app_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    my_label = Label(root, text=f'Labirynt generowany algorytmem Prima')
    my_label.pack(pady=10)

    my_label2 = Label(root, text=f'Podaj wymiar N labiryntu:')
    my_label2.pack(pady=10)

    canvas1 = Canvas(root, width=90, height=75)
    canvas1.pack()

    entry1 = Entry(root)
    canvas1.create_window(40, 25, window=entry1)

    B = Button(root, text="Generuj Labirynt dla NxN", command=lambda: prim.hania_prim(int(entry1.get())))
    B.pack()

    D = Button(root, text="Zamknij okno", command=lambda: root.destroy())
    D.pack(pady=10)

    root.mainloop()


def bartek():
    root = Tk()
    root.title('Generuj labirynt')

    # Designate Height and Width of our app
    app_width = 400
    app_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    my_label = Label(root, text=f'Labirynt generowany algorytmem BFS wersja 2')
    my_label.pack(pady=10)

    my_label2 = Label(root, text=f'Podaj wymiar N labiryntu:')
    my_label2.pack(pady=10)

    canvas1 = Canvas(root, width=90, height=75)
    canvas1.pack()

    entry1 = Entry(root)
    canvas1.create_window(40, 25, window=entry1)

    B = Button(root, text="Generuj Labirynt dla NxN", command=lambda: bk_lab.generate(int(entry1.get())))
    B.pack()

    D = Button(root, text="Zamknij okno", command=lambda: root.destroy())
    D.pack(pady=10)

    root.mainloop()


root = Tk()
root.title('Wybór generatora')

# Designate Height and Width of our app
app_width = 500
app_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

my_label = Label(root, text=f'Witaj! Wybierz jeden z poniższych generatorów labiryntów.')
my_label.pack(pady=10)

my_label2 = Label(root, text=f'Naciśnięcie jednego z poniższych przycisków otworzy nowe okno konfiguracji')
my_label2.pack()

B = Button(root, text="BFS wersja 2", command=lambda: bartek())
B.pack(pady=10)

H = Button(root, text="Prim", command=lambda: hania())
H.pack(pady=10)

H = Button(root, text="Generator Pawla", command=lambda: pawel())
H.pack(pady=10)

L = Button(root, text="Heksagonalny DFS", command=lambda: lukasz_hex())
L.pack(pady=10)

P1 = Button(root, text="Generator Konrada dfs", command=lambda: konrad_dfs())
P1.pack(pady=10)

P2 = Button(root, text="Generator konrada bfs", command=lambda: konrad_bfs())
P2.pack(pady=10)

Q = Button(text="Zamknij program", command=lambda: root.quit())
Q.pack(pady=10)
# root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
