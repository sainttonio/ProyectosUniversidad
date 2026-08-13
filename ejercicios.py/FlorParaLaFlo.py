from math import cos, sin, radians
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle
from matplotlib.animation import FuncAnimation
import matplotlib.patheffects as path_effects

# Configuración
n_petals = 24              # número de pétalos
petal_distance = 0.8       # distancia desde el centro
petal_width = 2.0          # ancho del pétalo
petal_height = 0.6         # largo del pétalo
petal_color = "#FFFF66"    # amarillo neón
edge_color = "#FFD700"     # dorado brillante

# Crear figura con fondo negro
fig, ax = plt.subplots(figsize=(6, 7))
fig.patch.set_facecolor("black")
ax.set_facecolor("black")
ax.set_aspect('equal')
ax.set_xlim(-2, 2)
ax.set_ylim(-2.5, 2)   # espacio para el nombre abajo
ax.axis('off')

# Lista de pétalos (con efecto neón)
petals = []
for i in range(n_petals):
    angle_deg = i * (360 / n_petals)
    angle_rad = cos(angle_deg)  # para que matplotlib rote los pétalos
    cx = petal_distance * cos(radians(angle_deg))
    cy = petal_distance * sin(radians(angle_deg))

    # Capa de resplandor (más grande y difusa)
    glow = Ellipse((cx, cy), width=petal_width * 1.2, height=petal_height * 1.2,
                   angle=angle_deg, alpha=0.15, linewidth=0,
                   facecolor=petal_color)
    petals.append(glow)

    # Pétalo principal
    petal = Ellipse((cx, cy), width=petal_width, height=petal_height,
                    angle=angle_deg, alpha=0.95, linewidth=1.5,
                    edgecolor=edge_color, facecolor=petal_color)
    petals.append(petal)

# Centro de la flor con efecto neón
center_glow = Circle((0, 0), 0.5, facecolor="#FFFF66", alpha=0.15, linewidth=0)
center_outer = Circle((0, 0), 0.35, facecolor="#FFD700", edgecolor="#FFFF99", linewidth=2)
center_inner = Circle((0, 0), 0.18, facecolor="#FFFF33", edgecolor="#FFD700", linewidth=1.5)

ax.add_patch(center_glow)
ax.add_patch(center_outer)
ax.add_patch(center_inner)

# --- Texto con borde estilo neón amarillo ---
text = ax.text(0, -2.0, "Para ti Bibi<3 ", fontsize=28, ha="center", va="center",
               color="black", weight="bold")

# Efecto neón amarillo alrededor de las letras
text.set_path_effects([
    path_effects.Stroke(linewidth=6, foreground="#FFFF66", alpha=0.9),
    path_effects.Stroke(linewidth=12, foreground="#FFFF66", alpha=0.2),
    path_effects.Normal()
])

# Función de animación
def animate(i):
    if i < len(petals):
        ax.add_patch(petals[i])

# Animación
ani = FuncAnimation(fig, animate, frames=len(petals), interval=150, repeat=False)

plt.show()