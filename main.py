from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

class ContentRequest(BaseModel):
    niche: str
    topic: str
    platform: str

@app.get("/")
def root():
    return {"message": "API fonctionnelle!", "status": "OK"}

@app.post("/generate")
def generate_content(request: ContentRequest):
    # Version simple pour tester d'abord
    content = f"""🔥 STOP ! Voici le secret pour dominer {request.niche} sur {request.platform}...

Dans le monde du {request.topic}, 90% des gens font cette erreur fatale :

❌ Ils créent du contenu générique
❌ Ils ignorent leur audience 
❌ Ils vendent avant de servir

Voici ma méthode en 3 étapes :

1️⃣ Identifiez LA douleur précise de votre audience
2️⃣ Créez une solution unique et actionnable  
3️⃣ Racontez une histoire personnelle

Résultat : +300% d'engagement garanti !

Essayez et dites-moi en commentaires ! 👇

#{request.niche} #{request.topic} #{request.platform} #business #entrepreneur"""

    return {
        "content": content,
        "status": "success",
        "niche": request.niche,
        "topic": request.topic,
        "platform": request.platform
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
