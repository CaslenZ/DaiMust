import psutil
import tkinter as tk
from tkinter import ttk
import threading

# 标志变量，用于跟踪窗口是否应该保持在最上方
always_top = False


def toggle_topmost():
    global always_top
    always_top = not always_top
    root.attributes('-topmost', always_top)
    topmost_button.config(text="Toggle Topmost" if always_top else "Restore Default")


def update_info():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        cpu_label.config(text=f"CPU: {cpu_usage}%")
        memory_label.config(text=f"Memory: {memory_usage}%")
        disk_label.config(text=f"Disk: {disk_usage}%")

        root.update()

    # 创建主窗口


root = tk.Tk()
root.title("DaiMust SysLive")


root.geometry("300x300")


style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12))


cpu_label = ttk.Label(root, text="CPU: 0%", style='TLabel')
cpu_label.pack(side=tk.TOP, fill=tk.X, pady=10, expand=True)


memory_label = ttk.Label(root, text="Memory: 0%", style='TLabel')
memory_label.pack(side=tk.TOP, fill=tk.X, pady=10, expand=True)


disk_label = ttk.Label(root, text="Disk: 0%", style='TLabel')
disk_label.pack(side=tk.TOP, fill=tk.X, pady=10, expand=True)


topmost_button = ttk.Button(root, text="Toggle Topmost", command=toggle_topmost)
topmost_button.pack(side=tk.BOTTOM, fill=tk.X, pady=10)


threading.Thread(target=update_info, daemon=True).start()


root.mainloop()