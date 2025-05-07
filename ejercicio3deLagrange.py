import numpy as np
import matplotlib.pyplot as plt

# Datos del problema
x_points = np.array([2.0, 4.0, 6.0, 8.0])
y_points = np.array([2500, 2300, 2150, 2050])

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
x_val = 5.0
y_val = lagrange_interpolation(x_val, x_points, y_points)
print(f"Consumo estimado a {x_val} km: {y_val:.2f} kg/h")

# Gráfica
x_values = np.linspace(2.0, 8.0, 200)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label="Interpolación", color="purple")
plt.scatter(x_points, y_points, color="black", label="Datos")
plt.axvline(x_val, color="gray", linestyle="--", label=f"x = {x_val}")
plt.axhline(y_val, color="gray", linestyle="--")
plt.title("Interpolación de Lagrange - Consumo de combustible")
plt.xlabel("Altitud (km)")
plt.ylabel("Consumo (kg/h)")
plt.legend()
plt.grid()
plt.savefig("ejercicio3_combustible.png")
plt.show()
