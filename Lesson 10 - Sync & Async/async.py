# Quy tắc:
# Sử dụng async def khi gọi hàm bất đồng bộ như:
# await asyncio.sleep()
# await db.fetch()
# await aiohttp.get()

# Ví dụ: Chờ xử lý 2 giây mới trả về
from fastapi import FastAPI
import asyncio

app =FastAPI()

@app.get("/delayed")
async def delayed_response():
    await asyncio.sleep(2)
    return {"message": "This response was delayed by 2 seconds"}

# Trong thời gian đó, server vẫn xử lý req khác
