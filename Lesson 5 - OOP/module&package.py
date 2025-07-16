# MODULE:

# Một file .py được gọi là một module
# Một module có thể chứa các class, hàm, biến, v.v.
# Để sử dụng module, ta cần import nó vào file khác
# Dùng module để tách code thành các phần nhỏ, dễ quản lý hơn
# Ví dụ: tạo một module có tên `math_utils.py` với các hàm toán học cơ bản
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
# Sau đó, ta có thể import module này vào file khác
# Ví dụ: import module `math_utils` và sử dụng các hàm trong đó

# import math_utils

# Hoặc import trực tiếp các hàm cần thiết

# from math_utils import add, subtract

# PACKAGE:
# Một package là một thư mục chứa nhiều module, cho phép tổ chức code theo cấu trúc phân cấp
# Thư mục này cần có file `__init__.py` để Python nhận diện là package
# Ví dụ: tạo một package có tên `my_package` với các module `math_utils.py` và `string_utils.py`
# Cấu trúc thư mục:
# my_package/
# ├── __init__.py
# ├── math_utils.py
# └── string_utils.py
# Trong file `__init__.py`, ta có thể import các module cần thiết