# Đa hình:
# Các object khác nhau nhưng có cùng phương thức, mỗi object thực thi theo cách riêng
class Animal:
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
    
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
    
def animal_sound(animal):
    print(animal.speak())

# Sử dụng đa hình
dog = Dog()
cat = Cat()
animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!

# Giải thích:
# - Class `Animal` là lớp cha với phương thức `speak` chưa được cài đặt.
# - Class `Dog` và `Cat` kế thừa từ `Animal` và cài đặt phương thức `speak` theo cách riêng.
# - Hàm `animal_sound` nhận một đối tượng `Animal` và gọi phương thức `speak`, cho phép sử dụng đa hình.
