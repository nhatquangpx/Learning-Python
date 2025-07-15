# Thay đổi giá trị trong tuple không được hỗ trợ trực tiếp
# Khi đó chuyển đổi tuple thành danh sách, thay đổi giá trị, rồi chuyển đổi lại thành tuple
thistuple = ("apple", "banana", "cherry")
thistuple_list = list(thistuple)  # Chuyển đổi tuple thành danh sách
thistuple_list[1] = "orange"  # Thay đổi giá trị tại chỉ mục 1
thistuple = tuple(thistuple_list)  # Chuyển đổi lại thành tuple
print(thistuple)  # In ra ('apple', 'orange', 'cherry')

# Thêm mục vào tuple không được hỗ trợ trực tiếp
# Tương tự, chuyển đổi tuple thành danh sách, thêm mục, rồi chuyển đổi lại thành tuple
thistuple = ("apple", "banana", "cherry")
thistuple_list = list(thistuple)  # Chuyển đổi tuple thành danh sách
thistuple_list.append("date")  # Thêm mục mới
thistuple = tuple(thistuple_list)  # Chuyển đổi lại thành tuple
print(thistuple)  # In ra ('apple', 'banana', 'cherry', 'date')

# Có thể thêm tuple khác vào tuple hiện tại
# Nếu thêm một tuple chỉ có một mục, cần phải nhớ có đấu phẩy sau mục đó
thistuple2 = ("date", "elderberry")
thistuple += thistuple2  # Nối hai tuple
print(thistuple)  # In ra ('apple', 'banana', 'cherry', 'date', 'date', 'elderberry')

# Xóa mục trong tuple không được hỗ trợ trực tiếp
# Tương tự, chuyển đổi tuple thành danh sách, xóa mục, rồi chuyển đổi lại thành tuple
thistuple = ("apple", "banana", "cherry")
thistuple_list = list(thistuple)  # Chuyển đổi tuple thành danh sách
thistuple_list.remove("banana")  # Xóa mục 'banana'
thistuple = tuple(thistuple_list)  # Chuyển đổi lại thành tuple
print(thistuple)  # In ra ('apple', 'cherry')

# Có thể xóa toàn bộ tuple bằng từ khóa del
del thistuple  # Xóa toàn bộ tuple
# print(thistuple)  # Nếu in ra sẽ báo lỗi vì thistuple đã bị xóa