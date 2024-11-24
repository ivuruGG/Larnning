
# 🌟 JSON Config Manager

JSON Config Manager は、JSON形式の設定ファイルを簡単に管理できるツールです。
CLI（コマンドラインインターフェース）とGUI（グラフィカルユーザーインターフェース）を備え、以下の機能を提供します。

---

## 🚀 主な機能

- **設定管理**: JSON形式の設定ファイルを読み書き、更新、削除が可能。
- **バックアップ**: 設定を保存するたびにバックアップを自動生成。
- **デフォルトリセット**: デフォルト設定にワンクリックでリセット。
- **復元機能**: 任意のバックアップを簡単に復元。
- **暗号化**: 設定ファイルを安全に暗号化して保存。
- **多様な操作方法**:
  - **CLI（コマンドライン）**: 細かい操作が可能。
  - **GUI（グラフィカル）**: シンプルで使いやすい操作画面。

---

## 🛠 必要環境

- **Python**: 3.8以上
- **ライブラリ**: `cryptography`, `tkinter`（標準ライブラリ）

依存関係をインストールするには、以下のコマンドを使用してください:

```bash
pip install -r requirements.txt
```

---

## 💻 使用方法

### 1. CLIツール

コマンドラインで設定ファイルを操作できます。以下は使用例です:

```bash
# 設定ファイルに新しい設定を追加
python cli_tool.py --file config.json --set theme dark

# 設定を取得
python cli_tool.py --file config.json --get theme

# 設定を削除
python cli_tool.py --file config.json --delete theme

# すべての設定を表示
python cli_tool.py --file config.json --show

# デフォルト設定にリセット
python cli_tool.py --file config.json --reset

# バックアップ一覧を表示
python cli_tool.py --file config.json --list-backups

# バックアップから復元
python cli_tool.py --file config.json --restore config.json.20241124120000.bak
```

---

### 2. GUIツール

GUIで直感的に設定を操作できます。

#### 起動
```bash
python gui_tool.py
```

#### 主な操作
1. **設定をリストで確認**:
   - 画面中央のリストボックスで設定を表示。
2. **設定を追加**:
   - 「設定を追加」ボタンをクリックし、新しいキーと値を入力。
3. **設定を削除**:
   - 削除したい設定を選択し、「設定を削除」ボタンをクリック。
4. **デフォルトリセット**:
   - 「デフォルトにリセット」ボタンをクリック。

---

## 📂 プロジェクト構成

```
json-config-manager/
├── cli_tool.py           # CLIツール
├── gui_tool.py           # GUIツール
├── config_manager.py     # 設定管理モジュール
├── requirements.txt      # 必要ライブラリ
├── README.md             # プロジェクトの説明
└── backups/              # バックアップディレクトリ（自動作成）
```

---

## 🌟 特長

- **安全性**: 設定ファイルを暗号化して保存可能。
- **柔軟性**: CLIとGUIの両方に対応。
- **自動化**: バックアップ機能で安心。

---

## 📜 ライセンス

このプロジェクトはMITライセンスのもとで公開されています。詳細は `LICENSE` ファイルをご確認ください。

---

## 🤝 コントリビューション

貢献を歓迎します！以下の手順で行えます:

1. このリポジトリをフォークします。
2. 新しいブランチを作成します:
   ```bash
   git checkout -b feature/your-feature
   ```
3. 変更をコミットします:
   ```bash
   git commit -m "Add your feature"
   ```
4. ブランチをプッシュします:
   ```bash
   git push origin feature/your-feature
   ```
5. プルリクエストを作成します。

---

## 📧 問い合わせ

質問や提案があれば、[issue](https://github.com/)を作成するか、直接ご連絡ください。
