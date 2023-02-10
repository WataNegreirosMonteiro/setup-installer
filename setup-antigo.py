from tkinter import *
from tkinter import ttk
import tkinter as tk
import os


def create_screen(title):
    screen = Tk()
    screen.title(title)
    screen.geometry('640x480')
    screen.resizable(width=False, height=False)
    iconScreen = PhotoImage(file="./assets/logo.png")
    screen.iconphoto(False, iconScreen)
    return screen

def start():
    screen = create_screen('SEJUS - Suporte')
    background =  PhotoImage(file='./assets/home.png')

    label = Label(screen, image=background)
    label.pack()
    
    img_btn_mapear = PhotoImage(file='./assets/btn_mapear.png')
    btn_mapear = Button(screen, highlightthickness=0, bd=0, background='#FFD439', image=img_btn_mapear, command=lambda:
    [    
        screen.destroy(),
        mapear()
    ])
    btn_mapear.place(width=297, height=25, x=172, y=232)
    
    img_btn_setup = PhotoImage(file='./assets/btn_setup.png')
    btn_setup = Button(screen, highlightthickness=0, bd=0, background='#FFD439', image=img_btn_setup, command=lambda:
    [    
        screen.destroy(),
        mapear
    ])
    btn_setup.place(width=297, height=25, x=172, y=302)
    
    screen.mainloop()
    
def mapear():
    screen = create_screen('SEJUS - Suporte')
    background =  PhotoImage(file='./assets/mapear.png')

    label = Label(screen, image=background)
    label.pack()
    combo = ttk.Combobox(
        state="readonly",
        values=[
        'alimentacao',
        'almox',
        'assejur',
        'asserso',
        'assimp',
        'centi',
        'ci',
        'cogesp',
        'cogespxgespen',
        'contabilidade',
        'coordenadoria',
        'copen',
        'cpd-gespen',
        'CPPAD COMISSÃO',
        'CPPAD E.F.M',
        'Direx',
        'DPP',
        'EGPE',
        'funedca',
        'fupen',
        'gab',
        'gaf',
        'gafgerencia',
        'geap',
        'geinf',
        'geinfo',
        'Gerente',
        'Gesau',
        'gespen_recam',
        'gespen2',
        'gpc',
        'grh',
        'grh_raimundo',
        'mp3',
        'npo',
        'ouvidoria',
        'protocolo',
        'recam',
        'stea',
        'todos',
        'transporte',
    ]
    )
    combo.place(width=297, height=25, x=172, y=232)
    
    
    netuse = 'net use G: \.\.172.16.123.6\Setores\.'
    admin = '/user:sejus\.tvictor !admin@sejus'
    netuse = netuse.split('.')
    admin = admin.split('.')
    
    img_btn_mapear = PhotoImage(file='./assets/btn_mapear.png')
    btn_mapear = Button(screen, highlightthickness=0, bd=0, background='#FFD439', image=img_btn_mapear, command=lambda:
    [    
        os.system(netuse[0]+netuse[1]+netuse[2]+'.'+netuse[3]+'.'+netuse[4]+'.'+netuse[5]+combo.get()+' '+admin[0]+admin[1]),
        screen.destroy(),
        finalizar()
    ])
    btn_mapear.place(width=297, height=25, x=172, y=302)
    

    screen.mainloop()

def finalizar():
    screen = create_screen('SEJUS - Suporte')
    background =  PhotoImage(file='./assets/finalizado.png')
    
    label = Label(screen, image=background)
    label.pack()
    
    img_btn_home = PhotoImage(file='./assets/btn_home.png')
    btn_home = Button(screen, highlightthickness=0, bd=0, background='#FFD439', image=img_btn_home, command=lambda:
    [    
        screen.destroy(),
        start()
    ])
    btn_home.place(width=28, height=28, x=551, y=389)
    
    screen.mainloop()

start()