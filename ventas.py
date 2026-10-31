def calcular_total(precio, cantidad):
    return precio + cantidad  # ¡El error intencional: es un '+' en lugar de un '*'!

if __name__ == "__main__":
    precio = 25
    cantidad = 2
    
    total = calcular_total(precio, cantidad)
    
    print(f"Precio: S/{precio}")
    print(f"Cantidad: {cantidad}")
    print(f"Total: S/{total}")