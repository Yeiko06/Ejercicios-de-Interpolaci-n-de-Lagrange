import numpy as np
import matplotlib.pyplot as plt
import time

# Datos del problema
x_points = np.array([0.5, 1.0, 1.5, 2.0])
y_points = np.array([1.2, 2.3, 3.7, 5.2])

# Función de interpolación de Lagrange
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

# Estimación en x = 1.25
x_val = 1.25
start = time.time()
y_val = lagrange_interpolation(x_val, x_points, y_points)
end = time.time()
print(f"Deformación estimada en x = {x_val} m: {y_val:.4f} mm")
print(f"Tiempo de ejecución: {end - start:.6f} segundos")

# Gráfica
x_values = np.linspace(0.5, 2.0, 200)
y_values = [lagrange_interpolation(x, x_points, y_points) for x in x_values]

plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label="Interpolación", color="blue")
plt.scatter(x_points, y_points, color="red", label="Datos")
plt.axvline(x_val, color="gray", linestyle="--", label=f"x = {x_val}")
plt.axhline(y_val, color="gray", linestyle="--")
plt.title("Interpolación de Lagrange - Deformación en una viga")
plt.xlabel("Posición (m)")
plt.ylabel("Deformación (mm)")
plt.legend()
plt.grid()
plt.savefig("ejercicio1_viga.png")
plt.show()
