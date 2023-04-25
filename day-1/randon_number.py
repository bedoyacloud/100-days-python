import random

correo = ["carlos1@gmail.com", 'julian@gamil.com']

diccionario = {}

lista_numerica = list(range(1, len(correo) + 1))


for i in correo:
    tamano_lista = len(lista_numerica)
    posicion_aleatoria = random.randrange(tamano_lista)
    numero_por_asignar = lista_numerica[posicion_aleatoria]
    diccionario[i] = numero_por_asignar
    lista_numerica.remove(numero_por_asignar)

print(diccionario)