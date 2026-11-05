def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto and "|" not in texto and ";" not in texto and ":" not in texto:
            return texto
        print("escribe un dato valido")


def pedir_numero(mensaje, entero=False, permitir_cero=False):
    while True:
        try:
            numero = int(input(mensaje)) if entero else float(input(mensaje))
            if numero < 0 or (numero == 0 and not permitir_cero):
                raise ValueError
            if not entero and (numero == float("inf") or numero != numero):
                raise ValueError
            return numero
        except ValueError:
            print("ingresa un numero valido")
