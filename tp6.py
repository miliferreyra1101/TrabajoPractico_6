#PROGRAMA DE GESTIÓN DE DATOS PARA UN ESCUELA

datos = {
    "alumnos":[
    {
            "Nombre": "Juan",
            "Apellido": "Pérez",
            "DNI": 47775898,
            "Fecha de nacimiento": "10/05/2008",
            "Tutor": "María Pérez",
            "Notas": [8, 7, 9],
            "Faltas": 2,
            "Amonestaciones": 0
        },
        {
            "Nombre": "Sofía",
            "Apellido": "Fernandez",
            "DNI": 49854675,
            "Fecha de nacimiento": "22/08/2008",
            "Tutor": "Carlos Rodríguez",
            "Notas": [10, 9, 10],
            "Faltas": 0,
            "Amonestaciones": 0
        },
        {
            "Nombre": "Pedro",
            "Apellido": "Martinez",
            "DNI": 51855775,
            "Fecha de nacimiento": "22/08/2008",
            "Tutor": "Luciana Martinez",
            "Notas": [8, 6, 7],
            "Faltas": 2,
            "Amonestaciones": 1
        }
    ]
}

print("A continuación, se le mostrará el nombre completo de todos los alumnos que asisten a la escuela:")
num_alumno = 1
for alumno in datos["alumnos"]:
    print("Número de alumno: ", num_alumno)
    print(alumno["Nombre"], alumno["Apellido"])
    num_alumno = num_alumno + 1

respuesta = input("¿Desea mostrar los datos completos de algún alumno?. Si lo desea, ingrese su número. De lo contrario, ingrese SIGUIENTE: ")
if respuesta.upper() != "SIGUIENTE":
    indice = int(respuesta) - 1
    if 0 <= indice  and indice < len(datos["alumnos"]):
            alumno_elegido = datos["alumnos"][indice]
            print("Nombre: ", {alumno_elegido["Nombre"]})
            print("Apellido: ", {alumno_elegido["Apellido"]})
            print("DNI: ", {alumno_elegido["DNI"]})
            print("Fecha de Nac.: ", {alumno_elegido["Fecha de nacimiento"]})
            print("Tutor: ", {alumno_elegido["Tutor"]})
            print("Notas: ", {alumno_elegido["Notas"]})
            print("Faltas: ",{alumno_elegido["Faltas"]})
            print("Amonestaciones: ", {alumno_elegido["Amonestaciones"]})
    else:
        print("Ese número de alumno no existe.")
else:
    print("...")

alumno_mod = input("¿Desea modificar los datos de algún alumno?. Si lo desea, ingrese su número. De lo contrario, ingrese SIGUIENTE: ")
if alumno_mod.upper() != "SIGUIENTE":
    indice = int(alumno_mod) - 1
    if 0 <= indice and indice < len(datos["alumnos"]):
        alumno_elegido = datos["alumnos"][indice]
        print("Modificando a: ", {alumno_elegido['Nombre']})
        print("1. Notas | 2. Faltas | 3. Amonestaciones")
        modificar = input("¿Qué desea modificar? (Ingrese el número): ")
        if modificar == "1":
            nueva_nota = int(input("Ingrese la nota: "))
            alumno_elegido["Notas"].append(nueva_nota)
        elif modificar == "2":
            nuevas_faltas = int(input("Ingrese las nuevas faltas: ")) 
            total = alumno_elegido["Faltas"] + nuevas_faltas
            alumno_elegido["Faltas"] = total
        elif modificar == "3":
            nuevas_amonestaciones = int(input("Ingrese las nuevas amonestaciones: "))
            total = alumno_elegido["Amonestaciones"] + nuevas_amonestaciones
            alumno_elegido["Amonestaciones"] = total
        print("Datos actualizados.")
    else:
        print("Ese número de alumno no existe.")
else:
    print("...")

respuesta_nuevo = int(input("¿Desea añadir un nuevo alumno o expulsar un alumno?. Ponga 1 si desea añadir, 2 si desea añadir, 3 si desea continuar: "))
if respuesta_nuevo == 1:
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = int(input("DNI: "))
    fecha_nac = input("Fecha de nacimiento: ")
    tutor = input("Nombre del tutor: ")

    nuevo = {
    "Nombre": nombre,
    "Apellido": apellido,
    "DNI": dni,
    "Fecha de nacimiento": fecha_nac,
    "Tutor": tutor,
    "Notas": [],       
    "Faltas": 0,       
    "Amonestaciones": 0 
    }
    datos["alumnos"].append(nuevo)

    print(f"El alumno {nombre} {apellido} ha sido agregado con éxito.")
elif respuesta_nuevo == 2: 
    indice_eliminar = int(input("Ingrese el número del alumno a expulsar: ")) - 1
    if 0 <= indice_eliminar and indice_eliminar < len(datos["alumnos"]):
        expulsado = datos["alumnos"].pop(indice_eliminar)
        print(f"El alumno {expulsado['Nombre']} ha sido removido.")
    else:
        print("Número no válido.")
else:
    print("...")


print("Listado final de alumnos: ")
num_alumno = 1
for alumno in datos["alumnos"]:
    print("Número de alumno: ", num_alumno)
    print(alumno["Nombre"], alumno["Apellido"])
    num_alumno = num_alumno + 1