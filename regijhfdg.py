import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Настройки
num_particles = 6
num_positive = 3
num_negative = 3
time_steps = 100

# Начальные позиции частиц
positions = np.array([
    [-5, 0],   # Положительная частица 1
    [-4, 2],   # Положительная частица 2
    [-3, -2],  # Положительная частица 3
    [5, 0],    # Отрицательная частица 1
    [4, -2],   # Отрицательная частица 2
    [3, 2]     # Отрицательная частица 3
])

# Скорости частиц (вектор направления к центру)
velocities = np.zeros((num_particles, 2))
for i in range(num_particles):
    direction = -positions[i] / np.linalg.norm(positions[i])  # Направление к центру
    velocities[i] = direction * 0.1  # Устанавливаем скорость

# Функция обновления для анимации
def update(frame):
    global positions
    positions += velocities  
    scatter.set_offsets(positions)  # Обновляем положение частиц в графике
    return scatter,

# Настройка графика
fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.set_title('Моделирование потока заряженных частиц')
scatter = ax.scatter(positions[:, 0], positions[:, 1], c=['blue'] * num_positive + ['red'] * num_negative)

# Анимация
ani = animation.FuncAnimation(fig, update, frames=time_steps, interval=50, blit=True)
plt.axhline(0, color='black', lw=2)  # Ось X
plt.axvline(0, color='black', lw=2)  # Ось Y
plt.show()