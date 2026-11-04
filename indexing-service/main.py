from fastapi import FastAPI

# Création de notre application FastAPI
app = FastAPI()

# Première route : page d'accueil
@app.get("/")
def home():
    return {"message": "Indexing Service is running"}

# Deuxième route : vérifier l'état du service
@app.get("/health")
def health():
    return {"status": "OK"}