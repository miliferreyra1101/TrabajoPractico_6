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