import os
import json
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)

        if parsed.path not in ("/api/request", "/request"):
            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"ok": False, "error": "Not found"}).encode())
            return

        tw = params.get("tw", [""])[0].strip()
        hostp = params.get("hostp", [""])[0].strip()

        if not tw or not hostp:
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({
                "ok": False,
                "error": "Both tw and hostp parameters are required."
            }).encode())
            return

        token = "8766757312:AAFdK3GWoREUF2ag29bnM0aoCHSTFa_cHVA"
        owner_id = "8295436090"

        notified = False
        if token and owner_id:
            message = (
                "🔔 New Request Received\n\n"
                f"tw: {tw}\n"
                f"hostp: {hostp}"
            )
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            data = urllib.parse.urlencode({
                "chat_id": owner_id,
                "text": message
            }).encode()
            req = urllib.request.Request(url, data=data, method="POST")
            try:
                with urllib.request.urlopen(req, timeout=8) as response:
                    notified = response.status == 200
            except Exception as e:
                notified = False

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(json.dumps({
            "ok": True,
            "notification_sent": notified,
            "message": "Request received."
        }).encode())

    def log_message(self, fmt, *args):
        return
