from persistencia import cargar_productos, cargar_ventas, guardar_productos
from inventario import mostrar, registrar, buscar, modificar, eliminar
from ventas import registrar_venta
from reportes import alertas, cierre


def iniciar():
    productos = cargar_productos()
    ventas = cargar_ventas()
    while True:
        print("
=== TIENDAPY ===")
        print("1. ver inventario")
        print("2. agregar producto")
        print("3. buscar producto")
        print("4. modificar producto")
        print("5. eliminar producto")
        print("6. hacer venta")
        print("7. alertas de stock")
        print("8. cierre del dia")
        print("9. guardar inventario")
        print("0. salir")
        opcion = input("elige una opcion: ").strip()
        try:
            if opcion == "1":
                mostrar(productos)
            elif opcion == "2":
                registrar(productos)
                guardar_productos(productos)
            elif opcion == "3":
                buscar(productos)
            elif opcion == "4":
                modificar(productos)
                guardar_productos(productos)
            elif opcion == "5":
                eliminar(productos)
                guardar_productos(productos)
            elif opcion == "6":
                registrar_venta(productos, ventas)
            elif opcion == "7":
                alertas(productos)
            elif opcion == "8":
                cierre(productos, ventas)
            elif opcion == "9":
                guardar_productos(productos)
                print("inventario guardado")
            elif opcion == "0":
                guardar_productos(productos)
                print("hasta luego")
                break
            else:
                print("opcion incorrecta")
        except ValueError as error:
            print("error:", error)
        except (EOFError, KeyboardInterrupt):
            guardar_productos(productos)
            print("
saliendo")
            break


if __name__ == "__main__":
    iniciar()
