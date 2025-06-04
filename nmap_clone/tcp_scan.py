import socket
from typing import Tuple

from .banner import grab_banner


Result = Tuple[str, int, bool, str]

def tcp_connect(ip: str, port: int, *, timeout: float = 1.0, banner: bool = False) -> Result:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        banner_data = ""
        if banner:
            banner_data = grab_banner(s, timeout)
        status = True
    except Exception:
        status = False
        banner_data = ""
    finally:
        s.close()
    return ip, port, status, banner_data
