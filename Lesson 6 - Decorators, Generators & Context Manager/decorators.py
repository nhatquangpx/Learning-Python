# Decorators:

# Cho phép gói một hàm khác để mở rộng chức năng của nó mà không cần thay đổi mã nguồn của hàm đó.
# Cú pháp: Sử dụng ký hiệu @ trước tên hàm decorator 
def decorator_function(original_function):
    def wrapper_function():
        print ("Start...")
        original_function()
        print ("End...")
    return wrapper_function
@decorator_function
def display():
    print("Hello, World!")
display()

# Giải thích:
# - `decorator_function`: Là hàm decorator, nhận một hàm `original_function` làm đối số.
# - `wrapper_function`: Là hàm bên trong `decorator_function`, thực hiện các thao tác trước và sau khi gọi `original_function`.
# - original_function: Là hàm gốc được truyền vào, trong trường hợp này là `display`.
# - `@decorator_function`: Là cú pháp để áp dụng decorator cho hàm `display`, tương đương với `display = decorator_function(display)`.
# - Khi gọi `display()`, thực chất là gọi `wrapper_function`, in ra "Start...", sau đó gọi `original_function` và in ra "End...".

# Decorators với đối số:
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper
@log_function
def add(a, b):
    return a + b
add(3, 5)

# Giải thích:
# - `log_function`: Là hàm decorator, nhận một hàm `func` làm đối số.
# - `wrapper`: Là hàm bên trong `log_function`, nhận các đối số và từ khóa của hàm gốc.
# - `*args` và `**kwargs`: Cho phép truyền bất kỳ số lượng đối số và từ khóa nào vào hàm gốc.
# - `func.__name__`: Trả về tên của hàm gốc để in ra thông tin.

# CÁC TRƯỜNG HỢP SỬ DỤNG DECORATOR:
# 1. Kiểm tra quyền truy cập:
def requires_permission(permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if permission == "admin":
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have permission to access this function.")
        return wrapper
    return decorator
@requires_permission("admin")
def admin_function():
    print("Admin function executed.")
    try:
        admin_function()
    except PermissionError as e:
        print(e)

# 2. Logging:
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} executed successfully.")
        return result
    return wrapper
@log_execution
def multiply(a, b):
    return a * b
multiply(2, 3)

# 3. Thời gian thực thi:
import time
def time_execution(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper
@time_execution
def slow_function():
    time.sleep(2)
slow_function()

# 4. Cache kết quả:
def cache_results(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("Returning cached result.")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            print("Result cached.")
            return result
    return wrapper
@cache_results
def expensive_function(x):
    print(f"Calculating {x}...")
    return x * x
expensive_function(5)
expensive_function(5)  # Sẽ sử dụng kết quả đã cache

# 5. Thay đổi hành vi của hàm:
def modify_behavior(func):
    def wrapper(*args, **kwargs):
        print("Modifying behavior before calling the function.")
        result = func(*args, **kwargs)
        print("Behavior modified after calling the function.")
        return result
    return wrapper
@modify_behavior
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

