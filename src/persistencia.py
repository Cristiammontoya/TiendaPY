from pathlib import Path

CARPETA = Path(__file__).resolve().parent.parent / "data"
INVENTARIO = CARPETA / "inventario.txt"
VENTAS = CARPETA / "ventas.txt"


def cargar_productos():
    productos = {}
    CARPETA.mkdir(exist_ok=True)
    if not INVENTARIO.exists():
        print("no habia inventario, se empieza vacio")
        INVENTARIO.touch()
    with INVENTARIO.open("r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, 1):
            if not linea.strip():
                continue
            try:
                codigo, nombre, categoria, precio, stock, minimo, proveedor = linea.strip().split("|")
                precio = float(precio)
                stock = int(stock)
                minimo = int(minimo)
                if not codigo or not nombre or not categoria or not proveedor or precio <= 0 or stock < 0 or minimo < 0 or codigo in productos:
                    raise ValueError
                productos[codigo] = {"codigo": codigo, "nombre": nombre, "categoria": categoria,
                                     "precio": precio, "stock": stock, "stock_minimo": minimo,
                                     "proveedor": proveedor}
            except ValueError:
                print(f"aviso: linea {numero} del inventario no se pudo leer")
    return productos


def guardar_productos(productos):
    CARPETA.mkdir(exist_ok=True)
    with INVENTARIO.open("w", encoding="utf-8") as archivo:
        for p in productos.values():
            archivo.write(f'{p["codigo"]}|{p["nombre"]}|{p["categoria"]}|{p["precio"]}|{p["stock"]}|{p["stock_minimo"]}|{p["proveedor"]}\n')


def cargar_ventas():
    ventas = []
    CARPETA.mkdir(exist_ok=True)
    if not VENTAS.exists():
        VENTAS.touch()
    with VENTAS.open("r", encoding="utf-8") as archivo:
        for numero, linea in enumerate(archivo, 1):
            if not linea.strip():
                continue
            try:
                fecha, total, detalle = linea.strip().split("|")
                productos = {}
                for parte in detalle.split(";"):
                    codigo, cantidad = parte.split(":")
                    cantidad = int(cantidad)
                    if not codigo or cantidad <= 0 or codigo in productos:
                        raise ValueError
                    productos[codigo] = cantidad
                total = float(total)
                if total <= 0 or not productos or len(fecha) != 10:
                    raise ValueError
                ventas.append({"fecha": fecha, "total": total, "productos": productos})
            except ValueError:
                print(f"aviso: linea {numero} de ventas no se pudo leer")
    return ventas


def guardar_venta(venta):
    CARPETA.mkdir(exist_ok=True)
    detalle = ";".join(f"{codigo}:{cantidad}" for codigo, cantidad in venta["productos"].items())
    with VENTAS.open("a", encoding="utf-8") as archivo:
        archivo.write(f'{venta["fecha"]}|{venta["total"]}|{detalle}\n')
