def média(exp):
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
    resulmedia = sum(media) / len(media)
    if exp:
        print(f'a soma de todos os termos digitados é {sum(media)}, e vai ser dividido por {len(media)}')
        sleep(2)
        print(f'o resultado final ficou {resulmedia}')
        sleep(3)
    else:
        print(f'média: {resulmedia}')
    media = sorted(media)
    if exp:
        print('agora vamos ver qual a mediana desses numeros digitados')
        sleep(1)
        print(f'vamos colocar a lista em ordem crescente: {media}')
        print('agora vamos analisar quantos valores tem a lista')
        sleep(3)
    else:
        pass
    if len(media) % 2 == 0:
        if exp:
            print(f'a lista tem {len(media)} valores e é par, logo devemos tirar a media dos 2 termos centrais para ter a mediana')
        else:
            pass
        comp1 = (len(media) / 2) - 1
        comp1 = int(comp1)
        comp2 = len(media) / 2
        comp2 = int(comp2)
        mediana = (media[comp1] + media[comp2]) / 2
        if exp:
            print(f'os 2 valores do meio da lista são {media[comp1]} e {media[comp2]} e a média delas fica {mediana}')
        else:
            print(f'mediana = {mediana}')
    else:
        if exp:
            print(f'a lista tem {len(media)} valores e é impar, logo podemos apenas pegar o valor do meio para definir a mediana')
        else:
            pass
        comp = (len(media) / 2) - 0.5
        comp = int(comp)
        mediana = media[comp]
    sleep(1)
    print(f'no fim a mediana fica {mediana}')
    sleep(2)
    if exp:
        print(f'agora vamos ver qual a moda da lista de numeros, que seria o numero que se repete mais')
    else:
        pass
    repeticoes = {}
    cont = 1
    for c in range(len(media) - 1):
        moda = media[c]
        if moda == media[c + 1]:
            cont += 1
        else:
            if exp:
                print(f'o numero {moda} se repete {cont} vez(es)')
            else:
                pass
            repeticoes[f'{cont}'] = moda
            cont = 1
        sleep(1)
    moda = max(repeticoes)
    print('no fim juntando todos os resultados temos: ')
    print(f'média: {resulmedia}, mediana: {mediana}, moda: {repeticoes[f"{moda}"]}')

def operações(exp):
    n = input('qual operação voce deseja realizar?\n+ (soma)\n- (subtração)\nX (multiplicação)\n% (divisão)\n')
    if n == '+':
        n = float(input('digite o primeiro numero: '))
        n0 = float(input('digite o numero a ser somado: '))
        resultado = n + n0
        if exp:
            print(f'{n} + {n0} = {resultado}')
        else:
            pass
        print('resultado = {}'.format(resultado))
        while True:
            n1 = (input('digite o numero a ser somado ou sair: '))
            if n1 == 'sair':
                if exp:
                    print('até a próxima')
                else:
                    pass
                break
            else:
                n1 = float(n1)
                if exp:
                    print(f'{resultado} + {n1} = {resultado+n1}')
                resultado = resultado + n1
                print('resultado = {}'.format(resultado))
    if n == '-':
        n = float(input('digite o primeiro numero: '))
        n0 = float(input('digite o numero para subtraido: '))
        resultado = n - n0
        if exp:
            print(f'{n} - {n0} = {resultado}')
        print('resultado = {}'.format(resultado))
        while True:
            n1 = (input('digite o numero para subtrair ou sair: '))
            if n1 == 'sair':
                if exp:
                    print('até a próxima')
                else:
                    pass
                break
            else:
                n1 = float(n1)
                if exp:
                    print(f'{resultado} - {n1} = {resultado - n1}')
                resultado = resultado - n1
                print('resultado = {}'.format(resultado))
    if n == 'x':
        n = float(input('digite o primeiro numero: '))
        n0 = float(input('digite o numero a ser multiplicado: '))
        resultado = n * n0
        if exp:
            print(f'{n} X {n0} = {resultado}')
        print('resultado = {}'.format(resultado))
        while True:
            n1 = (input('digite o numero a ser multiplicado ou sair: '))
            if n1 == 'sair':
                if exp:
                    print('até logo')
                else:
                    pass
                break
            else:
                n1 = float(n1)
                if exp:
                    print(f'{resultado} X {n1} = {resultado*n1}')
                resultado = resultado * n1
                print('resultado = {}'.format(resultado))
    if n == '%':
        n = float(input('digite o primeiro numero: '))
        n0 = float(input('digite o numero a dividir: '))
        resultado = n / n0
        if exp:
            print(f'{n} / {n0} = {resultado}')
        print('resultado = {}'.format(resultado))
        while True:
            n1 = (input('digite o numero a dividir ou sair: '))
            if n1 == 'sair':
                if exp:
                    print('até a próxima')
                else:
                    pass
                break
            else:
                n1 = float(n1)
                if exp:
                    print(f'{resultado} / {n1} = {resultado/n1}')
                resultado = resultado / n1
                print('resultado = {}'.format(resultado))

def converbinaria(exp):
    import bonitesas as bn
    from time import sleep
    bn.titulo('conversor binário')
    numero = input('''insira o numero a ser convertido em binário.
    atenção se for apenas um numero inteiro coloque .0 no final: ''')
    # separar a parte inteira da decimal
    numeros = numero.split('.')
    nint = numeros[0]
    ndec = numeros[1]
    if exp:
        print(f'parte inteira: {nint}')
        sleep(1)
    else:
        pass
    strgndec = f'0.{ndec}'
    ndec = float(strgndec)
    nint = float(nint)
    if exp:
        print(f'a parte decimal: {ndec}')
        sleep(2)
        print('descobrindo a quantidade de bits')
    else:
        pass
    cont = 0
    while True:
        if exp:
            sleep(1)
        else:
            pass
        cont += 1
        if exp:
            print(f'{cont} na base 2 fica {2 ** cont}')
        else:
            pass
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

def regra3():
    import bonitesas as bn
    from time import sleep
    import teste_poo
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
        valor1 = teste_poo.Valor(nome, n)
        print('agora vamos inserir os outros valores e definir')
        varl = []
        for c in range(qtd - 1):
            nome = input(f'insira o nome do valor{c + 2}')
            relacao = input(f'o valor{c + 2} é direta[d] ou inversamente[i] proporcional')
            vala = float(input(f'insira o a do valor {c + 2}'))
            valb = float(input(f'insira o b do valor{c + 2}'))
            val = teste_poo.Valor(nome, vala, valb)
            if relacao == 'i':
                val.inverso()
            varl.append(val)
        print('''uma vez digitado os valores vamos executar o calculo, lembrando que vai ser do mesmo jeito mostrado anteriormente
    porém temos que por em mente que os valores inversamente proporcionais ao valor de estudo tem o a e b invertido''')
        multdiv = 1
        multdive = 1
        print(f'''o calculo vai ficar:
    {valor1.nome}\t''', end='')
        for c in range(qtd - 1):
            print(f'{varl[c].nome}\t', end='')
        print()
        print(f'{valor1.valora}\t', end='')
        multdiv *= valor1.valora
        for c in range(qtd - 1):
            print(f'{varl[c].valora}\t', end='')
            multdive *= varl[c].valora
        print()
        print(f'desconhecido\t', end='')
        for c in range(qtd - 1):
            print(f'{varl[c].valorb}\t', end='')
            multdiv *= varl[c].valorb
        print()
        print(f'''com isso, a gente vai passar o a do valor de estudo para como numero que fica embaixo e fazemos o seguinte calculo
    desconhecido = ''', end='')
        for c in range(qtd - 1):
            if c == qtd - 1:
                print(f'{varl[c].valora}', end='')
            print(f'{varl[c].valora}*', end='')
        print('/', end='')
        for c in range(qtd - 1):
            if c == qtd - 1:
                print(f'{varl[c].valorb}', end='')
            print(f'{varl[c].valorb}*', end='')
        print(f'resultando em deconhecido = {multdiv}/{multdive} = {multdiv / multdive}')
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
            print(f'o valor desconhecido é {(a * b) / c}')

