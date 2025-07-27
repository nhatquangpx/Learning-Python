# Viết test cho background task
from fastapi.testclient import TestClient
from app.main import app
from time import time

client = TestClient(app)

def test_login_background_task():
    response = client.post("/login/?user_id=123")
    assert response.status_code == 200
    assert response.json()["msg"] == "Login accepted"
    
# Vì khi gọi hàm sẽ trả ngay response sau đó mới chạy tác vụ nền, vậy nên chỉ test được response chứ không thể kiểm tra tác vụ nền đã hoàn thành hay chưa.
# Nếu muốn kiểm tra file được ghi, có 2 cách:
# 1. Kiểm tra "sau vài giây" xem file đã được ghi hay chưa (không ổn định, phụ thuộc vào thời gian thực thi).
def test_login_logs_written():
    client.post("/login/?user_id=999")
    time.sleep(0.1)  # Chờ task hoàn thành (nguy hiểm nếu không đồng bộ)
    
    with open("log.txt", "r") as f:
        logs = f.read()
        assert "999" in logs
# -> Không nên dùng cách này nếu test nhiều lần, vì dễ gay flaky test (lúc test được lúc không)
# 2. Sử dụng thư viện monkeypatch hoặc mock để kiểm tra
# ví dụ: thay thế write_log bằng hàm mock trong test để kiểm soát nội dung
from fastapi.testclient import TestClient
from app.main import app

def test_background_with_mock(monkeypatch):
    called = {}

    def fake_write_log(user_id):
        called["log"] = user_id

    monkeypatch.setattr("app.main.write_log", fake_write_log)

    client = TestClient(app)
    response = client.post("/login/?user_id=777")

    assert response.status_code == 200
    assert called["log"] == 777
    
# -> monkeypatch sẽ thay thế hàm write_log bằng fake_write_log, giúp ta kiểm tra xem hàm có được gọi với đúng tham số hay không mà không cần phụ thuộc vào file log thực tế.