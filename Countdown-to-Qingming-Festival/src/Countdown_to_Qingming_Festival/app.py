import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from datetime import datetime, timedelta
import threading

# 计算清明节假期的时间范围
start_time = datetime(2024, 4, 3, 16, 0)
end_time = datetime(2024, 4, 7)

def format_timedelta(td):
    hours, remainder = divmod(td.seconds, 3600)
    minutes, _ = divmod(remainder, 60)
    return f"{td.days * 24 + hours}小时{minutes}分钟"


class 清明倒计时(toga.App):
    def update_progress(self):
        now = datetime.now()
        remaining_time = end_time - now
        total_seconds = (end_time - start_time).total_seconds()
        elapsed_seconds = (now - start_time).total_seconds()
        progress_percent = elapsed_seconds / total_seconds * 100
        self.progress_bar.value = progress_percent
        self.progress_label.text = f"假期剩余时间: {format_timedelta(remaining_time)}, 完成进度: {progress_percent:.2f}%"

        if now < end_time:
            threading.Timer(60, self.update_progress).start()  # 每分钟更新一次进度条

    def startup(self):
        """Construct and show the Toga application."""
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=20, alignment='center'))
        # Create a box for progress bar
        progress_bar_box = toga.Box(style=Pack(alignment='center', padding_bottom=10))
        self.progress_bar = toga.ProgressBar(max=100, style=Pack(flex=1, background_color='#EFEFEF'))  # 设置进度条背景颜色
        progress_bar_box.add(self.progress_bar)
        main_box.add(progress_bar_box)

        # Create a box for label
        progress_label_box = toga.Box(style=Pack(alignment='center'))
        self.progress_label = toga.Label("", style=Pack(text_align='center'))
        progress_label_box.add(self.progress_label)
        main_box.add(progress_label_box)

        # Update progress
        self.update_progress()

        # Create the main window and show it
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()


def main():
    return 清明倒计时()
