from presentacion.menus import menuPrincipal

def main():
    while True:
        menuPrincipal()
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            print("Menú de departamentos")
            # Aquí se llama a aplicacion.departamento_app
        elif opcion == "2":
            print("Menú de proyectos")
            # Aquí se llama a aplicacion.proyecto_app
        elif opcion == "3":
            print("Menú de empleados")
            # Aquí se llama a aplicacion.empleado_app
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()