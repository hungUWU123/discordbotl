import subprocess
import time

# Khởi chạy Bot 1
p1 = subprocess.Popen(['python', 'MyCreation1.py'])

# Khởi chạy Bot 2
p2 = subprocess.Popen(['python', 'MyCreation2.py'])

# Giữ cho chương trình chính không bị thoát
while True:
    # Kiểm tra nếu tiến trình bị sập thì có thể log ra hoặc khởi động lại ở đây
    time.sleep(60)