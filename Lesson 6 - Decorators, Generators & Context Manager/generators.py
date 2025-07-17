# Generators:
# Dùng để tạo ra các giá trị một cách lười biếng (lazy evaluation), tiết kiệm bộ nhớ
# và cho phép lặp qua các giá trị mà không cần lưu trữ toàn bộ trong bộ nhớ.
# Cú pháp tạo generator
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator
for x in gen():
    print(x)

# Giải thích:
# - `yield`: Từ khóa dùng để trả về giá trị từ generator, cho phép tiếp tục thực thi từ điểm dừng khi gọi lại.
# - `my_generator()`: Gọi hàm generator, trả về một iterator.
# Khi gặp yield, hàm "pause" và chờ lần gọi tiếp theo.
def example_yield():
    yield 1
    yield 2
    yield 3

gen = example_yield()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3

# Tạo dãy vô hạn bằng generator
def infinite_numbers():
    num = 1
    while True:
        yield num
        num += 1
infinite_gen = infinite_numbers()
for _ in range(5):
    print(next(infinite_gen))  # In ra 1, 2, 3, 4, 5
# - `next()`: Hàm dùng để lấy giá trị tiếp theo từ iterator, trong trường hợp này là generator.