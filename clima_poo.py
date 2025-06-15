# Clase que representa un día con temperatura
class DiaClima:
    def __init__(self, temperatura=0.0):
        # Temperatura privada (encapsulada)
        self.__temperatura = temperatura

    # Método para establecer la temperatura
    def set_temperatura(self, temperatura):
        self.__temperatura = temperatura

    # Método para obtener la temperatura
    def get_temperatura(self):
        return self.__temperatura

# Clase que representa una semana con 7 días de clima
class SemanaClima:
    def __init__(self):
        # Lista de 7 objetos DiaClima
        self.dias = [DiaClima() for _ in range(7)]

    # Método para ingresar la temperatura de cada día
    def ingresar_temperaturas(self):
        for i in range(7):
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.dias[i].set_temperatura(temp)  # Se establece la temperatura en cada objeto

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        # Se suman las temperaturas de cada objeto DiaClima
        total = sum(dia.get_temperatura() for dia in self.dias)
        return total / len(self.dias)  # Se calcula y retorna el promedio

# Función principal que organiza el flujo del programa
def main():
    print("== Promedio Semanal del Clima (POO) ==")
    semana = SemanaClima()  # Se crea una instancia de SemanaClima
    semana.ingresar_temperaturas()  # Se ingresan los datos
    promedio = semana.calcular_promedio()  # Se calcula el promedio
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")  # Se imprime el resultado

# Punto de entrada del programa
if __name__ == "__main__":
    main()
