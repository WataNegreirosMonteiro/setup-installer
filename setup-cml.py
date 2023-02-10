import os
import time
import subprocess, sys    

#helpers
def timer():
      print('1.')
      time.sleep(1)
      os.system('cls')
      print('2..')
      time.sleep(1)
      os.system('cls')
      print('3...')
      time.sleep(1)
      os.system('cls')
#------------

def start():
      os.system('cls')
      try:
            option = int(input('''
      ╔════════[SETUP - SEJUS]════════╗
      ╟-> 1 | Mapear pastas           ║
      ╟-> 2 | Admin local             ║
      ╟-> 3 | Dns                     ║ 
      ╟-> 5 | Ajustar_horario         ║
      ╠═══════════════════════════════╝ 
      ╚════>> '''))
            if option == 1:
                  map_dir()
            if option == 2:
                  local_admin()
            if option == 3:
                  dns()
            if option == 5:
                  set_time()
            else:
                  print('OPCAO INVALIDA!')
                  time.sleep(2)
                  start()
      
      except:
            print('OPCAO INVALIDA!')
            time.sleep(2)
            start()

def map_dir():
      os.system('cls')
      dir=[
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
      
      for sector in dir:
            print(f'>> {sector}')
      
      dir_to_map = input('Digite o nome do setor: ')
      if dir_to_map in dir:
            
            netuse = 'net use G: \.\.172.16.123.6\Setores\.'
            admin = '/user:sejus\.tvictor !admin@sejus'
            netuse = netuse.split('.')
            admin = admin.split('.')
            
            os.system(netuse[0]+netuse[1]+netuse[2]+'.'+netuse[3]+'.'+netuse[4]+'.'+netuse[5]+dir_to_map+' '+admin[0]+admin[1])
            print(f'{dir_to_map} foi mapeada com sucesso! Redirecionando...')
            timer()
            start()
      else:
            print('NOME INVALIDO!')
            time.sleep(2)
            map_dir()

def local_admin():
  os.system('cls')
  try:
    print('Adicionando administrador...')
    time.sleep(2)
    os.system('net user administrador /active:yes && net user Administrador !sejus%%geinfo#')
    print('Adicionado com sucesso. Redirecionando...')
    time.sleep(5)
    timer()
    start()
  except:
    print('Erro inesperado...')
    time.sleep(3)
    local_admin()

def dns():
  os.system('cls')
  try:
    print('Adicionando DNS padrão SETIC')
    os.system('netsh interface ipv4 add dnsserver "Ethernet" address=172.16.0.66 index=1')
    time.sleep(5)
    timer()
    start()
  except:
    print('Erro inesperado...')
    time.sleep(3)
    dns()
  
def set_time():
  os.system('cls')
  try:
    print('Ajustando horário windows')
    os.system('w32tm /resync')
    time.sleep(5)
    timer()
    start()
  except:
    print('Erro inesperado...')
    time.sleep(3)
    set_time()
    
start()