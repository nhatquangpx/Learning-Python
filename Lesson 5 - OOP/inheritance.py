# Kế thừa:
# Class con kế thừa class cha => tái sử dụng code, mở rộng chức năng
class Animal:
    def __init__ (self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def bark(self):
        print(f"{self.name} says Woof!")

my_dog = Dog("Buddy", "Brown")
my_dog.eat()  # Buddy is eating.
my_dog.bark()  # Buddy says Woof!

# Giải thích:
# - Class `Animal` là class cha, có phương thức khởi tạo `__init__` và phương thức `eat`.
# - Class `Dog` kế thừa class `Animal`, sử dụng `super()` để gọi phương thức khởi tạo của class cha.
# - Class `Dog` có thêm thuộc tính `color` và phương thức `bark`.
# - Đối tượng my_dog có thể sử dụng phương thức từ lớp cha và phương thức riêng của nó