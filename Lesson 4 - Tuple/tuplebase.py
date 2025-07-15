# Tuple dùng để lưu trữ các giá trị không thay đổi
# Tương tự như danh sách nhưng không thể thay đổi giá trị sau khi đã tạo
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Các mục trong tuple có thể truy cập bằng chỉ mục
# Các mục được sắp xếp theo thứ tự, không thể thay đổi và cho phép các giá trị trùng lặp
print(thistuple[1])  # In ra 'banana'

# Độ dài tuple dùng hàm len()
print(len(thistuple))  

# Tạo tuple với một mục, bắt buộc phải có dấu phẩy
# Nếu không có dấu phẩy, Python sẽ coi nó là một chuỗi
thistuple2 = ("apple",)

# Các mục trong tuple có thể thuộc bất kỳ kiểu dữ liệu nào
thistuple3 = ("apple", 1, True, 3.14)

# Kiểu của tuple là 'tuple'
print(type(thistuple))  # In ra <class 'tuple'>

# Có thể sử dụng hàm tuple() để chuyển đổi các kiểu dữ liệu khác thành tuple
thistuple4 = tuple(["apple", "banana", "cherry"])  # Chuyển đổi danh sách thành tuple
print(thistuple4)  # In ra ('apple', 'banana', 'cherry')