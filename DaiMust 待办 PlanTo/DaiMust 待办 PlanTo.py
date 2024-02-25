import tkinter as tk
from tkinter import messagebox


class TodoManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DaiMust 待办 PlanTo")
        self.geometry("400x500")

        # 创建列表框来显示待办事项
        self.todo_list = tk.Listbox(self, width=50, height=10, selectmode='browse')
        self.todo_list.pack(pady=10)

        # 为列表框添加双击事件绑定
        self.todo_list.bind("<Double-1>", self.on_double_click)

        # 创建输入框用于添加新待办事项
        self.new_todo_entry = tk.Entry(self, width=50)
        self.new_todo_entry.pack(pady=5)

        # 创建按钮用于添加待办事项
        self.add_todo_button = tk.Button(self, text="添加待办事项", command=self.add_todo)
        self.add_todo_button.pack(pady=5)

        # 创建按钮用于删除选定的待办事项
        self.delete_todo_button = tk.Button(self, text="删除待办事项", command=self.delete_todo)
        self.delete_todo_button.pack(pady=5)

        # 创建按钮用于导入待办事项
        self.import_todos_button = tk.Button(self, text="导入待办事项", command=self.load_todos)
        self.import_todos_button.pack(pady=5)

        # 创建按钮用于清空待办事项
        self.clear_todos_button = tk.Button(self, text="清空待办事项", command=self.clear_todos)
        self.clear_todos_button.pack(pady=5)

        # 创建按钮用于显示关于信息
        self.about_button = tk.Button(self, text="关于", command=self.show_about)
        self.about_button.pack(pady=5)

        # 在程序启动时加载待办事项
        self.load_todos()

        # 在程序关闭时保存待办事项
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        label = tk.Label(self, text="双击某一待办事项可将其标注为已完成。")
        label.pack(pady=20)

    def add_todo(self):
        # 获取输入框中的文本
        todo_text = self.new_todo_entry.get()
        if todo_text:
            # 将文本添加到列表框中
            self.todo_list.insert(tk.END, todo_text)
            # 清空输入框
            self.new_todo_entry.delete(0, tk.END)

    def delete_todo(self):
        # 获取选定的待办事项
        selected_index = self.todo_list.curselection()
        if selected_index:
            # 从列表框中删除选定的待办事项
            self.todo_list.delete(selected_index[0])

    def show_about(self):
        # 显示关于信息的弹窗
        messagebox.showinfo("关于", "DaiMust 待办\n技术支持：caslen08@outlook.com")

    def save_todos(self):
        with open("PlanToList.dmdata", "w", encoding="utf-8") as file:
            for index in range(self.todo_list.size()):
                todo_text = self.todo_list.get(index)
                file.write(todo_text + "\n")

    def load_todos(self):
        try:
            with open("PlanToList.dmdata", "r", encoding="utf-8") as file:
                for line in file:
                    todo_text = line.strip()
                    if todo_text:
                        self.todo_list.insert(tk.END, todo_text)
        except FileNotFoundError:
            pass

    def on_close(self):
        self.save_todos()
        self.destroy()

    def on_double_click(self, event):
        # 获取双击的待办事项
        selected_index = self.todo_list.curselection()
        if selected_index:
            # 获取待办事项的文本
            todo_text = self.todo_list.get(selected_index[0])
            # 在文本后添加"（已完成✔）"
            new_todo_text = todo_text + "（已完成✔）"
            # 更新列表框中的文本
            self.todo_list.delete(selected_index[0])
            self.todo_list.insert(selected_index[0], new_todo_text)

    def clear_todos(self):
        self.todo_list.delete(0, tk.END)

app = TodoManager()

# 进入事件循环
app.mainloop()