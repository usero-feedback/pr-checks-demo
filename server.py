# Serves a built site like `python3 -m http.server`, and reports its own time per page in a Server-Timing header.
# Usage: python3 server.py PORT DIRECTORY
import sys
import time
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class Handler(SimpleHTTPRequestHandler):
    # Keep-alive, like a real web server.
    protocol_version = "HTTP/1.1"

    def is_page(self):
        path = self.path.split("?")[0]
        return path.endswith("/") or path.endswith(".html")

    def do_GET(self):
        self.started = time.perf_counter()
        super().do_GET()

    def end_headers(self):
        started = getattr(self, "started", None)
        if started is not None and self.is_page():
            self.send_header("Server-Timing", f"total;dur={(time.perf_counter() - started) * 1000:.1f}")
        super().end_headers()

    def log_message(self, format, *args):
        pass


if __name__ == "__main__":
    port, directory = int(sys.argv[1]), sys.argv[2]
    ThreadingHTTPServer(("127.0.0.1", port), partial(Handler, directory=directory)).serve_forever()
