import tkinter as tk
from tkinter import messagebox, simpledialog
from config_manager import ConfigManager

class ConfigGUI:
    def __init__(self, root, config):
        self.root = root
        self.config = config

        self.root.title("JSON設定ファイルマネージャー")
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.refresh_button = tk.Button(self.frame, text="設定をリロード", command=self.load_config)
        self.refresh_button.pack(pady=5)

        self.add_button = tk.Button(self.frame, text="設定を追加", command=self.add_setting)
        self.add_button.pack(pady=5)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.pack(pady=10)

        self.load_config()

    def load_config(self):
        """現在の設定をリストボックスに表示"""
        self.listbox.delete(0, tk.END)
        for key, value in self.config.data.items():
            self.listbox.insert(tk.END, f"{key}: {value}")

    def add_setting(self):
        """新しい設定を追加"""
        key = simpledialog.askstring("キー", "新しいキーを入力:")
        if not key:
            return
        value = simpledialog.askstring("値", f"キー '{key}' の値を入力:")
        if value is not None:
            self.config.set(key, value)
            self.load_config()
            messagebox.showinfo("情報", f"設定を追加しました: {key} = {value}")

if __name__ == "__main__":
    config = ConfigManager("config.json")
    root = tk.Tk()
    app = ConfigGUI(root, config)
    root.mainloop()
