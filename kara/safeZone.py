import time
import sys
from colorama import init, Fore, Back, Style

# Khởi tạo colorama cho Windows
init(autoreset=True)

def type_text(text, delay=0.1, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Xuống dòng sau khi in xong

def type_multiple_lines(lines, delay, line_pause):
    for i, (text, color) in enumerate(lines):
        type_text(text, delay, color)
        if i < len(lines) - 1:  # Không dừng sau dòng cuối
            time.sleep(line_pause)

def main():
    # Danh sách các dòng chữ với màu sắc
    messages = [
        ("Sự thật là, vẫn chưa ai yêu anh nhiều hơn em từng làm", Fore.GREEN),
        ("Và cũng sẽ chẳng có ai có thể khiến cho nước mắt của em rơi từng hàng", Fore.BLUE),
        ("Và kể cả về sau này, có trong tay biển bạc và rừng vàng", Fore.RED),
        ("Cũng không bao giờ có thể thay thế người con gái bên cạnh lúc bần hàn", Fore.MAGENTA),
        ("Nhưng mà đây không phải lời thú tội", Fore.GREEN),
        ("Anh không tới để nhận án", Fore.BLUE),
        ("Anh đã có hình phạt, đó là nhìn em bên người xứng đáng", Fore.RED),
        ("Ta vẫn yêu và quan tâm nhau, chỉ là dùng một cách tiếp cận khác", Fore.MAGENTA),
        ("Tiếc là ta gặp nhau vào những năm tháng anh vẫn chưa sẵn sàng", Fore.GREEN),]    
    # In các dòng chữ với màu sắc
    type_multiple_lines(messages, delay=0.08, line_pause=0.5)
    
if __name__ == "__main__":
    main()