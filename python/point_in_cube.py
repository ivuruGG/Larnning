
def is_point_in_cube(point, cube):
    px, py, pz = point
    cx, cy, cz, width, height, depth = cube

    in_x = cx <= px <= cx + width
    in_y = cy <= py <= cy + height
    in_z = cz <= pz <= cz + depth

    return in_x and in_y and in_z
