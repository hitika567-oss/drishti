# drishti
AI-powered visual assistant for visually impaired individuals, built using Ollama, Gemma 4 E2B, Python FastAPI and native Android. Understand surroundings, read text and interact through voice.
DRISHTI AI 👁️

Beyond Vision. Towards Independence.

An AI-powered visual assistant designed to help visually impaired individuals understand and interact with their surroundings through artificial intelligence, computer vision and voice technology.

<p align="center">

Powered by Ollama + Gemma 4 E2B

Built with Kotlin • Python • FastAPI • Android

</p>

---

🌟 About the Project

Drishti is an AI-powered assistive technology application designed to make everyday visual information more accessible to people with visual impairments.

Using a smartphone camera and a multimodal AI model, Drishti aims to identify objects, describe surroundings, read printed text and answer questions about the user's environment.

The application combines local AI inference, computer vision and voice-based interaction to provide an accessible and privacy-focused experience.

Our vision: Make visual information more accessible, affordable and understandable through AI.

🎯 Problem Statement

Visually impaired individuals face several everyday challenges:

- Identifying objects and understanding their surroundings.
- Reading printed documents, notices and signboards.
- Locating everyday objects.
- Accessing visual information independently.
- Interacting with digital information through conventional interfaces.

Many assistive solutions require specialised hardware or expensive services.

Drishti aims to address these challenges through an affordable smartphone-based AI assistant.

💡 Our Proposed Solution

Drishti uses the smartphone camera to capture visual information and sends it to a locally hosted AI backend powered by Ollama and Gemma 4 E2B.

The AI analyses the captured image and generates a natural-language response. The Android application can then present the information through text and speech.

The system is designed around accessibility, local AI processing and natural voice interaction.

✨ Key Features

1. AI Scene Understanding

- Analyses camera images.
- Describes the user's surroundings.
- Identifies visible objects.
- Explains approximate object positions.

2. Intelligent Text Reader

- Reads printed notices and documents.
- Extracts text from images.
- Converts extracted text into spoken responses.

3. AI Object Finder

- Helps users locate requested objects.
- Identifies visible objects in camera images.
- Provides approximate positional information.

4. Voice-Based Interaction

- Accepts natural-language questions.
- Supports hands-free interaction.
- Provides spoken AI responses.

5. Multilingual Accessibility

- Designed for English and Hindi interaction.
- Planned support for additional Indian regional languages.

6. Conversational Visual Assistant

- Answers follow-up questions about a captured scene.
- Maintains temporary scene context.
- Provides simple and understandable responses.

7. Safety Awareness

- Identifies potentially hazardous objects in visible scenes.
- Provides supplementary visual warnings.
- Designed with uncertainty handling and safety limitations.

«Note: Features marked as planned or in development should not be considered completed functionality. Drishti is not a replacement for a white cane, guide dog or established mobility aids.»

🛠️ Technology Stack

Component| Technology
Mobile application| Native Android
Programming language| Kotlin
UI framework| Jetpack Compose
Camera integration| CameraX
AI model| Gemma 4 E2B
AI runtime| Ollama
Backend| Python
API framework| FastAPI
Image processing| Pillow / OpenCV
OCR| Google ML Kit Text Recognition
Speech input| Android SpeechRecognizer
Speech output| Android TextToSpeech
Networking| OkHttp / Retrofit

🧠 AI Architecture

Drishti follows a modular architecture in which the Android application communicates with a locally hosted Python backend.

System Workflow

1. User captures an image using the Android application.
2. The image is sent to the FastAPI backend.
3. The backend processes the image.
4. Ollama forwards the image and prompt to Gemma 4 E2B.
5. Gemma analyses the image and generates a response.
6. FastAPI returns the response to the Android application.
7. The application displays or speaks the generated information.

Architecture Diagram

flowchart TD
    A[User] --> B[Android Application]
    B --> C[CameraX]
    B --> D[Voice Input]
    C --> E[Image Capture]
    E --> F[FastAPI Backend]
    D --> F
    F --> G[Ollama Runtime]
    G --> H[Gemma 4 E2B]
    H --> I[AI Response]
    I --> F
    F --> J[Android Application]
    J --> K[Text Display]
    J --> L[Text To Speech]

Deployment Architecture

Current development approach:

- Android application runs on a physical smartphone.
- FastAPI runs on a laptop.
- Ollama runs Gemma locally on the laptop.
- Both devices communicate over a local Wi-Fi network.

This allows local AI inference without relying on a third-party cloud AI API after the model has been downloaded.

📂 Project Structure

Drishti-AI/
│
├── android/
│   └── DrishtiApp/
│       └── app/
│           └── src/main/
│               ├── java/com/drishti/app/
│               ├── res/
│               └── AndroidManifest.xml
│
├── backend/
│   ├── main.py
│   ├── gemma.py
│   ├── requirements.txt
│   └── services/
│
├── assets/
│   ├── screenshots/
│   ├── demo/
│   └── test-images/
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_DOCUMENTATION.md
│   └── INSTALLATION.md
│
├── .gitignore
├── LICENSE
└── README.md

⚙️ Installation and Setup

Prerequisites

Before starting, make sure you have:

- Windows 10/11, Linux or macOS.
- Python 3.11 or newer.
- Android Studio.
- Android SDK.
- Ollama.
- NVIDIA GPU (recommended for accelerated inference).
- Android smartphone running Android 14 or newer.

Step 1: Clone the Repository

git clone https://github.com/hitika567-oss/drishti

cd Drishti-AI

Step 2: Install Ollama

Download Ollama:

"https://ollama.com/download" (https://ollama.com/download)

Step 3: Download Gemma 4 E2B

ollama pull gemma4:e2b

Run the model:

ollama run gemma4:e2b

Step 4: Configure Python Backend

Navigate to the backend folder:

cd backend

Create a virtual environment:

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Step 5: Start the Backend

uvicorn main:app --host 0.0.0.0 --port 8000 --reload

Step 6: Run the Android Application

1. Open the "android/DrishtiApp" folder in Android Studio.
2. Allow Gradle to synchronise.
3. Connect an Android smartphone using USB debugging.
4. Configure the backend IP address in the Android application.
5. Make sure both devices are connected to the same local network.
6. Run the application.

Request parameters:

Parameter| Type| Description
image| File| Uploaded JPEG, PNG or WebP image
language| String| Desired response language

🔐 Privacy and Security

Drishti is designed around privacy-first AI processing.

- AI inference runs locally through Ollama.
- Images are transmitted to the user's local backend.
- No third-party cloud AI API is required for the core image-description workflow.
- User images should not be retained unnecessarily.
- Future production versions will include stronger authentication and secure network communication.

Speech recognition and other operating-system services may have separate network or privacy requirements depending on their implementation.

♿ Accessibility Goals

Drishti aims to follow accessibility-first design principles.

- Large interactive buttons.
- High-contrast interface.
- TalkBack compatibility.
- Voice-first navigation.
- Spoken feedback.
- Simple language.
- Multilingual interaction.
- Clear feedback when the AI cannot identify something.

👥 Team Members

Hitika Dhiman- hitika567-oss| UI/UX Integration and testing 
Harshita- harshitaydv7654-hub| Android Development
Sanskriti- sanskritisahu04-dot| AI and Backend Development
Ruhani- ruhanighai | AI and Backend Development 

🧪 Testing

Testing will cover:

- Indoor and outdoor scene recognition.
- Object identification.
- Printed text extraction.
- English and Hindi responses.
- Camera performance.
- Backend connectivity.
- Response latency.
- AI uncertainty and incorrect predictions.
- Accessibility and TalkBack usability.

Drishti is an assistive AI prototype.

AI-generated descriptions may be inaccurate or incomplete. Camera images alone cannot reliably determine exact distances, motion or collision risks.

Drishti must not be used as a substitute for mobility aids, professional guidance or established safety systems.

Users should verify important information independently.

🤝 Contributing

Contributions, ideas and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test your implementation.
5. Submit a pull request.

📌 Future Vision

Our long-term goal is to evolve Drishti into a reliable, affordable and accessible visual assistant that works directly on compatible smartphones.

We aim to explore on-device AI, better object localisation, multilingual voice interaction and more comprehensive accessibility features.

<p align="center">

DRISHTI AI

Beyond Vision. Towards Independence.

Made with ❤️ for accessibility and innovation.

</p>
