
import math

def are_spheres_overlapping(sphere1, sphere2):
    """
    2つの球が重なっているかを判定する

    :param sphere1: (x, y, z, radius) タプル - 1つ目の球の情報
    :param sphere2: (x, y, z, radius) タプル - 2つ目の球の情報
    :return: 重なっていれば True、そうでなければ False
    """
    x1, y1, z1, r1 = sphere1
    x2, y2, z2, r2 = sphere2

    # 球の中心間の距離の2乗を計算
    distance_squared = (x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2

    # 半径の合計の2乗を計算
    radius_sum_squared = (r1 + r2) ** 2

    # 中心間の距離が半径の合計以下であれば重なっている
    return distance_squared <= radius_sum_squared
