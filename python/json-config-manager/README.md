
# JSON Config Manager

JSON Config Managerは、JSON形式の設定ファイルを簡単に管理できるツールです。
CLI（コマンドラインインターフェース）とバックアップ機能を備え、さらに設定の暗号化や復元もサポートしています。

---

## 機能

- **設定管理**: 設定ファイルの読み取り、更新、削除、一覧表示。
- **バックアップ**: 設定ファイルを保存するたびに自動でバックアップを作成。
- **デフォルト設定のリセット**: デフォルト値へのリセット機能。
- **復元機能**: 任意のバックアップから復元。
- **暗号化**: 設定ファイルを暗号化して保存。

---

## 必要環境

- Python 3.8以上
- インストール済みライブラリ:
  - `cryptography`

インストールは以下のコマンドで可能です:

```bash
pip install -r requirements.txt
```

---

## 使用方法

### CLIツール

CLIを使って設定ファイルを操作できます。以下の例を参照してください:

```bash
# 新しい設定を追加
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

## プロジェクト構成

```
json-config-manager/
├── cli_tool.py           # CLIツール
├── config_manager.py     # 設定管理モジュール
├── requirements.txt      # 必要ライブラリ
├── README.md             # このファイル
└── backups/              # バックアップディレクトリ（自動作成）
```

---

## ライセンス

このプロジェクトはMITライセンスのもとで公開されています。自由に利用、変更、再配布できます。

---

## 貢献

- Issueを報告する
- 新しい機能を提案する
- コードを改善するプルリクエストを送る

---

## 問い合わせ

何か質問があれば、[issue](https://github.com/)を作成するか、直接連絡してください。
