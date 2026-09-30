import http.server
import socketserver
import os
import sys

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == "__main__":
    print(f"==========================================================")
    print(f"   Smart India Hackathon (SIH26032) Mandi Procurement SPA")
    print(f"==========================================================")
    print(f" Serving web app at: http://localhost:{PORT}")
    print(f" Press Ctrl+C to stop the server.")
    print(f"----------------------------------------------------------")
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped gracefully.")
        sys.exit(0)
