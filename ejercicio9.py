lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
datos = dict()
a={'1' : "primer", '2' : "segundo", '3' : "tercer", '4' : "cuarto"}
print "El", a['1'], "numero es", lista[0]
print "El", a['2'], "numero es", lista[1]
print "El", a['3'], "numero es", lista[2]
print "El", a['4'], "numero es", lista[3]
print "Seguro esto lo ves como vieja escuela pq tengo que imprimir tantas veces como quiera mostrar, seguro hay un metodo para ponerlo todo en una Linea, pero seguire investigando y dame las mieles"
print "Basicamente aqui lo que veo que te demuestro es que tengo la logica de invocar el elemento de la lista, o del diccionario que quiero y manejar el comando de print"
print "Sigo a ver si mejoro :) :D"


'''
Jajajajajaja....me gusta mucho esto....sobre todo pq puedo senalarte aqui
varias cosas....jajajaja...

Primero, me encanta tu LARGA linea 8, en el print donde te justificas...jajaja
pq me da pie para seguirte hablando de PEP8 jajaja.
Como te dije antes las lineas no pueden ser mas largas de 79 caracteres,
por lo tanto si me vas a dar tanta muela lo tienes que dividir :D
En serio, hay cosas de PEP8 q todavia no entiendo, pero las mas basicas
si hay que respetarlas para demostrar dominio y nivel :D

Rspecto a la solucion no es vieja escuela, estas muy cerca de la verdad, 
y me alegra :D. Lo malo aqui es que tendrias q poner tantas sentencias print
como numeros.
Mira, te pondre mi solucion, y luego tu me comentas. Fijate que respetare
PEP8 :D
'''
# La lista la creo no con los numero sino con los textos que seran distintos
lista = ['primer', 'segundo', 'tercer', 'cuarto', 'quinto', 'sexto', 'septimo', 'octavo', 'noveno', 'decimo']

# y como veo que me quedo una linea de mas de 79 caracters pues la manera correcta seria
lista = [
    'primer',
    'segundo',
    'tercer',
    'cuarto',
    'quinto',
    'sexto',
    'septimo',
    'octavo',
    'noveno',
    'decimo'
]

# o bien pudo ser
lista = [
    'primer', 'segundo', 'tercer',
    'cuarto', 'quinto', 'sexto',
    'septimo', 'octavo', 'noveno',
    'decimo'
]

# Ahora mira esto y dime si entiendes:
cont = 1
for n in lista:
    print('El {} numero es {}'.format(n, cont))
    cont += 1
