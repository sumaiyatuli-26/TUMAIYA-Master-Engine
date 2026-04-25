import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 1. Spacetime Grid Setup
grid_size = 100
x = np.linspace(-5, 5, grid_size)
y = np.linspace(-5, 5, grid_size)
X, Y = np.meshgrid(x, y)

# 2. Gravitational Wave Parameters
A = 0.5        # Wave Amplitude
k = 2.0        # Wave Number
omega = 5.0    # Angular Frequency

def get_curvature(t):
    # Radial distance from the source
    R = np.sqrt(X**2 + Y**2)
    
    # Sinusoidal wave dissipation modeling spacetime ripples
    Z = A * np.exp(-0.5 * R) * np.cos(k * R - omega * t)
    
    # Adding Singularity effect (Central Gravitational Well)
    singularity = - (1.5 / (R + 0.2))
    return Z + singularity

# 3. Visualization and Animation Engine
fig = plt.figure(figsize=(10, 7), facecolor='black')
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')

def update(frame):
    ax.clear()
    t = frame * 0.1
    Z = get_curvature(t)
    
    # Render surface using Magma colormap (Standard in Astrophysical Visualization)
    surf = ax.plot_surface(X, Y, Z, cmap='magma', antialiased=False, alpha=0.8)
    
    # Plot formatting
    ax.set_zlim(-5, 2)
    ax.axis('off')
    ax.set_title(f"Dynamic Spacetime Ripple (t={t:.1f}s)", color='white', fontsize=14)
    return surf,

# Execute Animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)
plt.show()
