
import numpy as np


def generate_fixed_positions(size):
        # Generar posiciones fijas para los nodos
        positions = {}
        angle_step = 2 * 3.14159 / size
        for i in range(size):
            angle = i * angle_step
            x = 10 * np.cos(angle)
            y = 10 * np.sin(angle)
            positions[i] = (x, y)
        return positions