import uuid
import os
import time
from fastapi import HTTPException
from yt_dlp import YoutubeDL


def download_video_mp3(url: str):
    unique_filename = str(uuid.uuid4())
    ydl_opts = {
        'format': 'bestaudio/best',  # Asegura que sea la mejor calidad de audio disponible
        'outtmpl': f'/tmp/{unique_filename}',  # No añadas la extensión aquí
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }]
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', None)
            # Asegúrate de que la extensión se añade aquí
            file_path = f"/tmp/{unique_filename}.mp3"

            # Verifica si el archivo existe y espera si es necesario
            for _ in range(10):
                if os.path.exists(file_path):
                    break
                time.sleep(1)

            if not os.path.exists(file_path):
                raise HTTPException(
                    status_code=500, detail="Archivo no encontrado")

            file_size = os.path.getsize(file_path) / (1024 * 1024) # Get the file size

            return {"name": video_title, "path": file_path, "size": file_size}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
