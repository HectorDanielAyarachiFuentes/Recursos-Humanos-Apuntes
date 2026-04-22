import subprocess
import json
import sys

cmd = [r"C:\Users\Ramoncito\AppData\Local\Programs\Python\Python311\Scripts\notebooklm-mcp.exe", "--config", "notebooklm-config.json", "server"]
try:
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=sys.stderr, text=True)
except Exception as e:
    print(f"Failed: {e}")
    sys.exit(1)

def send_request(req):
    process.stdin.write(json.dumps(req) + "\n")
    process.stdin.flush()
    return json.loads(process.stdout.readline())

init_req = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "test", "version": "1.0"}
    }
}
send_request(init_req)
process.stdin.write(json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}) + "\n")
process.stdin.flush()

tools_req = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list"
}
tools = send_request(tools_req)

ask_req = {
    "jsonrpc": "2.0",
    "id": 3,
    "method": "tools/call",
    "params": {
        "name": "ask_notebook",
        "arguments": {
            "query": "Lista todos los autores y sus respectivos temas mencionados específicamente en la Unidad 1 del programa de estudio. Sé detallado."
        }
    }
}
ans = send_request(ask_req)
print(ans)
process.terminate()
