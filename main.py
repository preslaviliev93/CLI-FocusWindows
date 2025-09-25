from datetime import datetime
import win32gui
import win32process
import psutil
from time import sleep


class WindowsFocus:

    def __init__(self) -> None:
        self.measuring_interval = 5
        self.statistics = {}


    def get_window_hwnd(self)-> int:
        window_identifier = win32gui.GetForegroundWindow()
        return window_identifier

    def get_window_title(self, hwnd):
        return win32gui.GetWindowText(hwnd)

    def get_pid(self, hwnd):
        _, pid = win32process.GetWindowThreadProcessId(hwnd)
        return pid

    def get_proc_name(self,pid_num):
        return psutil.Process(pid_num).name()

    def get_foreground_info(self):
        hwnd_main = self.get_window_hwnd()
        window_title = self.get_window_title(hwnd_main)
        pid = self.get_pid(hwnd_main)
        proc_name = self.get_proc_name(pid)
        return proc_name, window_title

    def populate_information(self, delta_time, proc_name, window_title):
        if proc_name not in self.statistics:
            self.statistics[proc_name] = {}

        if window_title not in self.statistics[proc_name]:
            self.statistics[proc_name][window_title] = 0

        self.statistics[proc_name][window_title] += delta_time

        return self.statistics

    def format_time(self, seconds: float) -> str:
        total = int(round(seconds))
        h, remaining = divmod(total, 3600)
        m, s = divmod(remaining, 60)
        return f"{h:02d}:{m:02d}:{s:02d}"

    def print_statistics_report(self) -> None:
        total_times_per_process = {
            proc: sum(windows_times.values())
            for proc, windows_times in self.statistics.items()
        }

        for proc, total in sorted(total_times_per_process.items(),
                                  key=lambda kv: kv[1], reverse=True):
            print(f"========= {proc} (Total time: {self.format_time(total)}) =========")
            for title, secs in sorted(self.statistics[proc].items(),
                                      key=lambda kv: kv[1], reverse=True):
                print(f"{title} -> {self.format_time(secs)}")
            print()

    def main(self):
        print(f'Tracking ... Press CTRL+C to exit ...')
        try:
            while True:
                proc_name, window_title = self.get_foreground_info()
                time_now = datetime.now()
                sleep(self.measuring_interval)
                after_sleep = (datetime.now() - time_now).total_seconds()
                self.populate_information(after_sleep, proc_name, window_title)
        except KeyboardInterrupt:
            print('\nProgram exited by user')
            self.print_statistics_report()
            sleep(3)
            exit(1)




if __name__ == '__main__':
    window = WindowsFocus()
    window.main()