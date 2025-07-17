# Bài 1: Decorator
# Viết decorator check_positive kiểm tra tất cả tham số phải dương, nếu không in cảnh báo.
def check_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <=0 or (isinstance(arg, float) and arg < 0):
                print ("Warning: All arguments must be positive!")
                return None
        return func(*args, **kwargs)
    return wrapper

@check_positive
def add(a, b):
    return a + b
print(add(5, 10))  # 15
print(add(-5, 10))  # Warning: All arguments must be positive! None

# Bài 2: Generator
# Viết generator fibo(n) sinh dãy Fibonacci tới số thứ n.
def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, b + a

for num in fibo(10):
    print(num)

# Context Manager
# Viết context manager open_file_uppercase đọc file, tự động in nội dung in hoa
class OpenFileUppercase:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        content = self.file.read()
        print(content.upper())
        self.file.close()

with OpenFileUppercase("generators.py") as f:
    pass