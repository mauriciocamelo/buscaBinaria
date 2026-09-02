def busca_binaria(lista, item):
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        palpite = lista[meio]

        if palpite == item:
            return meio
        if palpite < item:
            esquerda = meio + 1
        else:
            direita = meio - 1
        print(meio)

    return -1
lista = [0,1,2,3,4,5,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
x = int(input("Digite um número de 0 à 30: "))
resultado = busca_binaria(lista, x)
if resultado != -1:
    print(f'Item encontrado no índice: {resultado}')
else:
    print('Item não encontrado na lista.')
