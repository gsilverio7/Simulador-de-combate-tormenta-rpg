#Simulador de kombate

import random

print('Simulador de kombate (Sistema Tormenta RPG) v1.0 por Gabriel Silvério.')
print('')

#Koleta de dados!------------------------------------------------------------------------------------------------------
n1 = input ('Digite o nome do primeiro kombatente: ')
ca1 = int (input ('Qual sua classe de armadura? '))
a1 = int (input ('Qual seu valor de ataque?(BBA+Atk arma) '))
nd1 = int (input ('Qual seu valor de ataque? Digite primeiro quantos dados serão rolados '))
d1 = int (input(', qual tipo de dado será rolado. '))
df1 = int (input('e agora qual seu dano fixo (derivado do modificador de força caso atacante melee) '))
m1 = int (input ('Qual o valor da ameaça (crítico)? Primeiro digite a partir de que numero o ataque é considerado crítico '))
mm1 = int (input ('e agora qual o multiplicador de crítico '))
v1 = int (input ('Quantos pontos de vida? '))
i1 = int (input ('Qual o valor da iniciativa? '))

print('')
print('ok.')
print('')

n2 = input ('Digite o nome do segundo kombatente: ')
ca2 = int (input ('Qual sua classe de armadura? '))
a2 = int (input ('Qual seu valor de ataque?(BBA+Atk arma) '))
nd2 = int (input ('Qual seu valor de ataque? Digite primeiro quantos dados serão rolados '))
d2 = int (input (', qual tipo de dado será rolado. '))
df2 = int (input('e agora qual seu dano fixo (derivado do modificador de força caso atacante melee) '))
m2 = int (input ('Qual o valor da ameaça (crítico)? Primeiro digite a partir de que numero o ataque é considerado crítico '))
mm2 = int (input ('e agora qual o multiplicador de crítico '))
v2 = int (input ('Quantos pontos de vida? '))
i2 = int (input ('Qual o valor da iniciativa? '))
print('')
print('ok.')
print('')

#Kombate!---------------------------------------------------------------------------------------------------------
ki1=0
ki2=0
while ki1 == ki2:
    dado1 = random.randint(1,20)
    dado2 = random.randint(1,20)
    ki1 = i1 + dado1
    ki2 = i2 + dado2
    print ('Dado1:{}, Dado2:{}'.format(dado1,dado2))
    print ('Iniciativas iguais, re-rolling dices.' if ki1==ki2 else '' )

print ('A iniciativa de {} é {} e a de {} é {}'.format(n1,ki1,n2,ki2))

t = 0

if ki1 > ki2:
    print('{} atacará primeiro!'.format(n1))
    while v1 > 0 and v2 > 0:
        t = t + 1
        print('{} turno! Vez do Kombatente {}!'.format(t, n1))
        dado = random.randint(1, 20)
        print('Jogador UM rola o dado de ataque! o resultado é: ', dado)
        ka1 = a1 + dado
        print('Ataque de {} no turno {} é: {}'.format(n1, t, ka1))
        if dado >= m1:
            kritico = 1
            print('Lá vem acerto krítico!')
        else:
            kritico = 0
        if ka1 > ca2 or kritico == 1:
            print('{} acertou o ataque!'.format(n1))
            kd1=df1
            di=0
            for i in range (0, nd1):
                di = di + 1
                dado = random.randint(1,d1)
                kd1 = kd1 + dado
                print ('Jogador UM obteve um resultado {} no {} dado de ataque.'.format(dado,di))
            if kritico == 1:
                kd1 = kd1*mm1
            else:
                kd1 = kd1
            print ('O dano total dessa jogada de ataque é: ',kd1)
            v2 = v2 - kd1
            print('{} subtraiu {} pontos de vida de {} com seu ataque!'.format(n1,kd1,n2))
            print('Os pontos de vida atuais de {} são: {}.'.format(n2,v2))


        else:
            print('{} não foi bem-sucedido em seu ataque!'.format(n1))
        if v2 > 0:
            print('{} ainda está de pé!'.format(n2))
            print('{} turno! Vez do Kombatente {}!'.format(t, n2))
            dado = random.randint(1, 20)
            print('Jogador DOIS rola o dado de ataque! o resultado é: ', dado)
            ka2 = a2 + dado
            print('Ataque de {} no turno {} é: {}'.format(n2, t, ka2))
            if dado >= m2:
                kritico = 1
                print('Lá vem acerto krítico!')
            else:
                kritico = 0
            if ka2 > ca1 or kritico == 1:
                print('{} acertou o ataque!'.format(n2))
                kd2 = df2
                di = 0
                for i in range(0, nd2):
                    di = di + 1
                    dado = random.randint(1, d2)
                    kd2 = kd2 + dado
                    print('Jogador UM obteve um resultado {} no {} dado de ataque.'.format(dado, di))
                if kritico == 1:
                    kd2 = kd2 * mm2
                else:
                    kd2 = kd2
                print('O dano total dessa jogada de ataque é: ', kd2)
                v1 = v1 - kd2
                print('{} subtraiu {} pontos de vida de {} com seu ataque!'.format(n2, kd2, n1))
                print('Os pontos de vida atuais de {} são: {}.'.format(n1, v1))

                if v1 <= 0:
                    print ('{} não suportou os ferimentos!'.format(n1))
                else:
                    print ('{} ainda está de pé!'.format(n1))


            else:
                print('{} não foi bem-sucedido em seu ataque!'.format(n2))
        else:
            print('{} não suportou os ferimentos!'.format(n2))


else:
    print('{} atacará primeiro!'.format(n2))
    while v1 > 0 and v2 > 0:
        t = t + 1
        print('{} turno! Vez do Kombatente {}!'.format(t, n2))
        dado = random.randint(1, 20)
        print ('Jogador DOIS rola o dado de ataque! o resultado é: ',dado)
        ka2 = a1 + dado
        print('Ataque de {} no turno {} é: {}'.format(n2, t, ka2))
        if dado >= m1:
            kritico = 1
            print('Lá vem acerto krítico!')
        else:
            kritico = 0
        if ka2 > ca1 or kritico == 1:
            print('{} acertou o ataque!'.format(n2))
            kd2 = df2
            di = 0
            for i in range(0, nd2):
                di = di + 1
                dado = random.randint(1, d1)
                kd2 = kd2 + dado
                print('Jogador DOIS obteve um resultado {} no {} dado de ataque.'.format(dado, di))
            if kritico == 1:
                kd2 = kd2*mm2
            else:
                kd2 = kd2
            print ('O dano total dessa jogada de ataque é: ',kd2)
            v1 = v1 - kd2
            print('{} subtraiu {} pontos de vida de {} com seu ataque!'.format(n2,kd2,n1))
            print('Os pontos de vida atuais de {} são: {}.'.format(n1,v1))

        else:
            print('{} não foi bem-sucedido em seu ataque!'.format(n2))
        if v1 > 0:
            print('{} ainda está de pé!'.format(n1))
            print('{} turno! Vez do Kombatente {}!'.format(t, n1))
            dado = random.randint(1, 20)
            print('Jogador UM rola o dado de ataque! o resultado é: ', dado)
            ka1 = a1 + dado
            print('Ataque de {} no turno {} é: {}'.format(n1, t, ka1))
            if dado >= m1:
                kritico = 1
                print('Lá vem acerto krítico!')
            else:
                kritico = 0
            if ka1 > ca2 or kritico == 1:
                print('{} acertou o ataque!'.format(n1))
                kd1 = df1
                di = 0
                for i in range(0, nd1):
                    di = di + 1
                    dado = random.randint(1, d1)
                    kd2 = kd1 + dado
                    print('Jogador UM obteve um resultado {} no {} dado de ataque.'.format(dado, di))
                if kritico == 1:
                    kd1 = kd1 * mm1
                else:
                    kd1 = kd1
                print('O dano total dessa jogada de ataque é: ', kd1)
                v2 = v2 - kd1
                print('{} subtraiu {} pontos de vida de {} com seu ataque!'.format(n1, kd1, n2))
                print('Os pontos de vida atuais de {} são: {}.'.format(n2, v2))

                if v1 <= 0:
                    print('{} não suportou os ferimentos!'.format(n2))
                else:
                    print('{} ainda está de pé!'.format(n2))


            else:
                print('{} não foi bem-sucedido em seu ataque!'.format(n1))
        else:
            print('{} não suportou os ferimentos!'.format(n1))

if v1 > 0:
    print ('{} foi o grande vencedor!'.format(n1))
else:
    print (n2,'foi o grande vencedor!')

print('Dados do combate: Número de turnos: {}'.format(t))
