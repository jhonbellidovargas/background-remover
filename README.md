# background-remover
Image BG Remover
Instala Python y pip:

Descarga e instala la última versión de Python desde python.org.
Asegúrate de que Python esté en el PATH de Windows y verifica la instalación con:
bash
Copy code
python --version
Configura un entorno virtual:

Abre una terminal y crea un directorio para el proyecto:
bash
Copy code
mkdir background_removal_api
cd background_removal_api
Crea un entorno virtual:
bash
Copy code
python -m venv env
Activa el entorno virtual:
bash
Copy code
.\env\Scripts\activate
Instala las dependencias:

Instala FastAPI, Uvicorn (para correr la API), y RemBG para la eliminación de fondos:
bash
Copy code
pip install fastapi uvicorn rembg
Configura RemBG en Windows:

Para Windows, RemBG requiere de ffmpeg y torch. Instálalos con:
bash
Copy code
pip install torch torchvision torchaudio
