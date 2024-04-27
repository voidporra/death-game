import sys
import os
import random
from colorama import Fore, Style

def clear():
    os.system('clear')

def reset():
    clear()
    python = sys.executable
    os.execl(python, python, * sys.argv)

def death():
    print(Fore.RED+'VOCÊ MORREU'+Style.RESET_ALL)
    input('pressione enter para recomeçar a aventura')
    reset()
    

def combat():
    enemynum = (random.randint(1, 10))
    if enemynum > 6:
        death()
    else:
        clear()
        print('você matou o inimigo, parabéns, não tem mais nada nessa porta e você morre de fome.')
        death()

def chest():
    print(Fore.YELLOW+'''         __________
        /\____;;___\.
       | /         /
       `. ())oo() .
        |\(%()*^^()^\.
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|''')
    print(Style.RESET_ALL)

def reddoor():
    print(Fore.RED+'''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|''')
    print(Style.RESET_ALL)
def bluedoor():
    print(Fore.BLUE+'''
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __()|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|''')
    print(Style.RESET_ALL)
    
def monster():
    print(Fore.RED+'''       ,     .
        /(     )\               A
   .--.( `.___.' ).--.         /_}
   `._ `%_&%#%$_ ' _.'     /| <___> |\.
      `|(@\*%%/@)|'       / (  |L|  ) \.
       |  |%%#|  |       J d8bo|=|od8b L
        \ \$#%/ /        | 8888|=|8888 \.
        |\|%%#|/|        J Y8P"|=|"Y8P F
        | (.".)%|         \ (  |L|  ) /
    ___.'  `-'  `.___      \|  |L|  |/
  .'#*#`-       -'$#*`.       / )|
 /#%^#%*_ *%^%_  #  %$%\    .J (__)
 #&  . %%%#% ###%*.   *%\.-'&# (__)
 %*  J %.%#_|_#$.\J* \ %'#%*^  (__)
 *#% J %$%%#|#$#$ J\%   *   .--|(_)
 |%  J\ `%%#|#%%' / `.   _.'   |L|
 |#$%||` %%%$### '|   `-'      |L|''')
    print(Style.RESET_ALL)

def doorchoice():
    reddoor()
    bluedoor()
    print(name, 'se depara com duas portas, deseja entrar pela VERMELHA ou pela AZUL?')
    chooseddoor = input()
    if chooseddoor == 'vermelha':
        monster()
        print('você se encontrou com o minotauro que protege este lado da masmorra, deseja ENFRENTAR ou FUGIR?')
        battlechoice = input()
        if battlechoice == 'enfrentar':
            combat()
        elif battlechoice == 'fugir':
            doorchoice()            
            
    elif chooseddoor == 'azul':
        chest()
        input('parabéns, você achou um baú, pressione enter para ver o que tem dentro')
        clear()
        print('o baú era um monstro')
        death()
    else:
        input('opção inválida, tente novamente')
        doorchoice()

print('''      _            _   _                                  
     | |          | | | |                                 
   __| | ___  __ _| |_| |__     __ _  __ _ _ __ ___   ___ 
  / _` |/ _ \/ _` | __| '_ \   / _` |/ _` | '_ ` _ \ / _ \.
 | (_| |  __/ (_| | |_| | | | | (_| | (_| | | | | | |  __/
  \__,_|\___|\__,_|\__|_| |_|  \__, |\__,_|_| |_| |_|\___|
                                __/ |                     
                               |___/                      ''')
print('olá aventureiro, qual seu nome?')
name = input()


def namecheck():
    clear()
    print('seu nome é ',name,' certo? s/n ')
    check = input()
    if check == 'n':
        reset()
    elif check == 's':
        doorchoice()
    else:
        input('resposta inválida, pressione enter')
        namecheck()

namecheck()