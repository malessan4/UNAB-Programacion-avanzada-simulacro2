#
# Verdadero o Falso
# a)El acoplamiento bajo favorece que una clase se pueda 
# reutilizar con menos dependencias
# 
# Verdadero, porque una clase con bajo acoplamiento
# no tiene depende poco de otros modulos o clases
# 
# b) La encapsulacion impide el acceso a los atributos
# de una clase desde fuera de sus metods
# 
# Verdadero
# En Python no impide totalmente el acceso a los atributos
# desde afuera de los metodos, pero si establece mecanismos
# para controlarlo. En otros lenguajes como Java y C# si
# impiden el acceso a los atributos
# 
# c) type(objeto) devuelve la clase a la que pertenece
# objeto
# 
# Verdadero
# En Python, la función type(objeto) devuelve la clase (tipo) a la que pertenece el objeto.
# 
# d) La abstraccion consiste en ocultar la complejidad interna y mostrar solo lo esencial
# 
# Verdadero
# La abstraccion consiste en representar las caracteristirac esenciales de un objeto sin preocuparse
# por mostrar como funciona internamente.
# 
class Persona():
    def __init__ (self,nombre):
        self.nombre = nombre
    
    def saludar(self):
        return f'Hola, {self.nombre} esta saludando'
    
    def __str__(self):
        return f'Persona: {self.nombre}'
    
persona1 = Persona('Matias')
print(persona1.saludar())
print(persona1)
    