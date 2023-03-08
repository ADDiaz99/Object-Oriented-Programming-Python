class CasillaDeVotacion:
    
    def __init__(self, indentificador, pais):
        # Para indentificar una variable privada se usa (Doble) __ 
        self.__indentificador = indentificador
        self.__pais = pais
        self.__region = None
    
    @property
    def region(self):
        return self.__region
    
    @region.setter
    def set_region(self, region):
        try:
            if region in self.__pais : 
                self.__region = region
            
            else:
                raise ValueError(f'La region {region} no es valida en {self.__pais}')
        
        except: 
            print(f'Error al guardar la region')

# Punto de entrada
if __name__ == '__main__':
    
    casilla = CasillaDeVotacion(123, ['Ciudad de Mexico', 'Morelos'])

    print(casilla.region) # Imprime None
    
    # __region es un atributo privado de casilla y no se puede modificar directamente
    casilla.__region = 'ABCD' 
    print(casilla.region) # Imprime None
    
    casilla.set_region = 'Jalisco' # Error
    print(casilla.region) # Imprime None

    casilla.set_region = 'Morelos'
    print(casilla.region) # Imprime Morelos