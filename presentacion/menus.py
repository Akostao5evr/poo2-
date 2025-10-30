import os
from aplicacion.departamento_app import crudDepartamento
from aplicacion.empleado_app import crudEmpleado
from aplicacion.proyecto_app import crudProyecto

def menuPrincipal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("********** MENÚ PRINCIPAL **********")
        print("1. Menú de Departamentos")
        print("2. Menú de Proyectos")
        print("3. Menú de Empleados")
        print("4. Salir")
        print("************************************")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menuCRUD("Departamento", crudDepartamento)
        elif opcion == "2":
            menuCRUD("Proyecto", crudProyecto)
        elif opcion == "3":
            menuCRUD("Empleado", crudEmpleado)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def menuCRUD(entidad, crudFuncion):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"***** MENÚ {entidad.upper()} *****")
        print("1. Agregar")
        print("2. Mostrar todos")
        print("3. Modificar")
        print("4. Eliminar")
        print("5. Volver al menú principal")
        print("*****************************")
        opcion = input("Seleccione una opción: ")

        if opcion == "5":
            break
        elif opcion in ["1", "2", "3", "4"]:
            crudFuncion(opcion)
        else:
            print("Opción inválida.")