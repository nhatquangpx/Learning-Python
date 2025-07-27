# Ứng dụng thực tế: Resize ảnh (giả lập)
import time
from fastapi import FastAPI, BackgroundTasks

app = FastAPI()

def resize_image(filename: str):
    time.sleep(3) # Giả lập thời gian xử lý ảnh
    print(f"Finished resizing {filename}")
    
@app.post("/upload")
async def upload_image(filename: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(resize_image, filename)
    return {"status": "Image upload in progress", "filename": filename}

# Tác vụ nặng như xử lý ảnh, nên chuyển sang Celery