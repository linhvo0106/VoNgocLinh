import time
import sys
from colorama import init, Fore, Back, Style

# Khởi tạo colorama cho Windows
init(autoreset=True)

def type_text(text, delay=0.1, color=Fore.WHITE):
    """
    In từng ký tự của dòng chữ với độ trễ và màu sắc
    
    Args:
        text (str): Dòng chữ cần in
        delay (float): Thời gian trễ giữa các ký tự (giây)
        color (str): Màu chữ từ colorama.Fore
    """
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Xuống dòng sau khi in xong

def type_multiple_lines(lines, delay=0.05, line_pause=1.0):
    """
    In nhiều dòng chữ với màu sắc khác nhau
    
    Args:
        lines (list): Danh sách các tuple (text, color)
        delay (float): Thời gian trễ giữa các ký tự
        line_pause (float): Thời gian dừng giữa các dòng
    """
    for i, (text, color) in enumerate(lines):
        print(f"{Fore.YELLOW}[Dòng {i+1}]{Style.RESET_ALL}")
        type_text(text, delay, color)
        if i < len(lines) - 1:  # Không dừng sau dòng cuối
            time.sleep(line_pause)
        print()  # Dòng trống giữa các dòng

def main():
    # Danh sách các dòng chữ với màu sắc
    messages = [
        ("Xin chào! Đây là dòng đầu tiên.", Fore.GREEN),
        ("Dòng thứ hai có màu xanh dương.", Fore.BLUE),
        ("Dòng thứ ba có màu đỏ.", Fore.RED),
        ("Dòng cuối cùng có màu tím.", Fore.MAGENTA),
    ]
    
    print(f"{Fore.CYAN}=== CHƯƠNG TRÌNH IN CHỮ TỪNG DÒNG ==={Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Bắt đầu hiển thị...{Style.RESET_ALL}")
    time.sleep(1)
    
    # In các dòng chữ với màu sắc
    type_multiple_lines(messages, delay=0.08, line_pause=0.5)
    
    print(f"{Style.BRIGHT}{Fore.GREEN}✓ Hoàn thành!{Style.RESET_ALL}")

if __name__ == "__main__":
    main()