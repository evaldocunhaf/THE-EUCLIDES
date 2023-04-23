import bonitesas as bn
from time import sleep
print('escolha se a regra de 3 é simples ou composta')
escolha = input('escolha [simples] ou [composta]')
if escolha == 'composta':
if escolha == 'simples':
    bn.titulo('regra de 3')
    print('''''')
    print('''como funciona a regra de 3 de numeros inversamente proporcionais: são valores relacionados que assim podemos achar o quarto valor
    exemplo a está para b assim como c esta para d, 200 está para 100% assim como 150 está para 75%
    200----100%
    150----75%
    porém em aplicações da matemática nós vamos usar essa regra para descobrir um valor X
    a----b
    c---(numero a ser descoberto)''')
    sleep(5)
    print('agora vamos inserir seus valores com base na ultima representação apresentada')
    a = float(input('digite o numero que vai em a'))
    b = float(input('digite o numero que vai em b'))
    c = float(input('digite o numero que vai em c'))
    print(f'agora vamos calcular o valor desconhecido, o calculo será: {a}X = ({b})({c})')
    x = (b + c) / a
    print(f'o valor desconhecido é {x}')
