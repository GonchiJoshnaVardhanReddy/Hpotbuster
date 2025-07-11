import json

def load_targets(args):
    if args.input:
        with open(args.input, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    elif args.target:
        return [args.target]
    return []

def log_result(target, result, outfile):
    entry = {"target": target, "result": result}
    with open(outfile, 'a') as f:
        f.write(json.dumps(entry) + "\n")