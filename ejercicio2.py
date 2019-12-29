a = int (input ('Ingrese el numero 1: '))
b = int (input ('Ingrese el numero 2: '))

print ('La suma de los numeros es: ' +str(a+b))

#  Perfecto!!!! Solo unos comentarios.
#  Dices que lo hiciste distinto, pq no usaste raw_input
#  Aqui estaba desactualizado yo, pq con python3 la forma de hacerlo
#  es usando input, asi q vas bien :D

#  Hay algo que tienes que dominar y usar a la hora de escribir
#  codigo python (no importa si es scripts, frameworks, lo que sea)
#  esto se aplica para Python en general y se llama PEP8
#  https://pep8.org/
#  Estos son reglas para escribir codigo python de forma correcta
#  que sea entendible para todos. Son reglas de como nombrar variables,
#  como escribir operadores, la cantidad de espacios en blanco entre lineas,
#  etc. Parece boberia pero debes seguirlas, pq eso demuestra que dominas
#  el lenguaje y que tienes buen nivel.
#  Por ejemplo, PEP8 dicta que:
#  a=2+3 NO ES CORRECTO
#  a = 2 + 3 SI ES CORRECTO
#  Te das cuenta? Por ejemplo debes dejar un espacio entre el =, los numeros
#  y el operador.
#  Otro ejemplo:
#  a={'nombre':'Lester' ,'apellido':'Beade' } MAL
#  a = {'nombre': 'Lester', 'apellido': 'Beade'} BIEN
#  Aqui estarian mal que Lester esta pegado a los :, el espacio despues de Lester y antes de la ,...ademas
#  que esta unido Beade a los :..y que sobra un espacio antes del }
#  Eso ya lo vas agregando al dia a dia y por intuicion lo haces.

#  Con esto te senalo tus errores de PEP8, y voy a pegar aqui de nuevo tu codigo
#  para que veas la diferencia
a = int (input ('Ingrese el numero 1: '))
b = int (input ('Ingrese el numero 2: '))

print ('La suma de los numeros es: ' +str(a+b))

#  MANERA CORRECTA RESPETANDO PEP8
a = int(input('Ingrese el numero 1: '))
b = int(input('Ingrese el numero 2: '))
#  con esta linea en blanco q dejaste aqui no hay lio, pero pudiste
#  evitarla :D
print('La suma de los numeros es: ' + str(a + b))


#  No obstante el entorno de trabajo que uses se le pueden instalar
#  plugin que automaticamente te va diciendo donde estas cometiendo errores
#  de PEP8, peor eso lo haremos despues.
#  Por cierto, como estas haciendo estos ejercicios? Usando que?
#  un editor de texto normal?


