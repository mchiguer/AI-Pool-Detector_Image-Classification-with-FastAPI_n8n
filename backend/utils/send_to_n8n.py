import requests
from backend.config import N8N_WEBHOOK_URL, N8N_USERNAME, N8N_PASSWORD

def send_to_n8n(image_bytes, filename="image.jpg", mime_type="image/jpeg"):
    files = {"file": (filename, image_bytes, mime_type)}
    response = requests.post(
        N8N_WEBHOOK_URL,
        files=files,
        auth=(N8N_USERNAME, N8N_PASSWORD)
    )
    response.raise_for_status()
    return response.json()

