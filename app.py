from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi

app = FastAPI()

@app.get("/get-transcript/")
async def get_transcript(id_video: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(id_video, languages=['en'])
        return {"transcript": transcript}
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Error fetching transcript: {e}")
