import random
import time

print('='*40)
print('  Vamos jogar PEDRA, PAPEL ou TESOURA?')
print('='*40)

escolha = int(input('Digite:\n[0] para PEDRA\n[1] para PAPEL\n[2] para TESOURA\nR:'))

maquina = [0, 1, 2]

maquinaescolha = random.choice(maquina)

print('\nVocê escolheu: ', end='')

time.sleep(1)

if escolha == 0:
    print('PEDRA!')
elif escolha == 1:
    print('PAPEL!')
else:
    print('TESOURA!')

print('\nO computador escolheu: ', end='')

time.sleep(1)

if maquinaescolha == 0:
    print('PEDRA!')
elif maquinaescolha == 1:
    print('PAPEL!')
else:
    print('TESOURA!')

if escolha == maquinaescolha:
    print('EMPATE!')
elif escolha == 0 and maquinaescolha == 1:
    print('Você perdeu!')
elif escolha == 1 and maquinaescolha == 0:
    print('Você ganhou! :(')
elif escolha == 1 and maquinaescolha == 2:
    print('Você perdeu!')
elif escolha == 2 and maquinaescolha == 1:
    print('Você ganhou!')
elif escolha == 0 and maquinaescolha == 2:
    print('Você ganhou!')
elif escolha == 2 and maquinaescolha == 0:
    print('Você perdeu!')
