
from fastapi import FastAPI
from pydantic import BaseModel
from urllib.parse import urlparse, parse_qs

app = FastAPI(title="ClipRush AI")

class VideoRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return {
        "message": "ClipRush AI Backend is running!"
    }

@app.post("/analyse")
def analyse_video(video: VideoRequest):
    url = video.url.strip()
    parsed = urlparse(url)

    if parsed.hostname not in [
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
        "youtu.be"
    ]:
        return {"error": "Invalid YouTube link"}

    video_id = (
        parse_qs(parsed.query).get("v", [None])[0]
        or parsed.path.strip("/")
    )

    if not video_id:
        return {"error": "Video ID missing"}

    return {
        "status": "received",
        "video_id": video_id,
        "message": "YouTube link received successfully"
    }
