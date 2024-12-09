from abc import ABC, abstractmethod

class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        raise NotImplementedError("Método deve ser implementado.")
    

class Circulo(FormaGeometrica):

    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        area = 3.14 * self.raio ** 2
        return area
    
class Retangulo(FormaGeometrica):

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura
        return area


circulo = Circulo(raio=10)
print(circulo.calcular_area())

retangulo1 = Retangulo(largura=10, altura=5)

print(retangulo1.calcular_area())