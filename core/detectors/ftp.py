import socket

def scan(target):
    try:
        sock = socket.socket()
        sock.settimeout(3)
        sock.connect((target, 21))
        banner = sock.recv(1024).decode(errors='ignore')
        sock.close()
        if "HoneyFTP" in banner or "FakeFTP" in banner:
            return {"status": "honeypot-suspected", "banner": banner}
        return {"status": "clean", "banner": banner}
    except Exception as e:
        return {"status": "error", "error": str(e)}