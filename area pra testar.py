import bonitesas as bn
from time import sleep
print('escolha se a regra de 3 é simples ou composta')
escolha = input('escolha [simples] ou [composta]')
bn.titulo('regra de 3')
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
      \33[0;32m/\33[m\33[0;33m\ \33[m 
    c     d(valor a encontrar)''')
    sleep(5)
    print('agora vamos inserir seus valores com base na ultima representação apresentada')
    a = float(input('digite o numero que vai em a'))
    b = float(input('digite o numero que vai em b'))
    c = float(input('digite o numero que vai em c'))
    print(f'agora vamos calcular o valor desconhecido, o calculo será: {a}X = ({b})({c})')
    x = (b + c) / a
    print(f'o valor desconhecido é {x}')
elif escolha == 'I':
    print('''para regra de 3 inversamente proporcionais nos fazemos o calculo da seguinte maneira:
    a\33[0;33m-----\33[mb
    c\33[0;33m-----\33[md(valor a ser descoberto)''')
