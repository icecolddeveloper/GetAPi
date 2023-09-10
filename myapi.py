from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()

@app.get('/api')

def api():
    slack_name = request.Get.get("slack_name")
    today = datetime.now()
    current_day = today.strftime('%A')
    utc_time = datetime.now(pytz.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    track = request.Get.get("track")
    github_file_url = ""
    github_repo_url = ""
