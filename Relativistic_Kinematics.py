import numpy as np

def calculate_time_dilation(mass, radius):
    """
    Calculates the Schwarzschild time dilation factor.
    Units: G=1, c=1 (Natural Units)
    """
    rs = 2 * mass # Schwarzschild radius
    if radius <= rs:
        return float('inf') # Time dilation approach infinity at event horizon
    
    # Formula: t' = t * sqrt(1 - rs/r)
    dilation_factor = np.sqrt(1 - rs/radius)
    return dilation_factor

def get_light_bending_angle(mass, impact_parameter):
    """
    Calculates the deflection of light in a gravitational field.
    Formula: alpha = 4GM / (c^2 * b)
    """
    angle = (4 * mass) / impact_parameter
    return angle

# --- Research Data Generation ---
M = 10.0 # Mass of the virtual stellar body
distances = [100, 50, 25, 21] # Radial distances (r)

print("--- Engine Output: Relativistic Physical Parameters ---")
for r in distances:
    td = calculate_time_dilation(M, r)
    print(f"Distance: {r} units | Time Flow: {td*100:.2f}% of coordinate time")
