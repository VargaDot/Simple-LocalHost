import subprocess

def start_http_server():
    try:
        subprocess.run(["python", "-m", "http.server"])
    except KeyboardInterrupt:
        print("HTTP server stopped.")

if __name__ == "__main__":
    start_http_server()