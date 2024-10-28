
# Background Removal API

Este proyecto es una API que permite quitar el fondo de imágenes utilizando inteligencia artificial. Está construida con FastAPI y utiliza la librería RemBG para el procesamiento de imágenes.

## Características

- Elimina el fondo de imágenes en formatos populares.
- Autenticación mediante una clave de API.
- Límite de 200 consultas diarias por clave de API.
- Respuesta con la imagen procesada en formato base64.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **FastAPI**: Framework para construir APIs rápidas y eficientes.
- **RemBG**: Herramienta para la eliminación de fondos en imágenes.
- **Uvicorn**: Servidor ASGI para ejecutar la API.

## Requisitos Previos

- Python 3.8 o superior.
- pip para la instalación de paquetes.

## Instalación

1. Clona este repositorio o descarga el código fuente.
2. Navega al directorio del proyecto.
3. Crea un entorno virtual:
   ```bash
   python -m venv env
   ```
4. Activa el entorno virtual:
   - En Windows:
     ```bash
     .\env\Scripts ctivate
     ```
5. Instala las dependencias necesarias:
   ```bash
   pip install fastapi uvicorn rembg torch torchvision torchaudio
   ```

## Uso

1. Inicia el servidor de la API:
   ```bash
   uvicorn main:app --reload
   ```
2. Accede a la documentación de la API en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).
3. Realiza solicitudes POST al endpoint `/remove-background` con los siguientes parámetros:
   - **api_key**: Tu clave de API.
   - **file**: La imagen de la que deseas quitar el fondo (en formato `.png`, `.jpg`, etc.).

### Ejemplo de Solicitud

```bash
curl -X POST "http://127.0.0.1:8000/remove-background?api_key=your-secret-key" -F "file=@path_to_image.jpg"
```

## Límite de Consultas

La API está configurada para permitir un máximo de 200 consultas diarias por clave de API. Si se alcanza este límite, se retornará un error 429.

## Restablecimiento del Contador de Consultas

Un script se debe ejecutar diariamente para restablecer el contador de consultas. Se recomienda usar el Programador de Tareas de Windows para esto.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request para discutir mejoras o cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo LICENSE.
