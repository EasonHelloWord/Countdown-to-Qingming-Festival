import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# 计算清明节假期的时间范围
start_time = datetime(2024, 4, 3, 16, 0)
end_time = datetime(2024, 4, 7)

def format_timedelta(td):
    hours, remainder = divmod(td.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{td.days * 24 + hours}小时{minutes}分钟"

def update_progress():
    now = datetime.now()
    remaining_time = end_time - now
    total_seconds = (end_time - start_time).total_seconds()
    elapsed_seconds = (now - start_time).total_seconds()
    progress_percent = elapsed_seconds / total_seconds * 100
    progress_bar["value"] = progress_percent
    progress_label.config(text=f"假期剩余时间: {format_timedelta(remaining_time)}, 完成进度: {progress_percent:.2f}%")

    if now < end_time:
        root.after(60000, update_progress)  # 每分钟更新一次进度条

root = tk.Tk()
root.title("清明假期倒计时")
root.iconbitmap('./res/function.ico')

progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.pack(pady=10)
progress_label = tk.Label(root, text="")
progress_label.pack()

update_progress()

root.mainloop()
