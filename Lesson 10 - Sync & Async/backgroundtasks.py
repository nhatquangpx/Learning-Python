# Dùng BackgroundTasks để chạy tác vụ nền, ví dụ:
# - Gửi email sau khi đăng ký
# - Ghi log truy cập
# - Resize ảnh upload
# - Clean dữ liệu không cần thiết
# - Gửi thông báo nội bộ

from fastapi import BackgroundTasks, FastAPI

app = FastAPI()
def write_log(user_id: int):
    with open("log.txt", "a") as f:
        f.write(f"User {user_id} logged in\n")
        
@app.post("/login")
def login_user(user_id: int, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_log, user_id)
    return {"message": "User logged in successfully"}

# Hàm write_log sẽ được chạy sau khi API trả response
# Người dùng không cần chờ đợi tác vụ log này hoàn thành
# Tưởng tượng như bạn đặt nhắc việc cho trợ lý, còn bạn có thể làm việc khác trong khi trợ lý xử lý công việc đó.   

# Ví du: Gửi email sau khi đăng ký
def send_email(to: str):
    with open ("emails.log", "a") as f:
        f.write(f"Send email to {to}\n")
        
@app.post("/send-email/")
async def send_mail(to: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, to)
    return {"message": "Email will be sent in the background"}

# Tác vụ nền = chạy độc lập, không ảnh hưởng tốc độ phản hồi của API
