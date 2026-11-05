from validaciones import pedir_texto, pedir_numero

CATEGORIAS = ["Lacteos", "Bebidas", "Aseo", "Abarrotes", "Snacks"]


def mostrar(productos):
    if not productos:
        print("no hay productos")
        return
    print("codigo | nombre | categoria | precio | unidades | minimo | proveedor")
    for p in productos.values():
        print(f'{p["codigo"]} | {p["nombre"]} | {p["categoria"]} | ${p["precio"]:,.0f} | {p["stock"]} | {p["stock_minimo"]} | {p["proveedor"]}')


def registrar(productos):
    codigo = pedir_texto("codigo: ").upper()
    if codigo in productos:
        raise ValueError("ese codigo ya existe")
    nombre = pedir_texto("nombre: ")
    print("categorias: " + ", ".join(CATEGORIAS))
    while True:
        categoria = pedir_texto("categoria: ").capitalize()
        if categoria in CATEGORIAS:
            break
        print("elige una categoria de la lista")
    precio = pedir_numero("precio: ")
    stock = pedir_numero("unidades disponibles: ", entero=True, permitir_cero=True)
    minimo = pedir_numero("stock minimo: ", entero=True, permitir_cero=True)
    proveedor = pedir_texto("proveedor: ")
    productos[codigo] = {"codigo": codigo, "nombre": nombre, "categoria": categoria, "precio": precio,
                         "stock": stock, "stock_minimo": minimo, "proveedor": proveedor}
    print("producto guardado")


def buscar(productos):
    print("1. por codigo  2. por categoria")
    opcion = input("opcion: ").strip()
    if opcion == "1":
        codigo = pedir_texto("codigo: ").upper()
        mostrar({codigo: productos[codigo]} if codigo in productos else {})
    elif opcion == "2":
        categoria = pedir_texto("categoria: ")
        mostrar({c: p for c, p in productos.items() if p["categoria"].lower() == categoria.lower()})
    else:
        print("opcion incorrecta")


def modificar(productos):
    codigo = pedir_texto("codigo: ").upper()
    if codigo not in productos:
        raise ValueError("no existe ese producto")
    print("1. cambiar precio  2. cambiar stock")
    opcion = input("opcion: ").strip()
    if opcion == "1":
        productos[codigo]["precio"] = pedir_numero("nuevo precio: ")
    elif opcion == "2":
        productos[codigo]["stock"] = pedir_numero("nuevo stock: ", entero=True, permitir_cero=True)
    else:
        print("opcion incorrecta")
        return
    print("producto actualizado")


def eliminar(productos):
    codigo = pedir_texto("codigo: ").upper()
    if codigo not in productos:
        raise ValueError("no existe ese producto")
    if input("eliminar? (s/n): ").strip().lower() == "s":
        del productos[codigo]
        print("producto eliminado")
