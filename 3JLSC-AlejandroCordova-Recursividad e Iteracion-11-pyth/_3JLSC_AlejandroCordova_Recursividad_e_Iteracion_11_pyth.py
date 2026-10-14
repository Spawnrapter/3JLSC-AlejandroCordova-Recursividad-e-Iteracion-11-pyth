# Solución recursiva adaptada a Python
def suma_recursiva(n):
    if n <= 9:
        return n
    else:
        # Se usa // para la división entera
        return suma_recursiva(n // 10) + (n % 10)

# Solución iterativa adaptada a Python
def suma_iterativa(n):
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n

def main():
    # Se solicita la cantidad de números a evaluar
    cantidad = int(input("¿Cuantos numeros va a ingresar? "))
    
    # Bucle para iterar según la cantidad ingresada
    for i in range(cantidad):
        numero = int(input(f"\nIngrese el numero {i + 1}: "))
        
        # Se muestran los resultados
        print(f"Resultado con suma recursiva: {suma_recursiva(numero)}")
        print(f"Resultado con suma iterativa: {suma_iterativa(numero)}")

if __name__ == "__main__":
    main()
