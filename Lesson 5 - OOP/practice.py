#  Bài 1
# Viết class Student có:
# Thuộc tính: name, score.
# Method: in thông tin, kiểm tra đậu (>5 điểm).
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def check_pass(self):
        return self.score > 5
    def display_info(self):
        status = "Passed" if self.check_pass() else "Failed"
        print(f"Name: {self.name}, Score: {self.score}, Status: {status}")
stu1 = Student ("Quang", 10)
stu1.display_info()  

# Bài 2
# Viết class Shape (hình), kế thừa thành Circle và Rectangle, tính diện tích.
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Circle area: {circle.area()}")  # Circle area: 78.5
print(f"Rectangle area: {rectangle.area()}")  # Rectangle area: 24
