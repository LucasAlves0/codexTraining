import socket


def grab_banner(s: socket.socket, timeout: float = 1.0) -> str:
    s.settimeout(timeout)
    try:
        data = s.recv(1024)
        return data.decode(errors="ignore").strip()
    except Exception:
        return ""
