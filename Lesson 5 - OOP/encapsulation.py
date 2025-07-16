# Đống gói:
# Ẩn thông tin chi tiết bên trong object, chỉ cho phép truy cập qua method
class Person:
    def __init__(self, name, age):
        self.__name = name  # Thuộc tính riêng tư
        self.__age = age    # Thuộc tính riêng tư

    def get_name(self):
        return self.__name  # Phương thức truy cập tên

    def get_age(self):
        return self.__age    # Phương thức truy cập tuổi

    def set_age(self, age):
        if age > 0:
            self.__age = age  # Phương thức thay đổi tuổi

p = Person("Alice", 30)
print(p.get_name())  # Alice
print(p.get_age())   # 30
p.set_age(31)
print(p.get_age())   # 31

# Giải thích:
# Thuộc tính privated (bắt đầu bằng `__`) không thể truy cập trực tiếp từ bên ngoài lớp.
