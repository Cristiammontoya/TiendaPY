from datetime import date


def alertas(productos):
    pendientes = [p for p in productos.values() if p["stock"] <= p["stock_minimo"]]
    if not pendientes:
        print("todo bien con el inventario")
        return
    proveedores = sorted(set(p["proveedor"] for p in pendientes))
    for proveedor in proveedores:
        print("
proveedor:", proveedor)
        for p in pendientes:
            if p["proveedor"] == proveedor:
                estado = "AGOTADO" if p["stock"] == 0 else "stock bajo"
                print(f'{p["nombre"]} ({p["codigo"]}): {p["stock"]} unidades - {estado}')


def cierre(productos, ventas):
    hoy = date.today().isoformat()
    del_dia = [v for v in ventas if v["fecha"] == hoy]
    total = sum(v["total"] for v in del_dia)
    conteo = {}
    for venta in del_dia:
        for codigo, cantidad in venta["productos"].items():
            conteo[codigo] = conteo.get(codigo, 0) + cantidad
    print("
cierre del dia:", hoy)
    print(f"total vendido: ${total:,.0f}")
    print("ventas hechas:", len(del_dia))
    print(f"promedio por venta: ${total / len(del_dia) if del_dia else 0:,.0f}")
    if conteo:
        mayor = max(conteo, key=conteo.get)
        nombre = productos[mayor]["nombre"] if mayor in productos else mayor
        print(f"mas vendido: {nombre} ({conteo[mayor]} unidades)")
    else:
        print("mas vendido: ninguno")
    sin_ventas = [p["nombre"] for codigo, p in productos.items() if codigo not in conteo]
    print("sin ventas:", ", ".join(sin_ventas) if sin_ventas else "ninguno")
    categorias = sorted({productos[c]["categoria"] for c in conteo if c in productos})
    print("categorias con ventas:", ", ".join(categorias) if categorias else "ninguna")
