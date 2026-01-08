import json
import urllib.request
import urllib.error

payload = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "foobar1",
    "confirm_password": "foobar1",
    "login_method": "manual",
    "device_id": "dev",
    "device_name": "web",
    "location": "India",
}

data = json.dumps(payload).encode()
req = urllib.request.Request(
    "http://192.168.1.113:4000/auth/signup",
    data=data,
    headers={"Content-Type": "application/json"},
)

try:
    with urllib.request.urlopen(req) as resp:
        print("status", resp.status)
        print(resp.read().decode())
except urllib.error.HTTPError as exc:
    print("status", exc.code)
    print(exc.read().decode())
except Exception as exc:  # pragma: no cover - debugging helper
    print("error", type(exc).__name__, exc)
