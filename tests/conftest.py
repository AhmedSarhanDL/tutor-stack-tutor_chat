import socket
import threading
import time

import pytest
import requests
import uvicorn

from tutor_stack_chat.main import app


def find_free_port():
    """Find a free port to use for testing"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


@pytest.fixture
def client():
    # Find a free port
    port = find_free_port()

    # Start the server in a separate thread
    def run_server():
        uvicorn.run(app, host="127.0.0.1", port=port, log_level="error")

    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    # Wait for server to start
    time.sleep(1)

    # Create a simple requests client
    test_client = requests.Session()
    test_client.base_url = f"http://127.0.0.1:{port}"

    yield test_client

    # Cleanup
    test_client.close()
