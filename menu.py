import csv
import examennb

#examennb.abrrir_csv()
#examennb.leer_csv()
#examennb.crear_persona_csv()
#examennb.actualizar_personas()
#examennb.eliminar_persona_csv()

while True:
    print('----menu-----')
    print('[1.] leer csv.')
    print('[2] Crear persona.')
    print('[3] actualizar persona.')
    print('[4] eliminar persona.')
    print('[0] salir 🚪🏃💨')
    opcion = int(input('ingrese una opcion: '))

    if opcion == 1:
        examennb.leer_csv()
    if opcion ==2:
        examennb.crear_persona_csv()
    if opcion == 3:
        examennb.actualizar_personas()
    if opcion == 4:
        examennb.eliminar_persona_csv()
    elif opcion == 0:
        print('saliendo......')
        break