import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pygame.mixer
import threading

# 若对程序的合法性或相关权益存在质疑或反驳，请将合法证明和叙述发送到 caslen08@icloud.com，我们会积极跟进。

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DaiMust 音频播放器")
        self.geometry("400x600")

        # 初始化音频播放器
        pygame.mixer.init()

        # 音乐播放列表和当前播放索引
        self.music_files = []
        self.current_index = -1

        # 创建音乐列表控件
        self.music_listbox = tk.Listbox(self, selectmode='single', exportselection=False)
        self.music_listbox.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # 滚动条
        self.scrollbar = tk.Scrollbar(self, command=self.music_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.music_listbox.config(yscrollcommand=self.scrollbar.set)

        # 按钮
        self.controls_frame = tk.Frame(self)
        self.controls_frame.pack(pady=10)

        self.play_button = tk.Button(self.controls_frame, text="播放", command=self.play_music)
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.pause_button = tk.Button(self.controls_frame, text="暂停", command=self.pause_music)
        self.pause_button.pack(side=tk.LEFT, padx=5)

        self.stop_button = tk.Button(self.controls_frame, text="停止", command=self.stop_music)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        self.change_folder_button = tk.Button(self.controls_frame, text="选择音频目录", command=self.change_folder)
        self.change_folder_button.pack(side=tk.LEFT, padx=5)

        self.about_button = tk.Button(self.controls_frame, text="关于", command=self.show_about)
        self.about_button.pack(side=tk.LEFT, padx=5)

        # 音量控制
        self.volume_scale = tk.Scale(self, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_scale.set(10)  # 默认音量为10
        self.volume_scale.pack(pady=10)

        # 播放线程
        self.playing_thread = None

    def play_music(self):
        if len(self.music_files) == 0:
            messagebox.showwarning("警告", "播放列表为空，请添加音频文件！")
            return

        selected_index = self.music_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("警告", "请选择一个音频文件！")
            return

        selected_index = selected_index[0]  # 获取选中的索引（因为curselection()返回一个元组）
        selected_file = self.music_files[selected_index]  # 从音乐文件列表中获取文件路径

        if self.playing_thread and self.playing_thread.is_alive():
            self.stop_music()  # 如果已经在播放，则先停止

        def play_audio():
            pygame.mixer.music.load(selected_file)
            pygame.mixer.music.play()

        self.current_index = selected_index  # 更新当前播放的索引
        self.playing_thread = threading.Thread(target=play_audio)
        self.playing_thread.start()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def stop_music(self):
        if self.playing_thread:
            pygame.mixer.music.stop()
            self.playing_thread.join()  # 等待播放线程结束
            self.playing_thread = None
            self.current_index = -1
            self.music_listbox.selection_clear(0, tk.END)

    def change_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.load_music_files(folder_selected)

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume / 100)

    def show_about(self):
        messagebox.showinfo("关于", '感谢使用DaiMust音频播放器。\nGithub @CaslenZ\n')

    def load_music_files(self, folder_path):
        self.music_files.clear()
        self.music_listbox.delete(0, tk.END)

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith((".mp3", ".wav", ".flac", ".ogg")):
                    self.music_files.append(os.path.join(root, file))

        self.music_files.sort()  # 对文件列表进行排序

        for file in self.music_files:
            self.music_listbox.insert(tk.END, os.path.basename(file))

        if len(self.music_files) > 0:
            self.current_index = 0
            self.music_listbox.selection_set(self.current_index)
        else:
            messagebox.showwarning("警告", "所选文件夹中没有支持的音频文件！")

        # 运行音乐播放器


music_player = MusicPlayer()
music_player.mainloop()
