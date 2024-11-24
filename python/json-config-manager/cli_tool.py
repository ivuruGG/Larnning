
import argparse
from config_manager import ConfigManager
from cryptography.fernet import Fernet

DEFAULT_KEY = Fernet.generate_key()  # 必要に応じて保存

def main():
    parser = argparse.ArgumentParser(description="JSON設定ファイルマネージャー")
    parser.add_argument("--file", type=str, required=True, help="設定ファイルのパス")
    parser.add_argument("--get", type=str, help="指定されたキーの値を取得")
    parser.add_argument("--set", nargs=2, metavar=("KEY", "VALUE"), help="設定を更新")
    parser.add_argument("--delete", type=str, help="指定されたキーを削除")
    parser.add_argument("--show", action="store_true", help="すべての設定を表示")
    parser.add_argument("--reset", action="store_true", help="デフォルト設定にリセット")
    parser.add_argument("--list-backups", action="store_true", help="バックアップ一覧を表示")
    parser.add_argument("--restore", type=str, help="指定したバックアップを復元")
    args = parser.parse_args()

    config = ConfigManager(args.file, key=DEFAULT_KEY)

    if args.get:
        print(f"{args.get}: {config.get(args.get)}")
    elif args.set:
        key, value = args.set
        config.set(key, value)
        print(f"設定を更新しました: {key} = {value}")
    elif args.delete:
        config.delete(args.delete)
        print(f"キーを削除しました: {args.delete}")
    elif args.show:
        print("現在の設定:")
        for key, value in config.data.items():
            print(f"{key}: {value}")
    elif args.reset:
        config.reset_to_defaults()
        print("デフォルト設定にリセットしました")
    elif args.list_backups:
        print("バックアップ一覧:")
        for backup in config.list_backups():
            print(backup)
    elif args.restore:
        config.restore_backup(args.restore)
        print(f"バックアップを復元しました: {args.restore}")

if __name__ == "__main__":
    main()
