class Pila:
    """Implementación de la estructura de datos Pila (Stack)."""
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def tamano(self):
        return len(self.items)


def evaluar_posfija(expresion):
    """Evalúa una expresión aritmética en notación posfija separada por espacios."""
    pila = Pila()
    tokens = expresion.split()

    for token in tokens:
        # Si el token es un número, lo convertimos y lo apilamos
        try:
            # Intentamos convertir a float (soporta enteros y decimales)
            valor = float(token)
            pila.apilar(valor)
        except ValueError:
            # Si no es un número, debe ser un operador
            if token in ['+', '-', '*', '/', '^']:
                if pila.tamano() < 2:
                    raise ValueError("Expresión mal formada: faltan operandos.")
                
                b = pila.desapilar()
                if token == '+':
                    a = pila.desapilar()
                    pila.apilar(a + b)
                elif token == '-':
                    a = pila.desapilar()
                    pila.apilar(a - b)
                elif token == '*':
                    a = pila.desapilar()
                    pila.apilar(a * b)
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("Error: División entre cero.")
                    a = pila.desapilar()
                    pila.apilar(a / b)
                elif token == '^':
                    a = pila.desapilar()
                    pila.apilar(a ** b)
            else:
                raise ValueError(f"Token no reconocido: {token}")

    if pila.tamano() != 1:
        raise ValueError("Expresión mal formada: demasiados operandos.")
    
    return pila.desapilar()


# --- Ejemplo de uso ---
if __name__ == "__main__":
    # Expresión equivalente a (3 + 4) * 2 en posfija
    expresion_ejemplo = "3 4 + 2 *"
    print(f"Expresión posfija: {expresion_ejemplo}")
    resultado = evaluar_posfija(expresion_ejemplo)
    print(f"Resultado de la evaluación: {resultado}")