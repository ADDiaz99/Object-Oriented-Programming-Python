class Automovil:

    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)

        self._estado = 'en_movimiento'
    
    def retroceder(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(5)
        else:
            self._motor.inyecta_gasolina(1)

        self._estado = 'retrocediendo'


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

class Lights:

    def __init__(self, frontales, traseras):
        self.frontales = frontales
        self.traseras = traseras

    def encender(self, on, off):
        if Automovil.retroceder == 'despacio':
            Lights.frontales = on
            Lights.traseras = on
        else:
            Lights.frontales = on
            Lights.traseras = off
