
def are_cubes_overlapping(cube1, cube2):
    x1, y1, z1, w1, h1, d1 = cube1
    x2, y2, z2, w2, h2, d2 = cube2

    overlap_x = not (x1 + w1 < x2 or x2 + w2 < x1)
    overlap_y = not (y1 + h1 < y2 or y2 + h2 < y1)
    overlap_z = not (z1 + d1 < z2 or z2 + d2 < z1)

    return overlap_x and overlap_y and overlap_z
