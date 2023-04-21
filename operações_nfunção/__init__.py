def média():
    import bonitesas as bn
    from time import sleep
    bn.titulo('média aritmetica')
    media = []
    while True:
        n = input('insira o numero, ou n para parar: ')
        if n == 'n' or n == 'N':
            break
        else:
            n = float(n)
            media.append(n)
            print(media)
    print(f'a lista com todos os numeros digitados ficou {media}')
    sleep(2)
    print(f'a soma de todos os termos digitados é {sum(media)}, e vai ser dividido por {len(media)}')
    resulmedia = sum(media) / len(media)
    sleep(2)
    print(f'o resultado final ficou {resulmedia}')
    sleep(3)
    media = sorted(media)
    print('agora vamos ver qual a mediana desses numeros digitados')
    sleep(1)
    print(f'vamos colocar a lista em ordem crescente: {media}')
    print('agora vamos analisar quantos valores tem a lista')
    sleep(3)
    if len(media) % 2 == 0:
        print(
            f'a lista tem {len(media)} valores e é par, logo devemos tirar a media dos 2 termos centrais para ter a mediana')
        comp1 = (len(media) / 2) - 1
        comp1 = int(comp1)
        comp2 = len(media) / 2
        comp2 = int(comp2)
        print(
            f'os 2 valores do meio da lista são {media[comp1]} e {media[comp2]} e a média delas fica {(media[comp1] + media[comp2]) / 2}')
        mediana = (media[comp1] + media[comp2]) / 2
    else:
        print(
            f'a lista tem {len(media)} valores e é impar, logo podemos apenas pegar o valor do meio para definir a mediana')
        comp = (len(media) / 2) - 0.5
        comp = int(comp)
        mediana = media[comp]
    sleep(1)
    print(f'no fim a mediana fica {mediana}')
    sleep(2)
    print(f'agora vamos ver qual a moda da lista de numeros, que seria o numero que se repete mais')
    repeticoes = {}
    cont = 1
    for c in range(len(media) - 1):
        moda = media[c]
        if moda == media[c + 1]:
            cont += 1
        else:
            print(f'o numero {moda} se repete {cont} vez(es)')
            repeticoes[f'{cont}'] = moda
            cont = 1
        sleep(1)
    moda = max(repeticoes)
    print('no fim juntando todos os resultados temos: ')
    print(f'média: {resulmedia}, mediana: {mediana}, moda: {repeticoes[f"{moda}"]}')

def operações():
    n = input('qual operação voce deseja realizar?\n+ (soma)\n- (subtração)\nX (multiplicação)\n% (divisão)\n')
    if n == '+':
        n = float(input('digite o primeiro numero: '))
        n0 = float(input('digite o numero a ser somado: '))
        resultado = n + n0
        print('resultado = {}'.format(resultado))
        while True:
            n1 = (input('digite o numero a ser somado ou sair: '))
            if n1 == 'sair':
                break
            else:
                n1 = float(n1)
                resultado = resultado + n1
                print('resultado = {}'.format(resultado))
    if n == '-':
        n = float(input('digite o primeiro numero: '))
        n0 = float(input('digite o numero para subtraido: '))
        resultado = n - n0
        print('resultado = {}'.format(resultado))
        while True:
            n1 = (input('digite o numero para subtrair ou sair: '))
            if n1 == 'sair':
                break
            else:
                n1 = float(n1)
                resultado = resultado - n1
                print('resultado = {}'.format(resultado))
    if n == 'x':
        n = float(input('digite o primeiro numero: '))
        n0 = float(input('digite o numero a ser multiplicado: '))
        resultado = n * n0
        print('resultado = {}'.format(resultado))
        while True:
            n1 = (input('digite o numero a ser multiplicado ou sair: '))
            if n1 == 'sair':
                break
            else:
                n1 = float(n1)
                resultado = resultado * n1
                print('resultado = {}'.format(resultado))
    if n == '%':
        n = float(input('digite o primeiro numero: '))
        n0 = float(input('digite o numero a dividir: '))
        resultado = n / n0
        print('resultado = {}'.format(resultado))
        while True:
            n1 = (input('digite o numero a dividir ou sair: '))
            if n1 == 'sair':
                break
            else:
                n1 = float(n1)
                resultado = resultado / n1
                print('resultado = {}'.format(resultado))

def converbinaria():
    import bonitesas as bn
    from time import sleep
    bn.titulo('conversor binário')
    numero = input('''insira o numero a ser convertido em binário.
    atenção se for apenas um numero inteiro coloque .0 no final: ''')
    # separar a parte inteira da decimal
    numeros = numero.split('.')
    nint = numeros[0]
    ndec = numeros[1]
    print(f'parte inteira: {nint}')
    sleep(1)
    strgndec = f'0.{ndec}'
    ndec = float(strgndec)
    nint = float(nint)
    print(f'a parte decimal: {ndec}')
    sleep(2)
    print('descobrindo a quantidade de bits')
    cont = 0
    while True:
        sleep(1)
        cont += 1
        print(f'{cont} na base 2 fica {2 ** cont}')
        if 2 ** cont > nint:
            break
    print(f'o {2 ** cont} é maior do que {nint}, então vamos usar {2 ** (cont - 1)} e o numero vai ter {cont} bits')
    # cont = qtd de bits
    # convertendo
    sleep(2)
    resulnumero = nint
    nintconvertido = []
    print('agora vamos converter a parte inteira')
    for c in range(cont - 1, -1, -1):
        sleep(2)
        if (resulnumero - 2 ** c) >= 0:
            bit = '1'
            print(
                f'do numero {resulnumero} pode ser subtraido {2 ** c} e sobra {resulnumero - 2 ** c}, então o bit {c + 1} é 1')
            resulnumero += (-2 ** c)
        else:
            bit = '0'
            print(f'do numero {resulnumero} não pode ser subtraido {2 ** c}, então o bit {c + 1} é 0')
        nintconvertido.append(bit)
        resultemp = ''.join(nintconvertido)
        print(f'por enquanto a sequencia de bits está: {resultemp}', end='')
        print('0' * (cont - len(nintconvertido)))
    sleep(2)
    print('agora vamos ver a parte decimal')
    # converter a parte decimal
    numerodec = ndec
    ndecconvertido = []
    if numerodec != 0:
        while True:
            sleep(2)
            print(f'vamos multiplicar o {ndec} por 2, isso fica {ndec * 2}')
            ndec *= 2
            sleep(2)
            if ndec >= 1:
                print(f'como o numero {ndec} é maior que 1 vamos reduzir ele em 1 e colocar o bit como 1')
                ndec += -1
                bit = '1'
            else:
                bit = '0'
                print(f'como o numero {ndec}, não é maior que 1 vamos multiplicar denovo e colocar o bit como 0')
            ndecconvertido.append(bit)
            ndectemp = ''.join(ndecconvertido)
            sleep(1)
            print(f'sequencia de bits atuais: {ndectemp}')
            if ndec == 0:
                print('ja que o numero ficou 0 vamos parar por aqui')
                break
    else:
        print('como a parte decimal ficou 0 então não tem conversão')
        ndecconvertido = ['0']

    sleep(2)
    # formulando a resposta
    print('juntando as respostas fica: ', end='')
    resposta = ''
    for c, v in enumerate(nintconvertido):
        resposta += f'{v}'
    resposta += '.'
    for c, v in enumerate(ndecconvertido):
        resposta += f'{v}'
    print(resposta)

def matriz():
    import bonitesas as bn
    from time import sleep
    bn.titulo('matrizes')
    linhas = int(input('digite quantas linhas vai ter a sua matriz: '))
    colunas = int(input('digite quantas colunas vai ter a sua matriz: '))
    sleep(2)
    print('a sua matriz vai ficar assim: ')
    for l in range(linhas):
        for c in range(colunas):
            print(f'[{l};{c}]', end='')
        print()
    sleep(2)
    print('agora vamos inserir os numeros da sua matriz')
    matriz = []
    n = []
    for l in range(linhas):
        for c in range(colunas):
            n.append(float(input(f'digite o numero a ser inserido no lugar {l};{c}: ')))
        matriz.append(n[:])
        n = []
    sleep(3)
    print('sua matriz ficou: ')
    for l in range(linhas):
        for c in range(colunas):
            print(f'[{matriz[l][c]}]', end='')
        print()
    sleep(2)
    if linhas == colunas:
        if linhas <= 4:
            print('a sua matriz é uma matriz quadrada e logo é possivel calcular o determinante')
            if linhas == 1:
                print('a sua matriz é 1x1 e logo so tem um termo que é a determinante')
                print(f'a determinante da sua matriz é: {matriz[0][0]}')
            elif linhas == 2:
                print(
                    'a sua matriz é 2x2, nesse tipo de matriz a determinante se da pela subtração, dos produtos das diagonais da matriz')
                print(
                    f'a diagonal principal da sua matriz é {matriz[0][0]} e {matriz[1][1]}, e a diagonal secundária é {matriz[0][1]} e {matriz[1][0]}')
                sleep(2)
                multprin = matriz[0][0] * matriz[1][1]
                multsec = matriz[0][1] * matriz[1][0]
                print(f'a soma das matrizes ficou {multprin} e {multsec}, a determinante fica {multprin - multsec}. ')
                det = multprin - multsec
            elif linhas == 3:
                print('''sua matriz é 3x3, para tirar a sua determinante, clonamos as 2 colunas e colocamos a esquerda.
    então nos pegamos 3 diagonais da direta pra esquerda e multiplamos os valores das diagonais, e somamos as diagonais diferentes.
    depois fazemos isso com 3 diagonais da esquerda para direita, pegamos os valores finais de cada grupo de diagonais e subtraimos para conseguir
    o determinante''')
                sleep(5)
                print('segue o exemplo das diagonais principais: ')
                print(f'[ ][ ][\33[0;33mX\33[m]\33[1;30;40m{124:c}\33[m[\33[0;32mX\33[m][\33[0;31mX\33[m]')
                print(f'[ ][\33[0;33mX\33[m][\33[0;32mX\33[m]\33[1;30;40m{124:c}\33[m[\33[0;31mX\33[m][ ]')
                print(f'[\33[0;33mX\33[m][\33[0;32mX\33[m][\33[0;31mX\33[m]\33[1;30;40m{124:c}\33[m[ ][ ]')
                print('segue o exemplo das diagonais secundarias: ')
                sleep(3)
                print(f'[\33[0;31mX\33[m][\33[0;32mX\33[m][\33[0;33mX\33[m]\33[1;30;40m{124:c}\33[m[ ][ ]')
                print(f'[ ][\33[0;31mX\33[m][\33[0;32mX\33[m]\33[1;30;40m{124:c}\33[m[\33[0;33mX\33[m][ ]')
                print(f'[ ][ ][\33[0;31mX\33[m]\33[1;30;40m{124:c}\33[m[\33[0;32mX\33[m][\33[0;33mX\33[m]')
                print('os numeros após as barras pretas são as 2 primeiras colunas  clonadas')
                sleep(3)
                print(f'aplicando na sua matriz, os numeros diagonais principais ficam: ')
                diagprin = [[matriz[0][1], matriz[1][0], matriz[2][2]], [matriz[0][0], matriz[1][2], matriz[2][1]],
                            [matriz[0][2], matriz[1][1], matriz[2][0]]]
                diagsec = [[matriz[0][0], matriz[1][1], matriz[2][2]], [matriz[0][1], matriz[1][2], matriz[2][0]],
                           [matriz[0][2], matriz[1][0], matriz[2][1]]]
                print(diagprin)
                sleep(3)
                print('e os numeros das diagonais secundarias ficam: ')
                print(diagsec)
                sleep(3)
                print(
                    'agora vamos fazer a multiplicação das diagonais principais e somar elas para ver o resultado das diagonais principais1; ')
                resulprin = []
                resulsec = []
                multi = 1
                for c in range(3):
                    for v in range(3):
                        multi *= diagprin[c][v]
                    resulprin.append(multi)
                    multi = 1
                sleep(3)
                print(f'a multiplicação das diagonais principais: {resulprin}')
                sleep(2)
                for c in range(3):
                    for v in range(3):
                        multi *= diagsec[c][v]
                    resulsec.append(multi)
                    multi = 1
                print(f'a multiplicação das diagonais secundárias foi: {resulsec}')
                sleep(1)
                print(
                    f'no fim vai ficar {sum(resulprin)} - {sum(resulsec)} que vai dar a determinante = {sum(resulprin) - sum(resulsec)}')
        else:
            print('mesmo que a sua matriz seja quadrada, não é possível tirar uma determinante')

def regra_de_3: