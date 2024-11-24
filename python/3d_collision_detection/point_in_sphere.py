
def is_point_in_sphere(point, sphere):
    """
    点が球の内部にあるかを判定する

    :param point: (x, y, z) タプル - 判定する点の座標
    :param sphere: (x, y, z, radius) タプル - 球の情報
        x, y, z: 球の中心座標
        radius: 球の半径
    :return: 点が球の内部にあれば True、そうでなければ False
    """
    px, py, pz = point
    sx, sy, sz, radius = sphere

    # 点と球の中心間の距離の2乗を計算
    distance_squared = (px - sx) ** 2 + (py - sy) ** 2 + (pz - sz) ** 2

    # 距離が半径の2乗以下であれば内部にある
    return distance_squared <= radius ** 2
