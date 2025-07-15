# CẬP NHẬT MỘT MỤC TRONG TỪ ĐIỂN
# Thay đổi giá trị của một mục trong từ điển bằng cách sử dụng khóa của mục đó
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}   
thisdict["year"] = 2020
print(thisdict["year"])

# Cập nhật từ điển bằng cách sử dụng phương thức update()
# Có thể thêm hoặc thay đổi nhiều mục cùng một lúc
# Đối số phải là một từ điển khác hoặc một chuỗi các cặp khóa-giá trị
thisdict.update({"year": 2021})
print(thisdict["year"])
thisdict.update({"color": "red"})
print(thisdict)
#--------------------------------------------

# THÊM MỤC VÀO TỪ ĐIỂN
# Thêm một mục mới vào từ điển bằng cách sử dụng khóa mới và gán giá trị cho nó
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#--------------------------------------------

# XÓA MỤC TRONG TỪ ĐIỂN
# Xóa một mục khỏi từ điển bằng cách sử dụng khóa của mục đó, sử dunhg phương thức pop()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
# Nếu sử dụng popitem() sẽ xóa mục cuối cùng trong từ điển
thisdict.popitem()
print(thisdict)
# Nếu sử dụng del sẽ xóa mục chỉ định hoặc toàn bộ từ điển nếu không có khóa
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["year"]
print(thisdict)
del thisdict  # Xóa toàn bộ từ điển
print(thisdict)  # Sẽ báo lỗi vì từ điển đã bị xóa

# Sử dụng phương thức clear() để xóa tất cả các mục trong từ điển
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)  # Sẽ in ra một từ điển rỗng {} mà không báo lỗi