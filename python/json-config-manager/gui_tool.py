
import tkinter as tk
from tkinter import messagebox, simpledialog
from config_manager import ConfigManager
from cryptography.fernet import Fernet

DEFAULT_KEY = Fernet.generate_key()  # 必要に応じて保存

class ConfigGUI:
    def __init__(self, root, config):
        self.root = root
        self.config = config

        self.root.title("JSON設定ファイルマネージャー")
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # ボタン群
        self.add_button = tk.Button(self.frame, text="設定を追加", command=self.add_setting)
        self.add_button.pack(pady=5)

        self.delete_button = tk.Button(self.frame, text="設定を削除", command=self.delete_setting)
        self.delete_button.pack(pady=5)

        self.refresh_button = tk.Button(self.frame, text="設定をリロード", command=self.load_config)
        self.refresh_button.pack(pady=5)

        self.reset_button = tk.Button(self.frame, text="デフォルトにリセット", command=self.reset_settings)
        self.reset_button.pack(pady=5)

        # 設定一覧のリストボックス
        self.listbox = tk.Listbox(self.frame, width=50, height=15)
        self.listbox.pack(pady=10)

        self.load_config()

    def load_config(self):
        self.listbox.delete(0, tk.END)
        for key, value in self.config.data.items():
            self.listbox.insert(tk.END, f"{key}: {value}")

    def add_setting(self):
        key = simpledialog.askstring("キー", "新しいキーを入力:")
        if not key:
            return
        value = simpledialog.askstring("値", f"キー '{key}' の値を入力:")
        if value is not None:
            self.config.set(key, value)
            self.load_config()
            messagebox.showinfo("情報", f"設定を追加しました: {key} = {value}")

    def delete_setting(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("警告", "削除する設定を選択してください")
            return
        item = self.listbox.get(selected[0])
        key = item.split(":")[0]
        self.config.delete(key)
        self.load_config()
        messagebox.showinfo("情報", f"設定を削除しました: {key}")

    def reset_settings(self):
        confirm = messagebox.askyesno("確認", "デフォルト設定にリセットしますか？")
        if confirm:
            self.config.reset_to_defaults()
            self.load_config()
            messagebox.showinfo("情報", "デフォルト設定にリセットしました")


if __name__ == "__main__":
    config = ConfigManager("config.json", default_config={"theme": "light", "notifications": True}, key=DEFAULT_KEY)
    root = tk.Tk()
    app = ConfigGUI(root, config)
    root.mainloop()
