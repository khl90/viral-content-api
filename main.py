from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os
from typing import Optional

app = FastAPI(title="Viral Content Generator API")

# Configuration OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

class ContentRequest(BaseModel):
    niche: str
    topic: str
    platform: str
    language: Optional[str] = "french"

@app.get("/")
def root():
    return {"message": "Viral Content Generator API - Ready!", "status": "online"}

@app.post("/generate")
async def generate_content(request: ContentRequest):
    try:
        # Prompt optimisé pour contenu viral
        prompt = f"""
Créer un post {request.platform} viral pour la niche {request.niche} sur le sujet {request.topic}.

RÈGLES:
- Commence par un hook puissant qui arrête le scroll
- Utilise la psychologie de l'engagement (curiosité, controverse, émotion)
- Structure en paragraphes courts (max 2 lignes)
- Inclus des éléments de storytelling si approprié
- Optimisé pour {request.platform}

STRUCTURE DEMANDÉE:
1. Hook (1ère ligne qui accroche)
2. Contenu principal (valeur, insight, histoire)
3. Call-to-action engageant
4. Hashtags pertinents (max 10)

Niche: {request.niche}
Sujet: {request.topic}
Plateforme: {request.platform}

Génère un contenu qui maximise l'engagement et les partages.
"""

        # Appel OpenAI
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Tu es un expert en création de contenu viral sur les réseaux sociaux. Tu maîtrises parfaitement les mécaniques d'engagement et de viralité."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.8
        )
        
        generated_content = response.choices[0].message.content
        
        return {
            "content": generated_content,
            "status": "success",
            "niche": request.niche,
            "topic": request.topic,
            "platform": request.platform
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur génération: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
