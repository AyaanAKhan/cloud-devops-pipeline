"""A minimal Python web application used for the DevOps pipeline example.

When run inside a container, this script starts an HTTP server on port 8080 that returns a
JSON greeting.  In a real project, this could be replaced with a Flask/FastAPI service or any
other application.
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        message = {"message": "Hello from the DevOps pipeline sample!"}
        self.wfile.write(json.dumps(message).encode())


def run_server(port: int = 8080) -> None:
    server = HTTPServer(("0.0.0.0", port), HelloHandler)
    print(f"Server started on port {port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    run_server()