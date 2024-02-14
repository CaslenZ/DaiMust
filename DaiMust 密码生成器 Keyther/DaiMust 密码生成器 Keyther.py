import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Tesret Studio 用有此程序的编译著作权和管理权，请勿擅自将此程序进行改编或进行任何商业或盈利行为。
# 若对程序的合法性或相关权益存在质疑或反驳，请将合法证明和叙述发送到 caslen08@icloud.com，我们会积极跟进。

def generate_password(length, include_uppercase, include_numbers, include_symbols):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def generate_button_clicked():
    length = int(length_entry.get())
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()

    password = generate_password(length, include_uppercase, include_numbers, include_symbols)

    # 将密码复制到剪贴板
    pyperclip.copy(password)

    messagebox.showinfo("DaiMust 密码生成器 Keyther", f'''DaiMust Keyther为您生成的密码为：
    {password}
    密码已自动复制到剪贴板。''')

def show_dialog():
    messagebox.showinfo("关于", '''
    感谢使用由Tesret Studio提供的DaiMust系列软件 Keyther。
    有任何问题，欢迎联系技术支持caslen08@icloud.com。
    Tesret Studio拥有此软件著作权。''')

# 创建主窗口
window = tk.Tk()
window.title("DaiMust 密码生成器 Keyther")

# 密码长度标签和输入框
length_label = tk.Label(window, text="密码长度:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.pack()

# 选项复选框
uppercase_var = tk.IntVar()
uppercase_checkbox = tk.Checkbutton(window, text="包含大写字母", variable=uppercase_var)
uppercase_checkbox.pack()

numbers_var = tk.IntVar()
numbers_checkbox = tk.Checkbutton(window, text="包含数字", variable=numbers_var)
numbers_checkbox.pack()

symbols_var = tk.IntVar()
symbols_checkbox = tk.Checkbutton(window, text="包含符号", variable=symbols_var)
symbols_checkbox.pack()

# 生成按钮
generate_button = tk.Button(window, text="生成", command=generate_button_clicked)
generate_button.pack()

dialog_button = tk.Button(window, text="关于此软件", command=show_dialog)
dialog_button.pack()

label = tk.Label(window, text='''生成的密码默认含有小写字母，以上选项均为可选。
Tesret Studio DaiMust Keyther''')
label.pack()

# 运行主循环
window.mainloop()
