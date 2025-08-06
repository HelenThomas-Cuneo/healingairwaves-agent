from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import random

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def form_ui():
    return """
    <html>
        <head><title>HealingAirwaves Agent</title></head>
        <body>
            <h2>🎙️ HealingAirwaves Generator</h2>
            <form action="/generate" method="post">
                <input name="theme" type="text" placeholder="Enter a healing theme"><br>
                <select name="language">
                    <option value="en">English</option>
                    <option value="es">Spanish</option>
                    <option value="hi">Hindi</option>
                    <option value="fr">French</option>
                    <option value="ar">Arabic</option>
                </select><br>
                <input name="email" type="email" placeholder="Send to email (optional)"><br>
                <button name="type" value="voiceover">Generate Voiceover</button>
            </form>
        </body>
    </html>
    """

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
    return f"[Voiceover Script]\\n\\n{random.choice(opening[lang])}\\n\\n{theme}\\n\\n{random.choice(blessings[lang])}"

@app.post("/generate", response_class=HTMLResponse)
def generate_from_form(theme: str = Form(...), language: str = Form("en"), email: str = Form("")):
    content = generate_voiceover_script(theme, language)
    return f"""
    <html><body>
    <h3>Generated Output:</h3>
    <pre>{content}</pre>
    <a href='/'>⬅ Back</a>
    </body></html>
    """
