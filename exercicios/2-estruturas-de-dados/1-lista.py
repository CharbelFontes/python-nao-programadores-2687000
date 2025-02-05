# Crie uma lista apenas com elementos numéricos
numero = [1,2,3,4,5,6]
# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista = ['kyte',numero,True,60,'Chárbel',2345]
# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista[:5])
# Crie um slice na lista para que imprima na tela os elementos de índice par
lista = ['kyte',numero,True,60,'Chárbel',2345]
print(lista[0:-1:2])
# Insira na lista um novo item
lista = ['kyte',numero,True,60,'Chárbel',2345]
lista.append(57)
print(lista)
# Remova da lista o último item
lista.pop()
print(lista)
# Remova da lista um item específico
lista.remove(2345)
print(lista)