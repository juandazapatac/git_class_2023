#Asistente de contabilidad de tu empresa

from functools import reduce
from data_importing import import_data

def run():
    respuesta=input('''Bienvenid@ a tu asistente de contabilidad,          
¿Qué deseas conocer hoy?
1. Utilidades
2. Ventas
3. Gastos
:''')
    data=import_data()
    ventas=[int(row[1]) for row in data]
    gastos=[int(row[2]) for row in data]
    if respuesta=='1':
        print('La utilidad total es',str(reduce(lambda x,y:x+y,ventas)-reduce(lambda x,y:x+y,gastos)),'COP')
    elif respuesta=='2':
        print('Las ventas totales son de',str(reduce(lambda x,y:x+y,ventas)),'COP')
    elif respuesta=='3':
        print('Los gastos totales son de',str(reduce(lambda x,y:x+y,gastos)),'COP')
    else:
        print('Error en el valor ingresado')
        
if __name__=='__main__':
    run()
    
