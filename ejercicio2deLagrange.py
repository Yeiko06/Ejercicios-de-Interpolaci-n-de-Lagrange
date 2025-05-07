import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
x_points = np.array([1.0, 2.5, 4.0, 5.5])
y_points = np.array([85, 78, 69, 60])

# Función de interpolación
def lagrange_interpolation(x, x_points, y_points):
    n = len(x_points)
    result = 0
    for i in range(n):
        term = y_points[i]
        for j in range(n):
            if i != j:
                term *= (x - x_points[j]) / (x_points[i] - x_points[j])
        result += term
    return result

# Estimación
x_val = 3.0
y_val = lagrange_interpolation(x_val, x_points, y_points)
print(f"Temperatura estimada a {x_val} cm: {y_val:.2f} °C")

# Gráfica
x_values = np.linspace(1.0, 5.5, 200)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label="Interpolación", color="green")
plt.scatter(x_points, y_points, color="orange", label="Datos")
plt.axvline(x_val, color="gray", linestyle="--", label=f"x = {x_val}")
plt.axhline(y_val, color="gray", linestyle="--")
plt.title("Interpolación de Lagrange - Temperatura del motor")
plt.xlabel("Profundidad (cm)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid()
plt.savefig("ejercicio2_motor.png")
plt.show()
