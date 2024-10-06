from fastapi import FastAPI, HTTPException, Query
import functions.download_video_mp4 as mp4
import functions.download_video_mp3 as mp3
import functions.download_video_wav as wav

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/download")
def download_video(url: str, formats: str = Query(..., description="Formatos de archivo, separados por comas (e.g., 'mp4,mp3')")):
    formats_list = formats.split(',')
    files_info = []
    
    for fmt in formats_list:
        if fmt == 'mp4':
            files_info.append(mp4.download_video_mp4(url))
        elif fmt == 'mp3':
            files_info.append(mp3.download_video_mp3(url))
        elif fmt == 'wav':
            files_info.append(wav.download_video_wav(url))
        else:
            raise HTTPException(status_code=400, detail=f"Formato no soportado: {fmt}")
    
    return files_info
