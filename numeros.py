import os,sys,time,random

os.system('clear')

main = '''

 _   _ _   _ __  __ _____ ____   ___  ____  
| \ | | | | |  \/  | ____|  _ \ / _ \/ ___| 
|  \| | | | | |\/| |  _| | |_) | | | \___ \ 
| |\  | |_| | |  | | |___|  _ <| |_| |___) |
|_| \_|\___/|_|  |_|_____|_| \_\\___/|____/ 

Powered By Sr Solitario '''

print(main)

def babi(nob):
	for e in nob:
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)

numero = str(input('''Deseja continuar?
>>> '''))

if numero == 'sim':
	babi("CARREGANDO...")
	print
	os.system('clear')
	babi("(########################)")
	print
	os.system('clear')
	print("Numero Gerado Com Sucesso ")
	print(random.randrange(1, 100000000))
  print("Volte Sempre")
else:
	print('Espero que tenha ajudado!!!')

