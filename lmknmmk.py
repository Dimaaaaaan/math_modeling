import numpy as np
import matplotlib.pyplot as plt

# Константы
G = 6.674e-11  # гравитационная постоянная
M_sun = 1.989e30  # масса Солнца

# Параметры Земли
mass_earth = 5.972e24
pos_earth = np.array([1.496e11, 0])  # начальная позиция (м)
vel_earth = np.array([0, 29.78e3])  # начальная скорость (м/с)

# Параметры Фаэтона
mass_phaethon = 4.6e10
pos_phaethon = np.array([2e11, 0])  # начальная позиция (м)
vel_phaethon = np.array([0, 24e3])  # начальная скорость (м/с)

# Время моделирования
dt = 60 * 60 * 24  # шаг времени (1 день в секундах)
num_steps = 365  # количество шагов (1 год)

# Массивы для хранения траекторий
earth_trajectory = []
phaethon_trajectory = []

# Моделирование движения
for step in range(num_steps):
    # Расстояние до Солнца
    r_earth = np.linalg.norm(pos_earth)
    r_phaethon = np.linalg.norm(pos_phaethon)

    # Сила тяжести на Землю
    force_earth = -G * M_sun * mass_earth / r_earth**2 * (pos_earth / r_earth)
    # Сила тяжести на Фаэтон
    force_phaethon = -G * M_sun * mass_phaethon / r_phaethon**2 * (pos_phaethon / r_phaethon)

    # Обновление скоростей
    vel_earth += force_earth / mass_earth * dt
    vel_phaethon += force_phaethon / mass_phaethon * dt

    # Обновление позиций
    pos_earth += vel_earth * dt
    pos_phaethon += vel_phaethon * dt

    # Сохранение траекторий
    earth_trajectory.append(pos_earth.copy())
    phaethon_trajectory.append(pos_phaethon.copy())

# Преобразование в массивы для удобства
earth_trajectory = np.array(earth_trajectory)
phaethon_trajectory = np.array(phaethon_trajectory)

ani = FuncAnimation(fig, animate, frames=frames, interval=30)

# Визуализация
plt.figure(figsize=(10, 10))
plt.plot(earth_trajectory[:, 0], earth_trajectory[:, 1], label='Земля', color='blue')
plt.plot(phaethon_trajectory[:, 0], phaethon_trajectory[:, 1], label='Фаэтон (3200)', color='orange')
plt.scatter(0, 0, color='yellow', s=100, label='Солнце')  # Солнце
plt.xlabel('X (м)')
plt.ylabel('Y (м)')
plt.title('Моделирование движения Земли и Фаэтона в поле тяжести Солнца')
plt.axis('equal')
plt.legend()
plt.grid()
ani.save('fig_2.gif')