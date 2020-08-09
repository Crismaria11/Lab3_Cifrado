"""

Laboratorio 3
Ejercicio 1 

Fuentes consultadas:
Libreria de PyCryptodome
Links: 
https://docs.python.org/3/library/hmac.html
https://pycryptodome.readthedocs.io/en/latest/src/hash/hmac.html?highlight=hmac
https://stackoverrun.com/es/q/2156096

"""
from Crypto.Hash import HMAC, SHA256

#Parte a
key = b'CC3078'
mensaje = 'Cifrado de informacion seccion 10'

pruebaA = HMAC.new(key, msg=mensaje.encode(), digestmod=SHA256)
print("\nEl HMAC-SHA-256 de la Prueba A es:")
print(pruebaA.hexdigest() + '\n')


#Parte b
key = b'MAC'
mensaje = 'La implementacion de este ejercicio fue sencilla'

pruebaB = HMAC.new(key, msg=mensaje.encode(), digestmod=SHA256)
print("El HMAC-SHA-256 de la Prueba B es:")
print(pruebaB.hexdigest() + '\n')