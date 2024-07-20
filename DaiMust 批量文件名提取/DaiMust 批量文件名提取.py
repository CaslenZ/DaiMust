import os
import tkinter as tk
from tkinter import messagebox

def main():
    folder_path = folder_path_entry.get()

    if not os.path.isdir(folder_path):
        messagebox.showerror("错误", "输入的路径不是一个有效的文件夹。")
        return

    file_names = [file for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

    if numbering_var.get():  # 如果勾选了编号
        if show_extension_var.get():  # 如果勾选了显示后缀名
            for index, file in enumerate(file_names, start=1):
                result_text.insert(tk.END, f"{index}. {file}\n")
        else:  # 如果未勾选显示后缀名
            for index, file in enumerate(file_names, start=1):
                file_name_without_extension = os.path.splitext(file)[0]
                result_text.insert(tk.END, f"{index}. {file_name_without_extension}\n")
    else:  # 如果未勾选编号
        if show_extension_var.get():  # 如果勾选了显示后缀名
            for file in file_names:
                result_text.insert(tk.END, f"{file}\n")
        else:  # 如果未勾选显示后缀名
            for file in file_names:
                file_name_without_extension = os.path.splitext(file)[0]
                result_text.insert(tk.END, f"{file_name_without_extension}\n")

# 创建主窗口
root = tk.Tk()
root.title("DaiMust 批量文件名提取")

# 输入框
folder_path_label = tk.Label(root, text="文件夹路径:")
folder_path_label.pack()
folder_path_entry = tk.Entry(root)
folder_path_entry.pack()

# 编号选择复选框
numbering_var = tk.BooleanVar()
numbering_checkbox = tk.Checkbutton(root, text="显示编号", variable=numbering_var)
numbering_checkbox.pack()

# 后缀名选择复选框
show_extension_var = tk.BooleanVar()
show_extension_checkbox = tk.Checkbutton(root, text="显示后缀名", variable=show_extension_var)
show_extension_checkbox.pack()

# 提取按钮
extract_button = tk.Button(root, text="提取文件名", command=main)
extract_button.pack()

# 结果显示区域
result_text = tk.Text(root)
result_text.pack()

# 主事件循环
root.mainloop()