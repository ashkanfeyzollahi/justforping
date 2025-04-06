"""
Test a JustForPing server instance by pinging
"""

from multiprocessing import Process

from ping3 import ping

from justforping import make_and_serve_justforping_server


def test_justforping_server() -> None:
    """
    A simple test written for testing a JustForPing server
    """

    server_process = Process(
        target=make_and_serve_justforping_server,
        args=("127.0.0.1", 8000)
    )

    server_process.start()

    assert ping("127.0.0.1") is not None

    server_process.terminate()
    server_process.join()

