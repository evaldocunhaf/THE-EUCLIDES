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
sleep(1)
print(f'a soma de todos os termos digitados é {sum(media)}, e vai ser dividido por {len(media)}')
resulmedia = sum(media)/len(media)
media = sorted(media)
if len(media) % 2 == 0:
    comp1 = (len(media)/2) - 1
    comp1 = int(comp1)
    comp2 = len(media)/2
    comp2 = int(comp2)
    mediana = (media[comp1] + media[comp2])/2
else:
    comp = (len(media)/2) - 0.5
    comp = int(comp)
    mediana = media[comp]

repeticoes = {}
cont =1
for c in range(len(media)-1):
    moda = media[c]
    print(media[c])
    if moda == media[c+1]:
        cont += 1
    else:
        repeticoes[f'{cont}'] = moda
        cont = 1
print(repeticoes)
moda = max(repeticoes)

print(f'média: {resulmedia}, mediana: {mediana}, moda: {repeticoes[f"{moda}"]}')