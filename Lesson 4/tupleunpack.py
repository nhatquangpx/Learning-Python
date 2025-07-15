# Khi tạo một tuple, ta gán các giá trị cho nó. Quá trình này được gọi là packing - đóng gói.
fruits = ("apple", "banana", "cherry")

# Ta cũng có thể trích xuất giá trị trở lại các biến. Quá trình này được gọi là unpacking - giải nén.
fruit1, fruit2, fruit3 = fruits
print(fruit1)  # In ra 'apple'
print(fruit2)  # In ra 'banana'
print(fruit3)  # In ra 'cherry'

# Nếu số lượng biến không khớp với số lượng mục trong tuple, sẽ xảy ra lỗi.
# Nếu không, sử dụng dấu hoa thị (*) để thu thập các giá trị còn lại dưới dạng một list
fruits2 = ("apple", "banana", "cherry", "date")
fruit1, *rest = fruits2
print(fruit1)  # In ra 'apple'
print(rest)    # In ra ['banana', 'cherry', 'date']
# Nếu sử dụng dấu * vào các biến khác, sẽ gộp các giá trị cho biến đó đến khi số giá trị còn lại khớp với số biến còn lại
fruits3 = ("apple", "banana", "cherry", "date", "elderberry")
fruit1, *rest, fruit5 = fruits3
print(fruit1)  # In ra 'apple'
print(rest)    # In ra ['banana', 'cherry', 'date']
print(fruit5)  # In ra 'elderberry'

# Ngoài ra, có thể sử dụng dấu gạch dưới (_) để bỏ qua các giá trị không cần thiết
fruit1, _, fruit3 = fruits
print(fruit1)  # In ra 'apple'
print(fruit3)  # In ra 'cherry' - giá trị 'banana' bị bỏ qua