import tkinter as tk
from tkinter import ttk, messagebox
import requests
import hashlib
import random
import webbrowser

import json

app_key = ''

def open_url():
    url = "https://github.com/CaslenZ/DaiMust/tree/main/DaiMust%20%E7%BF%BB%E8%AF%91%E5%B8%88%20Ranxleta"
    webbrowser.open(url)

def save_app_key():
    global app_key
    app_key = key_input.get().strip()  # 获取并去除输入框两边的空白字符
    messagebox.showinfo("保存成功", "KEY已成功保存！")

def translate_text():
    text = text_input.get("1.0", tk.END).strip()

    app_id = '20231028001862484'

    url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'

    salt = str(random.randint(32768, 65536))
    sign = app_id + text + salt + app_key
    sign = hashlib.md5(sign.encode()).hexdigest()

    selected_lang = lang_combo.get()

    if selected_lang == "请选择目标语言":
        translated_output.delete("1.0", tk.END)
        translated_output.insert(tk.END, "请选择目标语言")
    else:
        if selected_lang == "英语":
            to_lang = "en"
        elif selected_lang == "中文":
            to_lang = "zh"
        elif selected_lang == "日语":
            to_lang = "jp"
        elif selected_lang == "韩语":
            to_lang = "kor"
        elif selected_lang == "德语":
            to_lang = "de"
        elif selected_lang == "俄语":
            to_lang = "ru"
        elif selected_lang == "粤语":
            to_lang = "yue"
        elif selected_lang == "繁体中文":
            to_lang = "cht"
        elif selected_lang == "文言文":
            to_lang = "wyw"
        elif selected_lang == "西班牙语":
            to_lang = "spa"
        elif selected_lang == "阿拉伯语":
            to_lang = "ara"
        elif selected_lang == "泰语":
            to_lang = "th"

        params = {
            'q': text,
            'from': 'auto',
            'to': to_lang,
            'appid': app_id,
            'salt': salt,
            'sign': sign
        }

        response = requests.get(url, params=params)
        result = response.json()

        if 'trans_result' in result:
            translated_text = result['trans_result'][0]['dst']
            translated_output.delete("1.0", tk.END)
            translated_output.insert(tk.END, translated_text)
        else:
            translated_output.delete("1.0", tk.END)
            translated_output.insert(tk.END, '''服务器连接错误。
            -请检查KEY是否输入错误。
            -请稍后再试。''')





window = tk.Tk()
window.title("DaiMust 翻译师 Ranxleta")
window.geometry("550x550")
window.resizable(False, False)  # 锁定界面大小

# 添加KEY输入框和保存按钮
key_label = tk.Label(window, text="请输入KEY：")
key_label.pack()  # 添加垂直填充

key_input = tk.Entry(window, width=30)
key_input.pack()

save_button = tk.Button(window, text="保存", command=save_app_key)
save_button.pack(pady=10)

# 添加输入文本框标签
text_label = tk.Label(window, text="请输入要翻译的文本：")
text_label.pack()

text_input = tk.Text(window, height=10, width=50)
text_input.pack(pady=10)

lang_options = ["请选择目标语言", "英语", "中文", "日语", "韩语", "德语", "俄语", "粤语", "繁体中文", "文言文", "西班牙语", "阿拉伯语", "泰语"]
lang_combo = ttk.Combobox(window, values=lang_options, state="readonly")
lang_combo.current(0)  # 设置默认选择项为第一个
lang_combo.pack()

translate_button = tk.Button(window, text="翻译", command=translate_text)
translate_button.pack(pady=10)

# 添加输出文本框标签
translated_label = tk.Label(window, text="翻译结果：")
translated_label.pack()

translated_output = tk.Text(window, height=10, width=50)
translated_output.pack()

about_button = tk.Button(window, text="获取KEY", command=open_url)
about_button.pack()

window.mainloop()
