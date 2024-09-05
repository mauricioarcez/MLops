import os
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World!"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Usa el puerto definido en PORT o el 8000 por defecto
    uvicorn.run(app, host="0.0.0.0", port=port)
