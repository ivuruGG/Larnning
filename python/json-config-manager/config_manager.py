
import json
import os
import shutil
from datetime import datetime
from cryptography.fernet import Fernet

class ConfigManager:
    def __init__(self, file_path, default_config=None, key=None):
        self.file_path = file_path
        self.default_config = default_config or {}
        self.data = self._load_config()
        self.backup_dir = "backups"
        os.makedirs(self.backup_dir, exist_ok=True)
        self.fernet = Fernet(key) if key else None

    def _load_config(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'rb' if self.fernet else 'r') as file:
                if self.fernet:
                    encrypted_data = file.read()
                    decrypted_data = self.fernet.decrypt(encrypted_data).decode()
                    return json.loads(decrypted_data)
                return json.load(file)
        return {}

    def save_config(self):
        self._create_backup()
        with open(self.file_path, 'wb' if self.fernet else 'w') as file:
            if self.fernet:
                encrypted_data = self.fernet.encrypt(json.dumps(self.data).encode())
                file.write(encrypted_data)
            else:
                json.dump(self.data, file, indent=4)

    def _create_backup(self):
        if os.path.exists(self.file_path):
            backup_name = os.path.join(
                self.backup_dir,
                f"{os.path.basename(self.file_path)}.{datetime.now().strftime('%Y%m%d%H%M%S')}.bak"
            )
            shutil.copy2(self.file_path, backup_name)

    def reset_to_defaults(self):
        self.data = self.default_config.copy()
        self.save_config()

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value
        self.save_config()

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            self.save_config()

    def list_backups(self):
        return sorted(os.listdir(self.backup_dir))

    def restore_backup(self, backup_name):
        backup_path = os.path.join(self.backup_dir, backup_name)
        if os.path.exists(backup_path):
            shutil.copy2(backup_path, self.file_path)
            self.data = self._load_config()
        else:
            raise FileNotFoundError(f"バックアップが見つかりません: {backup_name}")
