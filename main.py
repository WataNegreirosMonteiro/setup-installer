import os
import time
from tkinter import *
from tkinter import ttk
'''
/*******************************************************************************
 * AUXILIOS
 ******************************************************************************/
'''
def criador_telas(titulo):
  tela = Tk()
  tela.title(titulo)
  tela.geometry('640x480')
  tela.resizable(width=False, height=False)
  ic_sejus = PhotoImage(file='_assets/icone/ic_sejus.png')
  tela.iconphoto(False, ic_sejus)
  return tela
def verificar_credenciais(tela, senha):
  if senha == "!admin@sejus":
    tela.destroy()
    tela_inicio()
'''
/*******************************************************************************
 * TELAS
 ******************************************************************************/
'''
def tela_entrar():
  
  tela = criador_telas('SEJUS - Setup 2023')
  img_fundo =  PhotoImage(file='_assets/telas/tl_entrar.png')
  
  rotulo = Label(tela, image=img_fundo)
  rotulo.pack()
  
  esconder_senha = StringVar()
  entrada_senha = Entry(tela, textvariable=esconder_senha , show='*', highlightthickness=0, bd=0, font=('Inter', 8), justify=LEFT, foreground='#949494')
  entrada_senha.place(width=235, height=26, x=185, y=231)
  
  img_bt_entrar = PhotoImage(file='_assets/botoes/bt_entrar.png')
  bt_entrar = Button(tela, highlightthickness=0, bd=0, background='#1271D8', image=img_bt_entrar, command=lambda: [ verificar_credenciais(tela, entrada_senha.get()) ])
  bt_entrar.place(width=269, height=24, x=183, y=267)
  
  
  tela.mainloop()
def tela_inicio():
  tela = criador_telas('SEJUS - Setup')
  img_fundo =  PhotoImage(file='_assets/telas/tl_iniciar.png')
  
  rotulo = Label(tela, image=img_fundo)
  rotulo.pack()
  
  img_bt_mapear = PhotoImage(file='_assets/botoes/bt_mapear_pastas.png')
  bt_mapear = Button(tela, highlightthickness=0, bd=0, background='#1271D8', image=img_bt_mapear, command=lambda: [ tela.destroy(), tela_mapear() ])
  bt_mapear.place(width=256, height=35, x=192, y=132)
  
  img_bt_admin = PhotoImage(file='_assets/botoes/bt_administrador_local.png')
  bt_admin = Button(tela, highlightthickness=0, bd=0, background='#1271D8', image=img_bt_admin, command=lambda: [ admin_local(), tela.destroy(), tela_finalizado() ])
  bt_admin.place(width=256, height=35, x=192, y=177)
  
  img_bt_dns = PhotoImage(file='_assets/botoes/bt_dns.png')
  bt_dns = Button(tela, highlightthickness=0, bd=0, background='#1271D8', image=img_bt_dns, command=lambda: [ dns(), tela.destroy(), tela_finalizado() ])
  bt_dns.place(width=256, height=35, x=192, y=222)
  
  img_bt_horario = PhotoImage(file='_assets/botoes/bt_ajustar_horario.png')
  bt_horario = Button(tela, highlightthickness=0, bd=0, background='#1271D8', image=img_bt_horario, command=lambda: [ horario(), tela.destroy(), tela_finalizado() ])
  bt_horario.place(width=256, height=35, x=192, y=267)
  
  # img_bt_instalacao = PhotoImage(file='_assets/botoes/bt_instalacao_padrao.png')
  # bt_instalacao = Button(tela, highlightthickness=0, bd=0, background='#1271D8', image=img_bt_instalacao, command=lambda: [ tela.destroy() ])
  # bt_instalacao.place(width=256, height=35, x=192, y=312)
  
  tela.mainloop()
def tela_mapear():
  tela = criador_telas('SEJUS - Mapear')
  img_fundo =  PhotoImage(file='_assets/telas/tl_mapear.png')
  
  rotulo = Label(tela, image=img_fundo)
  rotulo.pack()
  
  cb_disco= ttk.Combobox(
    state='readonly',
    values=['G:', 'H:', 'L:', 'T:', 'W:']
  )
  cb_disco.place(width=217, height=37, x=232, y=178)
  
  cb_setor= ttk.Combobox(
    state='readonly',
    values=[
      'alimentacao', 'almox', 'assejur', 'asserso', 'assimp', 'centi', 'ci', 'cogesp', 'cogespxgespen', 'contabilidade',
      'coordenadoria', 'copen', 'cpd-gespen', 'CPPAD COMISSÃO','CPPAD E.F.M', 'Direx', 'DPP', 'EGPE', 'funedca',
      'fupen', 'gab', 'gaf', 'gafgerencia', 'geap', 'geinf', 'geinfo', 'Gerente', 'Gesau', 'gespen_recam',
      'gespen2', 'gpc', 'grh', 'grh_raimundo', 'mp3', 'npo', 'ouvidoria', 'protocolo', 'recam','stea','todos','transporte',
    ]
  )
  cb_setor.place(width=217, height=37, x=232, y=221)
  
  img_bt_mapear = PhotoImage(file='_assets/botoes/bt_mapear.png')
  bt_mapear = Button(tela, highlightthickness=0, bd=0, background='#1271D8', image=img_bt_mapear, command=lambda: [ mapear(cb_disco.get(), cb_setor.get()), tela.destroy(), tela_finalizado() ])
  bt_mapear.place(width=256, height=35, x=192, y=265)
  
  tela.mainloop()
def tela_finalizado():
  tela = criador_telas('SEJUS - Finalizado!')
  img_fundo =  PhotoImage(file='_assets/telas/tl_finalizado.png')
  
  rotulo = Label(tela, image=img_fundo)
  rotulo.pack()
  
  img_bt_inicio = PhotoImage(file='_assets/botoes/bt_inicio.png')
  bt_inicio = Button(tela, highlightthickness=0, bd=0, background='#1271D8', image=img_bt_inicio, command=lambda: [ tela.destroy(), tela_inicio() ])
  bt_inicio.place(width=93, height=35, x=87, y=415)
  
  tela.mainloop()
def tela_instalar():
  tela = criador_telas('SEJUS - Instalador')
  img_fundo =  PhotoImage(file='_assets/telas/tl_instalacoes.png')
  
  rotulo = Label(tela, image=img_fundo)
  rotulo.pack()
  
  cb_Winrar= ttk.Combobox(
    state='readonly',
    values=['-', 'Winrar']
  )
  cb_Winrar.place(width=115, height=20, x=196, y=201)
  
  cb_WPS= ttk.Combobox(
    state='readonly',
    values=['-', 'WPS']
  )
  cb_WPS.place(width=115, height=20, x=196, y=229)
  
  cb_Chrome= ttk.Combobox(
    state='readonly',
    values=['-', 'Chrome']
  )
  cb_Chrome.place(width=115, height=20, x=196, y=257)
  
  cb_Firefox= ttk.Combobox(
    state='readonly',
    values=['-', 'Firefox']
  )
  cb_Firefox.place(width=115, height=20, x=342, y=201)
  
  cb_Adobe= ttk.Combobox(
    state='readonly',
    values=['-', 'Adobe']
  )
  cb_Adobe.place(width=115, height=20, x=342, y=229)
  
  cb_Kaspersky= ttk.Combobox(
    state='readonly',
    values=['-', 'Kaspersky']
  )
  cb_Kaspersky.place(width=115, height=20, x=342, y=257)
  
  img_bt_instalar = PhotoImage(file='_assets/botoes/bt_instalar.png')
  bt_instalar = Button(tela, highlightthickness=0, bd=0, background='#1271D8', image=img_bt_instalar, command=lambda: [ 
    instalador(cb_Winrar.get(),
               cb_WPS.get(),
               cb_Chrome.get(),
               cb_Firefox.get(),
               cb_Adobe.get(),
               cb_Kaspersky.get()
    )])
  bt_instalar.place(width=256, height=36, x=192, y=311)
  
  tela.mainloop()
'''
/*******************************************************************************
 * AÇÕES
 ******************************************************************************/
'''
def mapear(disco, setor):
  netuse = 'net use .F:. \.\.172.16.123.6\Setores\.'
  admin = '/user:sejus\.tvictor !admin@sejus'
  netuse = netuse.split('.')
  admin = admin.split('.')
  
  os.system(netuse[0]+disco+netuse[2]+netuse[3]+netuse[4]+'.'+netuse[5]+'.'+netuse[6]+'.'+netuse[7]+setor+' '+admin[0]+admin[1])
  time.sleep(2)
def admin_local():
  os.system('net user administrador /active:yes && net user Administrador !sejus%%geinfo#')
  time.sleep(2)
def dns():
  os.system('netsh interface ipv4 add dnsserver "Ethernet" address=172.16.0.66 index=1')
  time.sleep(2)
def horario():
  os.system('w32tm /resync')
  time.sleep(2)
def instalador(winrar, wps, chrome, firefox, adobe, kaspersky):
  print(winrar+ wps+ chrome+ firefox+ adobe+ kaspersky)
'''
--------------------------------------------------------------------------------
'''
tela_instalar()