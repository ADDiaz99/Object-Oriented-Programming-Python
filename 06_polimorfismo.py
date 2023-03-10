class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print('Estoy Caminando')


class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

    def avanzar(self):
        print('Estoy moviendome en mi bicicleta')

def run():
    persona = Persona('David')
    persona.avanzar()
    
    ciclista = Ciclista('Pedro')
    ciclista.avanzar()


if __name__ == '__main__':
    run()

    