import bonitesas as bn
from time import sleep
from teste_poo import *
bn.titulo('regra de 3')
print('escolha se a regra de 3 é simples ou composta')
escolha = input('escolha [simples] ou [composta]').upper()
sleep(2)
if escolha == 'COMPOSTA':
    print('''para regras de 3 composta nos precisamos definir quais grandezas são diretas e quais são inversamente proporcionais:
as grandezas diretamente proporcionais aumentam em conjunto, exemplo:
200 ----- 100%
100 ----- 50%''')
    sleep(2)
    print('''já as grandezas inversamente proporcionais aumentam quando a outra diminui exemplo:
em um mesmo trecho de 100km 2 carros passam em diferentes velocidades e tempo:
100km/h ----- 1h
50km/h ----- 2h''')
    sleep(2)
    print('''definido isso vamos agora mostrar como funciona uma regra de 3 composta
    valor1     valor2 valor3
      a          a      a  == a1/desconhecido = a2*a3/b2*b3
(desconhecido)   b      b
as letras são as variaveis e o desconhecido é o numero a ser descoberto, para calcular esse valor devemos entrar no contexto e definir 
o que é direto e o que é inverso \33[1mem relação ao ponto da variavel desconhecida \33[mcomo explicado anteriormente.''')
    sleep(4)
    qtd = int(input('primeiramente insira quantas valores vão ter a sua regra de 3? '))
    print('vamos colocar o valor a ser estudado, isso é o valor que tem a variavel desconhecida')
    nome = input('qual o nome do valor a ser estudado? ')
    n = float(input('insira o valor da variavel a'))
    valor1 = Valor(nome, n)
    print('agora vamos inserir os outros valores e definir')
    varl = []
    for c in range(qtd-1):
        nome = input(f'insira o nome do valor{c+2}')
        relacao = input(f'o valor{c+2} é direta[d] ou inversamente[i] proporcional')
        vala = float(input(f'insira o a do valor {c+2}'))
        valb = float(input(f'insira o b do valor{c+2}'))
        val = Valor(nome, vala, valb)
        if relacao == 'i':
            val.inverso()
        varl.append(val)
    print('''uma vez digitado os valores vamos executar o calculo, lembrando que vai ser do mesmo jeito mostrado anteriormente
porém temos que por em mente que os valores inversamente proporcionais ao valor de estudo tem o a e b invertido''')
    multdiv = 1
    multdive = 1
    print(f'''o calculo vai ficar:
{valor1.nome}\t''',end='')
    for c in range(qtd-1):
        print(f'{varl[c].nome}\t',end='')
    print()
    print(f'{valor1.valora}\t', end='')
    multdiv *= valor1.valora
    for c in range(qtd-1):
        print(f'{varl[c].valora}\t',end='')
        multdive *= varl[c].valora
    print()
    print(f'desconhecido\t', end='')
    for c in range(qtd-1):
        print(f'{varl[c].valorb}\t',end='')
        multdiv*=varl[c].valorb
    print()
    print(f'''com isso, a gente vai passar o a do valor de estudo para como numero que fica embaixo e fazemos o seguinte calculo
desconhecido = ''',end='')
    for c in range(qtd-1):
        if c == qtd-1:
            print(f'{varl[c].valora}', end='')
        print(f'{varl[c].valora}*', end='')
    print('/', end='')
    for c in range(qtd-1):
        if c == qtd-1:
            print(f'{varl[c].valorb}', end='')
        print(f'{varl[c].valorb}*', end='')
    print(f'resultando em deconhecido = {multdiv}/{multdive} = {multdiv/multdive}')
if escolha == 'SIMPLES':
    escolha = input('escolha [simples] ou [composta]')
    print('''primeiro vamos definir se a regra é direta ou inversamente proporciona, isso é
    se as grandezas relaciondas aumentam em conjunto, elas são diretamente proporcionais.
    exemplo:
    200----100%
    150----75%
    quando a porcentagem aumenta o numero tambem aumenta.
    agora se quando uma aumentar a outra diminuir elas são inversamente proporcionais
    a exemplo de velocidade e tempo, exemplo: a um mesmo trecho de 100km 2 carros passam em velocidades diferentes com horas diferentes
    100km/h ----- 1h
    50km/h ----- x
    quando a velocidade aumenta a hora diminui, agora insira se a regra de 3 é simples ou composta''')
    escolha = input('escolha [d] para direta e [i] para inversa').upper()
    if escolha == 'D':
        print('''para a regra de 3 diretamente proporcional nos fazemos o calculo da seguinte maneira:
        a     b
          \33[0;33m\ \33[m\33[0;32m/\33[m
          \33[0;32m/ \33[m\33[0;33m\ \33[m 
        c     d(valor a encontrar)''')
        sleep(5)
        print('agora vamos inserir seus valores com base na ultima representação apresentada')
        a = float(input('digite o numero que vai em a'))
        b = float(input('digite o numero que vai em b'))
        c = float(input('digite o numero que vai em c'))
        print(f'agora vamos calcular o valor desconhecido, o calculo será: {a}X = ({b})({c})')
        print(f'o valor desconhecido é {(b + c) / a}')
    elif escolha == 'I':
        print('''para regra de 3 inversamente proporcionais nos fazemos o calculo da seguinte maneira:
        a\33[0;33m-----\33[mb
        c\33[0;33m-----\33[md(valor a ser descoberto)''')
        a = float(input('digite o numero que vai em a'))
        b = float(input('digite o numero que vai em b'))
        c = float(input('digite o numero que vai em c'))
        sleep(3)
        print(f'então o calculo fica a*b = c*d ou seja {a}*{b} = {c}*d')
        print(f'o valor desconhecido é {(a*b)/c}')