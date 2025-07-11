import socket

def scan(target):
    try:
        sock = socket.socket()
        sock.settimeout(3)
        sock.connect((target, 22))
        banner = sock.recv(1024).decode(errors='ignore')
        sock.close()
        if "Cowrie" in banner or "SSH-2.0-OpenSSH_5.1p1" in banner:
            return {"status": "honeypot-suspected", "banner": banner}
        return {"status": "clean", "banner": banner}
    except Exception as e:
        return {"status": "error", "error": str(e)}