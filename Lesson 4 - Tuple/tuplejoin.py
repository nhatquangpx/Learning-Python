# Để join 2 tuple, ta có thể sử dụng toán tử cộng (+)
tuple1 = ("apple", "banana")
tuple2 = ("cherry", "date")
tuple3 = tuple1 + tuple2  # Nối hai tuple
print(tuple3)  # In ra ('apple', 'banana', 'cherry', 'date')

# Nhân tupele với một số nguyên để lặp lại các mục trong tuple
tuple4 = tuple1 * 2  # Nhân tuple1 với 2
print(tuple4)  # In ra ('apple', 'banana', 'apple', 'banana')

# Có thể join nhiều tuple cùng lúc
tuple5 = tuple1 + tuple2 + ("elderberry",)  # Nối ba tuple
print(tuple5)  # In ra ('apple', 'banana', 'cherry', 'date', 'elderberry')