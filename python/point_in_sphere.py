
def is_point_in_sphere(point, sphere):
    px, py, pz = point
    sx, sy, sz, radius = sphere

    distance_squared = (px - sx) ** 2 + (py - sy) ** 2 + (pz - sz) ** 2
    return distance_squared <= radius ** 2
