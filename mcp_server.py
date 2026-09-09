import sys
import json
from client import ChaitinBriggsRegisterAllocator

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "allocate":
        alloc = ChaitinBriggsRegisterAllocator(params.get("k", 4))
        for u, v in params.get("edges", []):
            alloc.add_interference(u, v)
        return alloc.allocate()
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == '__main__':
    main()
