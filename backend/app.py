from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from backend.utils.send_to_n8n import send_to_n8n
import json
import re

app = FastAPI()

# Allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/classify")
async def classify_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    try:
        result = send_to_n8n(image_bytes, filename=file.filename, mime_type=file.content_type)

        # n8n / GPT result is a list with nested text
        if isinstance(result, list) and "content" in result[0]:
            text = result[0]["content"][0]["text"]
            # Extract JSON from triple backticks or raw text
            json_str = re.search(r'\{.*\}', text, re.DOTALL).group(0)
            parsed = json.loads(json_str)
            # Convert confidence to float
            parsed["confidence"] = float(parsed["confidence"])
            return parsed

        return {"error": "Unexpected response structure", "raw": result}

    except Exception as e:
        return {"error": str(e)}
