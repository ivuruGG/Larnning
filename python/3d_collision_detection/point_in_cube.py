
def is_point_in_cube(point, cube):
    """
    点が立方体内にあるかを判定する

    :param point: (x, y, z) タプル - 判定する点の座標
    :param cube: (x, y, z, width, height, depth) タプル - 立方体の情報
        x, y, z: 立方体の起点座標
        width, height, depth: 立方体の幅、高さ、奥行き
    :return: 点が立方体内にあれば True、そうでなければ False
    """
    px, py, pz = point
    cx, cy, cz, width, height, depth = cube

    # 点が立方体の各軸の範囲内に収まっているかを確認
    in_x = cx <= px <= cx + width
    in_y = cy <= py <= cy + height
    in_z = cz <= pz <= cz + depth

    return in_x and in_y and in_z
