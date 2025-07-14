# Truy cập các mục trong từ điển bằng cách tham chiếu đến khóa
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
# Ngoài ra còn có thể sử dụng phương thức get()
y = thisdict.get("model")
print(x)
print(y)

# Lấy khóa, sử dụng phương thức keys()
z = thisdict.keys()
print(z)
# Thêm một mục mới vào từ điển, khi đó sẽ tự động cập nhật khóa
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x)              
car["color"] = "white"
print(x) 

# Lấy giá trị, sử dụng phương thức values()
a = car.values()
print(a)
# Thêm một giá trị mới vào từ điển, khi đó sẽ tự động cập nhật giá trị
car["part_color"] = "red"
print(a)

# Lấy cặp khóa-giá trị, sử dụng phương thức items()
b = car.items()
print(b)
# Thêm một cặp khóa-giá trị mới vào từ điển, khi đó sẽ tự động cập nhật cặp khóa-giá trị

# Kiểm tra khóa có trong từ điển hay không, sử dụng toán tử in
if "model" in car:
    print("Model is present in the car dictionary.")