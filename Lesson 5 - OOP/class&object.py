# Cú pháp tạo cass
class Dog:
    # Phương thức khởi tạo
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Phương thức mô tả hành động
    def bark(self):
        print(f"{self.name} with {self.age} yearsold says Woof!")

my_dog = Dog("Buddy", 3)  # Tạo một đối tượng Dog mới
my_dog.bark()  # Gọi phương thức bark của đối tượng my_dog

# Giải thích: 
# - `class Dog:`: Định nghĩa một lớp mới có tên là Dog.
# - __init__ : Hàm khởi tạo, tự động gọi khi tạo object từ lớp Dog.
# - `self`: Tham chiếu đến đối tượng hiện tại, cho phép truy cập các thuộc tính và phương thức của đối tượng
# - `name` và `age`: Thuộc tính của đối tượng Dog, được khởi tạo khi tạo một đối tượng mới.