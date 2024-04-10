from random import randint 
from time import sleep
#variavel
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0,2)
#mostrar opções
print('''Suas Opções:
    [0]PEDRA 
    [1]PAPEL
    [2]TESOURA''')
JOGADOR = int(input('Qual sua jogada?'))
#contagem regressiva
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep (1)
print('vai')
sleep(1)
print('-=' * 11)
#escolha de cada jogador
print(f'jogador jogou: {itens[JOGADOR]}')
print(f'computador jogou:{itens[computador]}')
print('-=' * 11)
#sistema de resultados
if computador == 0:
    if JOGADOR == 0:
        print('empate')
        
    elif JOGADOR ==1:
        print('JOGADOR VENCEU!')
        
    elif JOGADOR ==2:
        print('computador venceu!')
        
    else:
        print('jogada invalida')
        