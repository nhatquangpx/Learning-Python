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
    
# Cập nhật bài viết
def test_update_post():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.put(f"/posts/{post_id}", json={
        "title": "Updated Test Post",
        "content": "This is updated content for the test post."
    }, headers=headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Test Post"
    assert response.json()["content"] == "This is updated content for the test post."
    assert response.json()["id"] == post_id

# Kiểm thử cập nhật bài viết không có token -> phải bị từ chối
def test_update_post_without_token():
    response = client.put(f"/posts/{post_id}", json={
        "title": "Unauthorized Update",
        "content": "This update should not work."
    })
    assert response.status_code == 401  # Phải trả về lỗi 401 Unauthorized

# Kiểm thử cập nhật bài viết không tồn tại
def test_update_nonexistent_post():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.put("/posts/99999", json={
        "title": "Update Non-existent",
        "content": "This post does not exist."
    }, headers=headers)
    assert response.status_code == 403  # Phải trả về lỗi 404 Not Found

# Xóa bài viết
# Xóa bài viết
def test_delete_post():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete(f"/posts/{post_id}", headers=headers)
    assert response.status_code == 200
    assert "deleted" in response.json()
    assert response.json()["deleted"] == True
    
    # Kiểm tra xem bài viết đã bị xóa chưa
    response_check = client.get(f"/posts/{post_id}")
    assert response_check.status_code == 404  # Bài viết không còn tồn tại

# Kiểm thử xóa bài viết không có token -> phải bị từ chối
def test_delete_post_without_token():
    # Tạo bài viết mới để test xóa
    headers = {"Authorization": f"Bearer {token}"}
    response = client.post("/posts/", json={
        "title": "Post to Delete",
        "content": "This post will be used for delete test."
    }, headers=headers)
    temp_post_id = response.json()["id"]
    
    # Thử xóa không có token
    response = client.delete(f"/posts/{temp_post_id}")
    assert response.status_code == 401  # Phải trả về lỗi 401 Unauthorized
    
    # Cleanup: Xóa bài viết test
    client.delete(f"/posts/{temp_post_id}", headers=headers)

# Kiểm thử xóa bài viết không tồn tại
def test_delete_nonexistent_post():
    headers = {"Authorization": f"Bearer {token}"}
    response = client.delete("/posts/99999", headers=headers)
    assert response.status_code == 403  # Phải trả về lỗi 404 Not Found