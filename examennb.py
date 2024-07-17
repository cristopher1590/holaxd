import csv
# Crear, leer, actualizar y eliminar
def abrrir_csv():
    with open('people_list.csv', mode= 'r', newline='',encoding='utf-8') as archivos:
        datos = csv.DictReader(archivos)
        return(list(datos))
    
def leer_csv():
    datos = abrrir_csv()

    for linea in datos:
        print(linea)

  
def crear_persona_csv():
    datos = abrrir_csv()


    nueva_persona = { 'DNI':input('ingrese un dni neuvo: '),
                    'Nombre':input('ingrese un nombre nevo: '),
                    'Edad':input('ingrese una edad nueva: ')}
                    
    datos.append(nueva_persona)

    with open('people_list.csv', mode= 'w', newline='',encoding='utf-8') as archivos:
        datos_persona = csv.DictWriter(archivos , fieldnames=['DNI', 'Nombre', 'Edad'])
        datos_persona.writeheader
        datos_persona.writerows(datos)
        print('persona creada correctamente.')

def actualizar_personas():
    datos = abrrir_csv
    buscar_dni = input('ingrese un dni a actualizar')

    for linea in datos:
        if linea['DNI'] == buscar_dni:
            print(linea)
            editador_persona = {'Nombre':input('ingrese un nombre: '),
                    'Edad':input('ingrese una edad: ')
                    }
            linea.update(editador_persona)
    
    with open('people_list.csv', mode= 'w', newline='',encoding='utf-8') as archivos:
        datos_persona = csv.DictWriter(archivos , fieldnames=['DNI', 'Nombre', 'Edad'])
        datos_persona.writeheader
        datos_persona.writerows(datos)
        print('persona actualizada correctamente.')
    



def eliminar_persona_csv():
    datos = abrrir_csv()
    dni = input("Ingrese el dni de la persona a eliminar: ")
    datos_filtrados = [persona for persona in datos if persona['DNI'] != dni]

    if len(datos) == len(datos_filtrados):
        print("Persona con DNI {} no encontrada".format(dni))
    else:
        with open('people_list.csv', mode='w', encoding='utf-8', newline='') as archivos_csv:
            datos_escribir = csv.DictWriter(archivos_csv, fieldnames=['DNI', 'Nombre', 'Edad'])
            datos_escribir.writeheader()
            datos_escribir.writerows(datos_filtrados)
            print("Persona eliminada correctamente.")








  
  #prueba de funciones 

#leer_csv()
#crear_persona_csv()
#Aactualizar_personas()
#eliminar_persona_csv()




