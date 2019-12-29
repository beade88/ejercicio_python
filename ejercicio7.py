datos = dict()
datos={'nombre' : "Lester", 'apellido' : "Beade", 'mail' : "beade88@gmail.com", 'telefono' : "58290007"}
print "Su nomnbre es: ", datos['nombre']
print "Su apellido es: ", datos['apellido']
print "Su correo electronico es: ", datos['mail']
print "Su telefono es: ", datos['telefono']
print "El ejercicio 7 y el 8 se me parecen y por eso los puse en el 7, dime si me falto algo :)"

'''
Uso aqui otra forma de hacer comantarios, cuando son muy largos se hacen asi :D
Varias notas aqui:
1. datos = dict() Eso no tienes que hacerlo nunca en Python. 
Simplemente asignale a las variables los valores y el intuye el tipo,
o sea que comienzas por la linea 2.

2. En la linea dos hay errores de PEP8.
 - Los : van justo a continuacion de la palabra que los antecede y dejas 
   el espacio despues de los :. Seria 'nombre': 'Lester'  
 - PEP8 dicta que una linea no debe tener mas de 79 caracteres, pq es muy
    trabajoso leerla, y hay forma de hacer las lineas las cortas.
    Por ejemplo la linea 2 la puedes escribir de esta forma:
    datos = {
        'nombre': 'Lester',
        'apellido': 'Beade',
        'mail': 'beade88@gmail.com',
        'telefono': '58290007',
    }
    
    ** OJO aqui para no cometer errores de PEP8
    - fijate que la llave que cierra todo esta al mismo nivel que la palabra datos
    - 'nombre', 'apellido'', 'mail' y 'telefono' estan un nivel de identacion
       mas dentro que datos (ya debes saber q auqi la identacion en Python es 
       super importante)
    - fijate los espacios entre los : y la palabra q los sucede

3. Lo mismo de los print anteriores.
print('Su telefono es: ', datos['telefono'])

O pudieras hacerlo con el format
print('Su telefono es: {}'.format(datos['telefono']))
'''

# A lo que me refiero en el ejercicio 8 es que valides
# si lo que esta en el campo telefono es el fijo tuyo o el movil
# para que cambie el letrero y diga: 'El telefono es X' o 'el movil es X'
# Te iba a poner la solucion pero te dejare q lo pienses y lo hagas :D
