
import os
import base64

from fastapi import FastAPI, UploadFile, File, HTTPException
from openai import OpenAI

app = FastAPI(
    title="DRISHTI API",
    description="AI Accessibility Assistant",
    version="1.1"
)


@app.get("/")
def home():
    return {
        "message": "DRISHTI backend is running!",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/vision/describe")
def describe_image(file: UploadFile = File(...)):

    allowed_types = [
        "image/jpeg",
        "image/png",
        "image/webp",
        "image/gif"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Please upload a supported image."
        )

    image_data = file.file.read()

    if not image_data:
        raise HTTPException(
            status_code=400,
            detail="The uploaded image is empty."
        )

    if len(image_data) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail="Image must be smaller than 10 MB."
        )

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=503,
            detail="AI service is not configured yet."
        )

    encoded_image = base64.b64encode(
        image_data
    ).decode("utf-8")

    try:
        client = OpenAI(api_key=api_key)

        response = client.responses.create(
            model="gpt-5.5",
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": (
                                "Describe the visible scene clearly "
                                "and concisely for a person who needs "
                                "accessibility assistance. Mention "
                                "important objects and visible text. "
                                "Do not guess uncertain details."
                            )
                        },
                        {
                            "type": "input_image",
                            "image_url": (
                                f"data:{file.content_type};"
                                f"base64,{encoded_image}"
                            )
                        }
                    ]
                }
            ]
        )

        return {
            "status": "success",
            "description": response.output_text
        }

    except Exception:
        raise HTTPException(
            status_code=502,
            detail="AI image analysis failed."
        )

@app.post("/vision/test")
async def test_image_upload(file: UploadFile = File(...)):
    allowed_types = [
        "image/jpeg",
        "image/png",
        "image/webp"
    ]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Please upload a JPG, PNG, or WEBP image."
        )

    image_data = await file.read()

    if not image_data:
        raise HTTPException(
            status_code=400,
            detail="The uploaded image is empty."
        )

    if len(image_data) > 10 * 1024 * 1024:
        raise HTTPException(
            status_code=413,
            detail="Image must be smaller than 10 MB."
        )

    return {
        "status": "success",
        "filename": file.filename,
        "content_type": file.content_type,
        "size_bytes": len(image_data),
        "description": (
            "DRISHTI test mode: Image uploaded successfully. "
            "AI image analysis is not connected yet."
        )
    }
