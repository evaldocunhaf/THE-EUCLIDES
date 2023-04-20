def média():
    import bonitesas as bn
    bn.titulo('média aritmetica')
    n0 = float(input('digite o primeiro numero: '))
    n1 = float(input('digite o segundo numero: '))
    total = n0 + n1
    divisor = 2
    while True:
        continuidade = input('digite o proximo numero ou resultado para calcular a média: ')
        if continuidade == 'resultado':
            break
        else:
            continuidade = float(continuidade)
            total = total + continuidade
            divisor = divisor + 1
    print('o resultado foi {}'.format(total / divisor))

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
    print(f'o {2 ** cont} é maior do que {nint}, então vamos usar {2 ** (cont - 1)}e o numero vai ter {cont} bits')
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
            if ndec >= 1:
                print(f'como o numero {ndec} é maior que 1 vamos reduzir ele em 1 e colocar o bit como 1')
                ndec += -1
                bit = '1'
            else:
                bit = '0'
                print(f'como o numero {ndec}, não é maior que 1 vamos multiplicar denovo e colocar o bit como 0')
            ndecconvertido.append(bit)
            ndectemp = ''.join(ndecconvertido)
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