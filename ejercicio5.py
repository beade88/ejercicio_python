for x in range(1, 11):
    print ("El numero es "+str(x))

#  Mas de PEP8: print('El numero es ' + str(x)),
#  use '', y espacios antes y despues del +

#  Otra forma de hacerlo, que fue el tip que te di:
for x in range(1, 11):
    print ('El numero es {}'.format(x))

#  Esta manera de hacerla es muy comoda,
#  pq te permite concatenar cosas a los strings sin preocuparte
#  mucho (o eso creo) por el tipo, ademas el orden depende
#  de como los pongas dentro de format.
#  Por ejemplo:
a = 'Reinaldo'
b = 'Javier'
c = 'Menendez'
d = 'Alonso'
edad = 31
pichi = 'El pichi es {} {} {} {} y tiene {} anyos de edad'.format(a, b, c, d, edad)
print('format es una talla :D, mira como concatenas strings e ints')
print(pichi)

#  Hay otras formas de hacerlo, pero esta es la que mas uso
#  y es muy comoda.
