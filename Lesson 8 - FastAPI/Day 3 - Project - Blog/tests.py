from fastapi import testclient
from main import app

client = testclient.TestClient(app)

# Đăng ký người dùng mới
def test_register_user():
    response = client.post("/register", json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code in (200, 400) # 200 nếu đăng ký thành công, 400 nếu tên người dùng đã tồn tại
    
# Đăng nhập người dùng
def test_login_user():
    response = client.post("/token", data={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
    global token # Lưu token để sử dụng trong các test khác
    token = response.json()["access_token"]
    
# Lấy thông tin người dùng hiện tại
def test_read_me():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/me", headers=headers)
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"
    
# Tạo bài viết mới
def test_create_post():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/posts/", json={
        "title": "Test Post",
        "content": "This is a test post content."
    }, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Post"
    global post_id # Lưu ID bài viết để sử dụng trong các test khác
    post_id = response.json()["id"]
    
# Lấy tất cả bài viết
def test_get_all_posts():
    response = client.get("/posts/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  # Kiểm tra xem kết quả là một danh sách

# Lấy bài viết theo ID
def test_get_post():
    response = client.get(f"/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["id"] == post_id
    
# Kiểm thử tạo bài viết không có token -> phải bị từ chối
def test_create_post_without_token():
    response = client.post("/posts/", json={
        "title": "Unauthorized Post",
        "content": "This post should not be created."
    })
    assert response.status_code == 401  # Phải trả về lỗi 401 Unauthorized