"""
desktop_bridge.py - AI 手勢全域簡報控制器 (免安裝第三方套件，純 Python 標準庫 + Windows API)
功能：接收瀏覽器端的手勢觸發訊號，自動向 Windows 系統發送真實鍵盤事件（Right Arrow / Left Arrow），
使任何 PowerPoint、Canva、Adobe PDF 或全螢幕投影片皆可實現隔空手勢翻頁。
"""
import http.server
import socketserver
import ctypes
import time
import sys

PORT = 8765

# Windows Virtual Key Codes
VK_LEFT = 0x25    # Left arrow key (上一頁)
VK_RIGHT = 0x27   # Right arrow key (下一頁)
VK_SPACE = 0x20   # Space key
KEYEVENTF_KEYUP = 0x0002

user32 = ctypes.windll.user32

def press_key(vk_code):
    """模擬真實 Windows 按鍵按下與釋放"""
    user32.keybd_event(vk_code, 0, 0, 0)
    time.sleep(0.05)
    user32.keybd_event(vk_code, 0, KEYEVENTF_KEYUP, 0)

class GestureBridgeHandler(http.server.BaseHTTPRequestHandler):
    def end_headers(self):
        # 允許跨網域請求 (CORS)，使 GitHub Pages 亦能呼叫本機服務
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        path = self.path.split('?')[0].lower()
        if path == '/next':
            press_key(VK_RIGHT)
            print("👉 [手勢觸發] 模擬鍵盤：下一頁 (Right Arrow)")
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"NEXT_OK")
        elif path == '/prev':
            press_key(VK_LEFT)
            print("👈 [手勢觸發] 模擬鍵盤：上一頁 (Left Arrow)")
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"PREV_OK")
        elif path == '/ping':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"PONG_ONLINE")
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # 隱藏一般 HTTP 存取日誌，保持終端畫面乾淨
        return

def main():
    print("=" * 65)
    print("   AI 手勢全域簡報控制器 (PowerPoint / PDF 系統級橋接服務)")
    print("=" * 65)
    print(f"[*] 服務正在監聽端口: http://127.0.0.1:{PORT}")
    print("[*] 運作說明：")
    print("    1. 請保持此視窗開啟。")
    print("    2. 打開您的 PowerPoint、PDF 或任何簡報並進入「全螢幕播放模式」。")
    print("    3. 瀏覽器手勢辨識到 👉 向右 或 👈 向左 時，將自動發送實體按鍵翻頁！")
    print("[*] 按 Ctrl+C 即可停止服務。\n")

    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("127.0.0.1", PORT), GestureBridgeHandler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服務已停止。")
        sys.exit(0)

if __name__ == "__main__":
    main()
