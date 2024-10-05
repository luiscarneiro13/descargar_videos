import uuid
import os
import time
from fastapi import HTTPException
from yt_dlp import YoutubeDL

def download_video_mp4(url: str):
    unique_filename = str(uuid.uuid4())
    ydl_opts = {
        'format': 'bestvideo[height<=480]+worstaudio[height<=480]/bestvideo[height<=360]+worstaudio[height<=360]/bestvideo[height<=240]+worstaudio[height<=240]',  # Descargar en 480p, 360p o 240p con audio de menor calidad
        'outtmpl': f'/tmp/{unique_filename}.mp4',  # Asegurarse de que la plantilla de salida termine en .mp4
        'merge_output_format': 'mp4'  # Forzar la salida en MP4
    }
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_title = info_dict.get('title', None)
            file_path = f"/tmp/{unique_filename}.mp4"
            
            # Verifica si el archivo existe y espera si es necesario
            for _ in range(10):
                if os.path.exists(file_path):
                    break
                time.sleep(1)
            
            if not os.path.exists(file_path):
                raise HTTPException(status_code=500, detail="Archivo no encontrado")
            
            file_size = os.path.getsize(file_path)  # Obtener el tamaño del archivo
            
            return {"name": video_title, "path": file_path, "size": file_size}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


