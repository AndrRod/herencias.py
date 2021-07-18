
# Crea al menos un objeto de cada subclase y añadelos a una lista llamada vehiculos.

# Realiza una función llamada catalogar() que reciba la lista de vehículos y los recorra mostrando el nombre de su clase y sus atributos.

# Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.


import os
import time

time.sleep(2)
if os.name == "posix":
    var = "clear"       
elif os.name == "ce" or os.name == "nt" or os.name == "dos":
    var = "cls"
  

class vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return f'Vehiculoo: {type(self).__name__}\n Color: {self.color}\n Ruedas: {self.ruedas}'



class coche(vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return vehiculo.__str__(self) + f'\n Velocidad: {self.velocidad} km\n Cilidrada: {self.cilindrada} cc.'



# auto = coche('rojo', '4', '120', '400')
# print(auto, '\n')


class camioneta(coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f'\n Capacidad de carga {self.carga} kilogramos'


# camion = camioneta('azul', '4', '90', '200', '5000')
# print(camion, '\n')




class bicicleta(vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + f'\n Tipo: {self.tipo}'


# bici = bicicleta('verde', '2', 'deportiva')
# print(bici, '\n')

class Motocicleta(bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + f'\n Velocidad: {self.velocidad}\n Cilindrada: {self.cilindrada} cc.'

# moto = Motocicleta('azul', '2', 'urbana', '150', '150')
# print(moto)

class catalogar():
    def __init__(self):
        self.lista_vehiculos = []

    def agregar_vehiculo(self, vehi):
        self.lista_vehiculos.append(vehi)


    def __str__(self):
        lista_str = '\nLa lista de vehiculos es la siguiente: \n'
        ubicacion_lista = 0
        for vehi in self.lista_vehiculos:
            ubicacion_lista +=1
            lista_str += f'{ubicacion_lista}:\n {vehi}\n'
    
        return f'{lista_str} \n'

    def buqueda_por_ruedas(self, cantidad_ruedas):
        self.cantidad_ruedas = cantidad_ruedas
        vehiculos_ruedas = ''
        indice = 0
        for v in self.lista_vehiculos:
            if v.ruedas == self.cantidad_ruedas:
                indice +=1
                vehiculos_ruedas += f'{indice}:\n{v}\n'
        if indice > 0:
            return f'vehiculos que coinciden con su busqueda: \n{vehiculos_ruedas}\n\n Se ha encontrado {indice} vehiculos con {cantidad_ruedas} ruedas'
        else: return 'Ningun vehiculo coincide con su busqueda'
        
            
          


def red(cadena):
    red = "\033[31m" + cadena + "\033[0m"
    return red

def green(cadena):
    green = '\033[32m' + cadena + '\033[0m'
    return green

def es_digito(cadena):
    while not cadena.isdigit():
        cadena = input('Ingrese solo numeros: ')
    return cadena




lista_vehi = catalogar()    


opcion= ''
while opcion != 'no':
    opcion = input('\nDesea crear un vehiculo o ver la lista de vehiculos creados? \n\tsi \n\tno\n\n').lower()

    if opcion == 'si':
        opcion = input('Elija la opcion del vehiculo quiere crear o ver la lista de vehiculos creados \n\t1. Coche \n\t2. Camioneta \n\t3. Bicicleta \n\t4. Motocicleta \n\t5. Ver lista creada de vehiculos \n\t6. Busqueda por cantidad de ruedas\n')
        os.system(var) 

        if opcion in ['1', '2', '3', '4', '5', '6']:
            if opcion == '1':
                print('COCHE: ')
                color, ruedas, velocidad, cilindrada = input('color: '), input('ruedas: '), input('velocidad: '), input('cilindrada: ')
                vehiculo_creado = coche(color, ruedas, velocidad, cilindrada)

                print('\nUsted creo el siguiente vehiculo:\n' , vehiculo_creado)
                lista_vehi.agregar_vehiculo(vehiculo_creado)
            
            elif opcion == '2':
                print('CAMIONETA: ')
                color, ruedas, velocidad, cilindrada, carga= input('color: '), input('ruedas: '), input('velocidad: '), input('cilindrada: '), input('Carga: ')
                vehiculo_creado = camioneta(color, ruedas, velocidad, cilindrada, carga)
                print('\nUsted creo el siguiente vehiculo:\n' , vehiculo_creado)
                lista_vehi.agregar_vehiculo(vehiculo_creado)
            
            elif opcion == '3':
                print('BICICLETA: ')
                color, ruedas, tipo= input('color: '), input('ruedas: '), input('tipo (urbana/deportiva): ')
                vehiculo_creado = bicicleta(color, ruedas, tipo)
                print('\nUsted creo el siguiente vehiculo:\n' , vehiculo_creado)
                lista_vehi.agregar_vehiculo(vehiculo_creado)
            
            elif opcion == '4':
                print('MOTOCICLETA: ')
                color, ruedas, tipo, velocidad, cilindrada= input('color: '), input('ruedas: '), input('tipo (urbana/deportiva): '), input('velocidad: '), input('cilindrada: ')
                vehiculo_creado = Motocicleta(color, ruedas, tipo, velocidad, cilindrada)
                print('\nUsted creo el siguiente vehiculo:\n' , vehiculo_creado)
                lista_vehi.agregar_vehiculo(vehiculo_creado)

            elif opcion  == '5':
                print(lista_vehi)            
                time.sleep(4)
                
            else:
                cantidad_ruedas = es_digito(input('Ingrese número de ruedas: '))
                print(lista_vehi.buqueda_por_ruedas(cantidad_ruedas))
                time.sleep(4)
                

        else:
            print(red('\nOPCION INCORRECTA. Vuelva intentarlo '))
                
    elif not opcion == 'no':
        print(red('\nOPCION INCORRECTA. Vuelva intentarlo '))
        
    else: 
        print(green('\nMuchas gracias vuelva pronto'))

    time.sleep(3)
    os.system(var) 
    
