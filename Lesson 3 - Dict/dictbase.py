# Từ điển cho phép lưu dữ liệu dưới dạng cặp key:value
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2025
}

print(thisdict)

# Muốn in cụ thể một mục trong từ điển
print(thisdict["brand"])

# Có thứ tự => Có chỉ mục và tham chiếu bằng chỉ mục

# Có thể thay đổi CRUD

# Không được phép trùng lặp => không có hai mục cùng key
# Nếu như trùng lặp thì sẽ ghi đè lên các giá trị hiện có trước đó
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

# Độ dài từ điển
print(len(thisdict))

# Kiểu dữ liệu: Các giá trị trong mục từ điển có thể thuộc bất kì kiểu dữ liệu nào

# Kiểu của từ điển là dict
print(type(thisdict))

# Cũng có thể sử dụng hàm dict() để tạo từ điển, khi đó dùng ngoặc đơn chứ không phải ngoặc nhọn, chỉ mục không còn sử dụng ngoăc kép
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

