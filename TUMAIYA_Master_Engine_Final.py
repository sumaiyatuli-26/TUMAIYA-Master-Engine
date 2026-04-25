import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def run_master_engine():
    # --- Physical Parameters ---
    mass = 10.0      # Mass of the virtual stellar object
    grid_res = 80    # Grid resolution
    
    # 1. Spacetime Grid Generation
    x = np.linspace(-15, 15, grid_res)
    y = np.linspace(-15, 15, grid_res)
    X, Y = np.meshgrid(x, y)
    R = np.sqrt(X**2 + Y**2) + 0.1 # Avoid division by zero
    
    # 2. Curvature Calculation (Z-axis represents spacetime warping)
    Z = - (mass / R)

    # 3. Data Output (Relativistic Analysis)
    print("="*50)
    print("   MASTER ENGINE: RELATIVISTIC DATA ANALYSIS")
    print("="*50)
    
    check_points = [30, 20, 15, 12, 10.1] # Distance from center (r)
    for r in check_points:
        # Schwarzschild Time Dilation calculation
        rs = 2 * mass
        if r > rs:
            time_flow = np.sqrt(1 - rs/r)
            status = f"{time_flow*100:.2f}% normal speed"
        else:
            status = "SINGULARITY REACHED (Time Frozen)"
        
        # General Relativistic Light Deflection (Alpha = 4GM/c^2r)
        bending = (4 * mass) / r
        
        print(f"Distance: {r:4} | Time: {status:25} | Deflection: {bending:.3f} rad")
    
    # 4. Visualization (3D Spacetime Fabric)
    fig = plt.figure(figsize=(12, 8), facecolor='black')
    ax = fig.add_subplot(111, projection='3d')
    ax.set_facecolor('black')

    # Plot Design
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolors='white', lw=0.05, alpha=0.9)
    
    # Labeling and Aesthetics
    ax.set_title("3D Spacetime Curvature Simulation", color='white', fontsize=15)
    ax.set_zlim(-5, 0)
    ax.axis('off') 
    
    print("\n[Simulation Successful] Visualizing Spacetime Fabric...")
    plt.show()

if __name__ == "__main__":
    run_master_engine()
