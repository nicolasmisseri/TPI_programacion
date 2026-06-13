def normalizar_texto(texto):
    """Convierte el texto a minúsculas para comparaciones insensibles a mayúsculas"""
    return texto.lower().strip()


def limpiar_numero(numero_texto):
    """Limpia y convierte números removiendo puntos y comas (separadores de miles)"""
    numero_texto = numero_texto.strip()
    numero_texto = numero_texto.replace(".", "").replace(",", "")
    return int(numero_texto)


def mostrar_paises(paises):
    """Muestra una lista de países de forma formateada"""
    if not paises:
        print("No hay países para mostrar.")
        return

    print(f"\n{'Nombre':<25} {'Población':>15} {'Superficie':>15} {'Continente':<20}")
    print("-" * 75)
    for p in paises:
        print(f"{p['nombre']:<25} {p['poblacion']:>15,} {p['superficie']:>15,} {p['continente']:<20}")
