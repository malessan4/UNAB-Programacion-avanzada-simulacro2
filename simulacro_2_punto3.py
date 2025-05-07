"""
Explica en una 1 o 2 lineas que es un decorador en Python
Escribi un decorador anunciar que imprima 'Ejecutando
funcion' antes de llamar a la funcion decorada y luego
retorno el resultado
Aplica @anunciar a sumar(a,b)
"""


# Los decoradores son funciones o clases que modifica el
# comportamiento de otra funcion/metodo sin alterar su
# codigo original. Las funciones decoradoras son
# patrones de diseño de software.


def anunciar (func):
    def wrapper(*args, **kwargs):
        print('Ejecutando funcion...')
        func(*args, **kwargs)
    return wrapper

@anunciar
def sumar(a,b):
    resultado = a+b
    print(f'La suma de {a} y {b} es {resultado}')
    
sumar(2,5)