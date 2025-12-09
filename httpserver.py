
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

PORT = 56789

class cacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # 加上禁止快取的標頭
        # self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        # self.send_header('Pragma', 'no-cache')
        # self.send_header('Expires', '0')
        self.send_header('Cache-Control', 'max-age=3600')  # 快取 1 小時
        super().end_headers()

Handler = cacheHandler

with ThreadingHTTPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n收到 Ctrl+C，正在安全關閉伺服器...")
        httpd.server_close()
        print("伺服器已關閉")

