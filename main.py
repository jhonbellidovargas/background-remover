# main.py
from fastapi import FastAPI, File, UploadFile, HTTPException, Depends
from rembg import remove
from config import API_KEY
from models import ImageResponse, usage_control
import base64

app = FastAPI()

# Dependencia para verificar la API Key y las consultas diarias
def check_api_key(api_key: str):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    if not usage_control.increment_requests():
        raise HTTPException(status_code=429, detail="Request limit reached")
    return True

@app.post("/remove-background", response_model=ImageResponse)
async def remove_background(api_key: str = Depends(check_api_key), file: UploadFile = File(...)):
    try:
        # Leer la imagen y eliminar el fondo
        input_image = await file.read()
        output_image = remove(input_image)

        # Codificar la imagen de salida a base64 para enviarla como respuesta
        output_image_base64 = base64.b64encode(output_image).decode("utf-8")

        return ImageResponse(message="Background removed successfully", image_data=output_image_base64)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")
