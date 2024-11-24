import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from config_manager import ConfigManager
from cryptography.fernet import Fernet

DEFAULT_KEY = Fernet.generate_key()  # 必要に応じて保存

class ConfigGUI:
    def __init__(self, root, config):
        self.root = root
        self.config = config

        self.root.title("JSON設定ファイルマネージャー")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        # タイトルラベル
        title_label = tk.Label(
            self.root,
            text="JSON 設定ファイルマネージャー",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=10)

        # 現在の設定表示
        self.config_display = tk.Text(self.root, width=70, height=15, state="disabled", bg="#ffffff", fg="#333333")
        self.config_display.pack(pady=10)
        self.load_config()

        # ボタンフレーム
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        # ボタン配置
        add_button = ttk.Button(button_frame, text="設定を追加", command=self.add_setting)
        add_button.grid(row=0, column=0, padx=5, pady=5)

        delete_button = ttk.Button(button_frame, text="設定を削除", command=self.delete_setting)
        delete_button.grid(row=0, column=1, padx=5, pady=5)

        reset_button = ttk.Button(button_frame, text="デフォルトにリセット", command=self.reset_settings)
        reset_button.grid(row=0, column=2, padx=5, pady=5)

        refresh_button = ttk.Button(button_frame, text="設定をリロード", command=self.load_config)
        refresh_button.grid(row=0, column=3, padx=5, pady=5)

    def load_config(self):
        """現在の設定を表示"""
        self.config_display.config(state="normal")
        self.config_display.delete("1.0", tk.END)
        for key, value in self.config.data.items():
            self.config_display.insert(tk.END, f"{key}: {value}\n")
        self.config_display.config(state="disabled")

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

    def delete_setting(self):
        """設定を削除"""
        key = simpledialog.askstring("削除", "削除するキーを入力:")
        if key and key in self.config.data:
            self.config.delete(key)
            self.load_config()
            messagebox.showinfo("情報", f"設定を削除しました: {key}")
        else:
            messagebox.showwarning("警告", "指定されたキーが見つかりません")

    def reset_settings(self):
        """デフォルト設定にリセット"""
        confirm = messagebox.askyesno("確認", "デフォルト設定にリセットしますか？")
        if confirm:
            self.config.reset_to_defaults()
            self.load_config()
            messagebox.showinfo("情報", "デフォルト設定にリセットしました")


if __name__ == "__main__":
    # デフォルト設定を指定
    default_config = {"theme": "light", "notifications": True}
    config = ConfigManager("config.json", default_config=default_config, key=DEFAULT_KEY)

    root = tk.Tk()
    app = ConfigGUI(root, config)
    root.mainloop()
