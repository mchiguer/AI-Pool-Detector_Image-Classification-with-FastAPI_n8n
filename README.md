#  AI Pool Detector — Image Classification with FastAPI & n8n 

This project is a full-stack AI web application that detects the presence of a swimming pool in an image.  
It combines a **FastAPI backend**, a **simple web frontend**, and an **n8n workflow** that connects to **OpenAI GPT-4o (Vision)** for intelligent image analysis.

---
![Texte alternatif](Screen from n8n.png)
##  Overview

The system lets users upload a photo of a house or building.  
The image is sent to the backend (FastAPI), which forwards it to n8n.  
n8n calls **GPT-4o** to analyze the visual content and returns a JSON prediction like:

```json
{
  "category": "villa with swimming pool",
  "confidence": 0.93
}
