# Comparacion-de-Programacion-Tradicional-y-POO-en-Python
Objetivo: Desarrollar habilidades prácticas en la Programación Tradicional y la Programación Orientada a Objetos (POO) mediante la implementación de un programa en Python para determinar el promedio semanal del clima.
# Comparación entre Programación Tradicional y Programación Orientada a Objetos en Python

## 🎯 Objetivo
Desarrollar un programa en Python que calcule el **promedio semanal del clima**, aplicando dos enfoques diferentes: **Programación Tradicional** y **Programación Orientada a Objetos (POO)**.

---

## 🧮 Programación Tradicional

Este enfoque utiliza funciones independientes para realizar tareas específicas:

- `ingresar_temperaturas()`: Solicita las temperaturas de los 7 días de la semana.
- `calcular_promedio()`: Calcula el promedio de las temperaturas ingresadas.
- La lógica del programa se estructura de manera lineal dentro de una función principal `main()`.

**Ventajas**:
- Código simple y directo.
- Fácil de entender para principiantes.

**Desventajas**:
- Difícil de escalar en proyectos grandes.
- Menor modularidad y reutilización.

---

## 🧱 Programación Orientada a Objetos (POO)

Este enfoque modela la información mediante clases y objetos:

- `DiaClima`: Representa un día con una temperatura, utilizando encapsulamiento.
- `SemanaClima`: Administra los 7 días de clima y ofrece métodos para ingresar datos y calcular el promedio.

**Conceptos aplicados**:
- **Encapsulamiento**: Atributos privados con métodos `set` y `get`.
- **Composición**: La clase `SemanaClima` contiene objetos de la clase `DiaClima`.

**Ventajas**:
- Código más organizado, escalable y mantenible.
- Facilita la reutilización de componentes y la extensión del programa.

**Desventajas**:
- Más complejo de entender inicialmente.
- Requiere mayor planeación en la estructura.

---

## 📊 Comparación General

| Aspecto                          | Tradicional                             | POO                                      |
|----------------------------------|------------------------------------------|------------------------------------------|
| Estructura                       | Funciones independientes                 | Clases y objetos                          |
| Escalabilidad                    | Limitada                                 | Alta                                     |
| Encapsulamiento                  | No                                       | Sí                                       |
| Mantenimiento                    | Más difícil                              | Más fácil                                |
| Ideal para                       | Tareas simples o scripts pequeños        | Proyectos medianos a grandes             |

---

## 📁 Archivos incluidos

- `clima_tradicional.py`: Código con funciones.
- `clima_poo.py`: Código con clases.
- `README.md`: Documento explicativo.

---

## 🚀 Cómo ejecutar

```bash
python clima_tradicional.py
python clima_poo.py
