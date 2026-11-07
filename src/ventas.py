from datetime import date
from validaciones import pedir_texto, pedir_numero
from persistencia import guardar_venta, guardar_productos


def descuento_para(subtotal):
    if subtotal >= 100000:
        return 0.10
    if subtotal >= 50000:
        return 0.05
    return 0


def registrar_venta(productos, ventas):
    carrito = {}
    while True:
        codigo = input("codigo del producto (enter para terminar): ").strip().upper()
        if not codigo:
            break
        if codigo not in productos:
            print("ese producto no existe")
            continue
        cantidad = pedir_numero("cantidad: ", entero=True)
        acumulado = carrito.get(codigo, 0) + cantidad
        if acumulado > productos[codigo]["stock"]:
            print("no hay suficientes unidades")
            continue
        carrito[codigo] = acumulado
        print("agregado")

    if not carrito:
        print("venta vacia")
        return
    subtotal = 0
    print("
resumen de venta")
    for codigo, cantidad in carrito.items():
        p = productos[codigo]
        valor = p["precio"] * cantidad
        subtotal += valor
        print(f'{p["nombre"]}: {cantidad} x ${p["precio"]:,.0f} = ${valor:,.0f}')
    descuento = subtotal * descuento_para(subtotal)
    total = subtotal - descuento
    print(f"subtotal: ${subtotal:,.0f}")
    print(f"descuento: ${descuento:,.0f}")
    print(f"total: ${total:,.0f}")
    if input("confirmar venta? (s/n): ").strip().lower() != "s":
        print("venta cancelada")
        return
    for codigo, cantidad in carrito.items():
        if cantidad > productos[codigo]["stock"]:
            raise ValueError("no hay stock suficiente, no se hizo la venta")
    while True:
        pago = pedir_numero("con cuanto paga: ")
        if pago >= total:
            break
        print("el pago no alcanza")
    venta = {"fecha": date.today().isoformat(), "total": total, "productos": carrito}
    guardar_venta(venta)
    for codigo, cantidad in carrito.items():
        productos[codigo]["stock"] -= cantidad
    guardar_productos(productos)
    ventas.append(venta)
    print(f"cambio: ${pago - total:,.0f}")
    print("venta registrada")
