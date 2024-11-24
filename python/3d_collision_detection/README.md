
# 3D Collision Detection Algorithms

このリポジトリでは、3D空間での当たり判定アルゴリズムを実装しています。ゲーム開発や物理シミュレーションで役立つ基本的な4種類の判定方法を提供します。

---

## 📂 ファイル構成

- `point_in_cube.py`: 点が立方体の内部にあるかを判定
- `cubes_overlap.py`: 2つの立方体が重なっているかを判定
- `spheres_overlap.py`: 2つの球が重なっているかを判定
- `point_in_sphere.py`: 点が球の内部にあるかを判定

---

## ✨ 使用例

### 1. 点と立方体の当たり判定

点が立方体の内部にあるかをチェックします。

```python
from point_in_cube import is_point_in_cube

point = (5, 5, 5)
cube = (0, 0, 0, 10, 10, 10)
print(is_point_in_cube(point, cube))  # 出力: True
```

![点と立方体の当たり判定](img?text=Point+in+Cube+Diagram)

---

### 2. 立方体同士の当たり判定

2つの立方体が重なっているかをチェックします。

```python
from cubes_overlap import are_cubes_overlapping

cube1 = (0, 0, 0, 10, 10, 10)
cube2 = (5, 5, 5, 10, 10, 10)
print(are_cubes_overlapping(cube1, cube2))  # 出力: True
```

![立方体同士の当たり判定](img?text=Cubes+Overlap+Diagram)

---

### 3. 球と球の当たり判定

2つの球が重なっているかをチェックします。

```python
from spheres_overlap import are_spheres_overlapping

sphere1 = (0, 0, 0, 5)
sphere2 = (6, 0, 0, 5)
print(are_spheres_overlapping(sphere1, sphere2))  # 出力: True
```

![球と球の当たり判定](img?text=Spheres+Overlap+Diagram)

---

### 4. 点と球の当たり判定

点が球の内部にあるかをチェックします。

```python
from point_in_sphere import is_point_in_sphere

point = (3, 4, 5)
sphere = (0, 0, 0, 7)
print(is_point_in_sphere(point, sphere))  # 出力: True
```

![点と球の当たり判定](img?text=Point+in+Sphere+Diagram)

---

## 📘 詳細解説

### アルゴリズムの特長
- **軽量で効率的**: 必要最小限の計算で結果を得られるように設計
- **実用性**: ゲームエンジンや物理シミュレーションに簡単に統合可能
- **汎用性**: 点、立方体、球の基本形状に対応

### 最適化ポイント
- 距離の計算では平方根を省略し、パフォーマンスを向上
- 軸ごとの分離を確認することで計算コストを削減

---

## 🛠 開発環境

- **Python**: 3.8以上
- 必要ライブラリ: なし（標準ライブラリのみ使用）

---

## 🖼 図解ギャラリー

以下のリンクから図解付きの詳細説明をご覧ください。
- 点と立方体: [Point in Cube](img)
- 立方体同士: [Cubes Overlap](img)
- 球と球: [Spheres Overlap](img)
- 点と球: [Point in Sphere](img)

---

## 🤝 貢献方法

1. このリポジトリをフォーク
2. 新しいブランチを作成 (`git checkout -b feature/your-feature`)
3. 変更をコミット (`git commit -m 'Add your feature'`)
4. プッシュ (`git push origin feature/your-feature`)
5. プルリクエストを作成

---

## 📄 ライセンス

MITライセンスのもとで公開されています。詳細は `LICENSE` ファイルをご覧ください。

---

## 📧 サポート

質問や提案がある場合は、[issue](https://github.com/) を作成するか、直接お問い合わせください。
