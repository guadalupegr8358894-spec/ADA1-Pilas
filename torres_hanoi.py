class Pila:
    """Implementación de la estructura de datos Pila (Stack) con nombre de torre."""
    def __init__(self, nombre=""):
        self.items = []
        self.nombre = nombre

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def __str__(self):
        return f"{self.nombre}: {self.items}"


def hanoi_con_pilas(n, origen, destino, auxiliar):
    """Resuelve las Torres de Hanói moviendo discos entre objetos Pila."""
    if n == 1:
        disco = origen.desapilar()
        destino.apilar(disco)
        print(f"Mover disco {disco} de [{origen.nombre}] a [{destino.nombre}]")
        print(f"  Estado -> {origen} | {auxiliar} | {destino}")
        return

    # 1. Mover n-1 discos de origen a auxiliar usando destino como apoyo
    hanoi_con_pilas(n - 1, origen, auxiliar, destino)

    # 2. Mover el disco restante de origen a destino
    disco = origen.desapilar()
    destino.apilar(disco)
    print(f"Mover disco {disco} de [{origen.nombre}] a [{destino.nombre}]")
    print(f"  Estado -> {origen} | {auxiliar} | {destino}")

    # 3. Mover n-1 discos de auxiliar a destino usando origen como apoyo
    hanoi_con_pilas(n - 1, auxiliar, destino, origen)


# --- Ejemplo de uso ---
if __name__ == "__main__":
    num_discos = 3
    print(f"--- Resolviendo Torres de Hanói con {num_discos} discos ---\n")

    # Creación de las pilas (Torres)
    torre_origen = Pila("Origen")
    torre_auxiliar = Pila("Auxiliar")
    torre_destino = Pila("Destino")

    # Inicializar la torre de origen con los discos (el disco 3 es el más grande en la base, 1 en la cima)
    # Apilamos del mayor al menor para que el 1 quede en el tope.
    for disco in range(num_discos, 0, -1):
        torre_origen.apilar(disco)

    print("Estado inicial:")
    print(f"  {torre_origen}")
    print(f"  {torre_auxiliar}")
    print(f"  {torre_destino}\n")
    print("--- Movimientos ---")

    # Ejecución del algoritmo
    hanoi_con_pilas(num_discos, torre_origen, torre_destino, torre_auxiliar)

    print("\n--- Estado final ---")
    print(f"  {torre_origen}")
    print(f"  {torre_auxiliar}")
    print(f"  {torre_destino}")