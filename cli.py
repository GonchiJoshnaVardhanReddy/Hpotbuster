import argparse
from core.detectors import ssh, http, ftp, smb, generic
from utils import load_targets, log_result

protocol_map = {
    'ssh': ssh.scan,
    'http': http.scan,
    'ftp': ftp.scan,
    'smb': smb.scan,
    'auto': generic.scan
}

def main():
    parser = argparse.ArgumentParser(description="hpotbuster - Honeypot Detection Tool")
    parser.add_argument('--target', help='Target IP or URL')
    parser.add_argument('--protocol', choices=protocol_map.keys(), required=True)
    parser.add_argument('--input', help='File with list of targets')
    parser.add_argument('--output', default='results.json', help='Output result file')
    args = parser.parse_args()

    targets = load_targets(args)
    for target in targets:
        result = protocol_map[args.protocol](target)
        log_result(target, result, args.output)

if __name__ == '__main__':
    main()