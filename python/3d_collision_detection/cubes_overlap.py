
def are_cubes_overlapping(cube1, cube2):
    """
    2つの立方体が重なっているかを判定する

    :param cube1: (x, y, z, width, height, depth) タプル - 1つ目の立方体の情報
    :param cube2: (x, y, z, width, height, depth) タプル - 2つ目の立方体の情報
    :return: 重なっていれば True、そうでなければ False
    """
    x1, y1, z1, w1, h1, d1 = cube1
    x2, y2, z2, w2, h2, d2 = cube2

    # 各軸での分離条件を確認
    overlap_x = not (x1 + w1 < x2 or x2 + w2 < x1)  # X軸で重なっているか
    overlap_y = not (y1 + h1 < y2 or y2 + h2 < y1)  # Y軸で重なっているか
    overlap_z = not (z1 + d1 < z2 or z2 + d2 < z1)  # Z軸で重なっているか

    # 全軸で重なっていれば True
    return overlap_x and overlap_y and overlap_z
