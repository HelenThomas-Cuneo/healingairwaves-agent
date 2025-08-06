# HealingAirwaves Agent (FastAPI + Frontend + Gmail + Upload + Mobile UI)
# A ritual media generator and healing content delivery agent

from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from datetime import datetime
import random
import smtplib
from email.message import EmailMessage
from gtts import gTTS
import os

app = FastAPI(title="HealingAirwaves Agent")

# requirements.txt
# fastapi
# uvicorn
# gtts
# email-validator
# python-dotenv

# README.md
"""
# HealingAirwaves Agent

This is a FastAPI-powered ritual media generator for the HealingAirwaves movement.

## Features:
- Generate poetic healing scripts
- Voiceover audio creation in 5 languages
- Email blessings to subscribers via Gmail SMTP
- Upload elder stories or healing visuals
- Mobile-first UI for TikTok creators

## Topics (GitHub Tags):
fastapi, healing, gpt, voiceover, peace-media, ayurveda, ritual, openai-agent, substack, canva, global-healing

## To run locally:
```
pip install -r requirements.txt
uvicorn healingairwaves_agent:app --reload
```
Visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to use the interface.

## Gmail Note:
Use an app-specific password and .env file to store your credentials securely.

## Deploy to Render/Replit for public access.
"""

class ThemeRequest(BaseModel):
    theme: str = ""
    language: str = "en"
    email: str = ""

class Output(BaseModel):
    content: str

# --- Core Content Generator ---

def generate_voiceover_script(theme: str, lang: str = "en") -> str:
    opening = {
        "en": ["The sun rises across the skin of the Earth", "You are alive. You are loved.", "Place your hand on your chest — breathe in the morning like it’s medicine."],
        "es": ["El sol se eleva sobre la piel de la Tierra", "Estás vivo. Eres amado.", "Pon tu mano en el pecho — respira la mañana como si fuera medicina."],
        "hi": ["सूरज पृथ्वी की त्वचा पर उगता है", "तुम जीवित हो। तुम प्रिय हो।", "अपना हाथ अपने सीने पर रखें — सुबह को दवा की तरह सांस लें।"],
        "fr": ["Le soleil se lève sur la peau de la Terre", "Tu es vivant. Tu es aimé.", "Pose ta main sur ta poitrine — respire le matin comme un remède."],
        "ar": ["تشرق الشمس على جلد الأرض", "أنت على قيد الحياة. أنت محبوب.", "ضع يدك على صدرك — تنفس الصباح كأنه دواء."]
    }
    blessings = {
        "en": ["May you remember who you are.", "May your breath carry the wisdom of your ancestors.", "May today feel like a ritual of healing."],
        "es": ["Que recuerdes quién eres.", "Que tu respiración lleve la sabiduría de tus antepasados.", "Que hoy se sienta como un ritual de sanación."],
        "hi": ["आपको याद रहे कि आप कौन हैं।", "आपकी साँसें आपके पूर्वजों की बुद्धि को वहन करें।", "आज का दिन उपचार की एक रस्म की तरह महसूस हो।"],
        "fr": ["Puisses-tu te souvenir de qui tu es.", "Que ton souffle porte la sagesse de tes ancêtres.", "Que cette journée soit un rituel de guérison."],
        "ar": ["عسى أن تتذكر من أنت.", "ليحمل نفسك حكمة أجدادك.", "ليكن هذا اليوم طقسًا للشفاء."]
    }
    return f"[Voiceover Script]\n\n{random.choice(opening[lang])}\n\n{theme}\n\n{random.choice(blessings[lang])}"

# (Rest of the file continues unchanged...)
