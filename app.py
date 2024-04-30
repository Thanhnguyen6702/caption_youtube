from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

app = FastAPI()

@app.get("/get-transcript/")
async def get_transcript(id_video: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(id_video, languages=['en'])
        return {"transcript": transcript}
    except TranscriptsDisabled:
        # Video không có phụ đề
        raise HTTPException(status_code=404, detail="Transcripts are disabled for this video.")
    except NoTranscriptFound:
        # Không tìm thấy phụ đề cho video
        raise HTTPException(status_code=404, detail="No transcript found for this video.")
    except VideoUnavailable:
        # Video không tồn tại hoặc không truy cập được
        raise HTTPException(status_code=404, detail="Video is unavailable or restricted.")
    except Exception as e:
        # Xử lý ngoại lệ chung chung
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")

