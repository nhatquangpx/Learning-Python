# Một số mehtod đặc biệt trong Python
# '__init__' là phương thức khởi tạo, được gọi khi tạo một đối tượng mới từ lớp.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# '__str__' là phương thức trả về chuỗi mô tả đối tượng, được gọi khi sử dụng hàm print.
    def __str__(self):
        return f"{self.name} is {self.age} years old."
# '__eq__' là phương thức so sánh hai đối tượng, được gọi khi sử dụng toán tử ==.
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
# '__repr__' là phương thức trả về chuỗi mô tả đối tượng, được gọi khi sử dụng hàm repr.
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
    
# 'f"abc"': Cú pháp f-string để định dạng chuỗi, cho phép chèn giá trị của biến vào chuỗi.
# 'self': Tham chiếu đến đối tượng hiện tại, cho phép truy cập các thuộc tính và phương thức của đối tượng.
# 'other': Tham chiếu đến đối tượng khác để so sánh trong phương thức __eq__.