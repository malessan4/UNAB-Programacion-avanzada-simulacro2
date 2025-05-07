# Define en python dos clases:
# Vehiculo: con atributo marca(string) y metodo info() que devuelve "Vehiculo <marca>".
# Coche hereda de Vehiculo, añade atributo pasajeros (int) y redefino info() para devolver "Coche: <marca>, pasajeros <pasajeros>"

class Vehiculo:
    def __init__(self,marca):
        self.marca = marca
        
    def info(self):
        return f'Vehiculo {self.marca}'
    
class Coche(Vehiculo):
    def __init__(self, marca, pasajeros):
        self.pasajeros = pasajeros
        super().__init__(marca)
        
    def info(self):
        return f'Coche: {self.marca}, pasajeros: {self.pasajeros}'
    
if __name__ == '__main__':
    coche1 = Coche('Fiat', 4)
    print(coche1.info())
    vehiculo1 = Vehiculo('Toyota')
    print(vehiculo1.info())