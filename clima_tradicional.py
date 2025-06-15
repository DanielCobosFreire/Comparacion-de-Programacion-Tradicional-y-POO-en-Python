# Función para ingresar las temperaturas de los 7 días de la semana
def ingresar_temperaturas():
    temperaturas = []  # Lista vacía para almacenar las temperaturas
    for i in range(7):  # Bucle de 7 iteraciones (una por cada día)
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)  # Agrega la temperatura a la lista
    return temperaturas  # Devuelve la lista completa

# Función para calcular el promedio de una lista de temperaturas
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)  # Promedio = suma / cantidad

# Función principal que organiza la lógica del programa
def main():
    print("== Promedio Semanal del Clima (Programación Tradicional) ==")
    temps = ingresar_temperaturas()  # Llamada a la función para ingresar datos
    promedio = calcular_promedio(temps)  # Llamada a la función para calcular promedio
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")  # Muestra resultado

# Punto de entrada del programa
if __name__ == "__main__":
    main()
