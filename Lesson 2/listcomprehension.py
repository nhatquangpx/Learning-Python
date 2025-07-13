# List Comprehension cung cấp cú pháp ngắn hơn giúp tạo danh sách mới dựa trên danh sách hiện có

# Cú pháp
# newlist = [expression for item in iterable if condition == true]

# Ví dụ
fruits = ["apple", "banana", "orange", "cherry"]
newlist =[]
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# Khi đó ta có thể rút gọn bằng cú pháp sau:
newlist = [x for x in fruits if "a" in x]
print(newlist)

# Phàn điều kiện có thể lược bỏ, khi đó lấy mọi giá trị trong fruits
newlist = [x for x in fruits]
print(newlist)

# Đối tượng lặp lại có thể là bất cứ đối tượng nào (iterable)
newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Biểu thức là kết quả thu được (expression)
newlist = [x.upper() for x in fruits]               # Viết hoa toàn bộ kết quả thu được
print(newlist)
# Biểu thức cũng có thể chứa điều kiện như một cách để thao tác kết quả 
newlist = [x if x != "banana" else "orange" for x in fruits]            #Trả lại sản phẩm nếu không phải là chuối, nếu là chuối thì trả lại sản phẩm cam
print(newlist)