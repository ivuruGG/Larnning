
import math

def are_spheres_overlapping(sphere1, sphere2):
    x1, y1, z1, r1 = sphere1
    x2, y2, z2, r2 = sphere2

    distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2
    radius_sum_squared = (r1 + r2) ** 2

    return distance_squared <= radius_sum_squared
