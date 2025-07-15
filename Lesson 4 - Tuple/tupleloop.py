# Sử dụng vòng for lặp qua các mục trong tuple
thistuple = ("apple", "banana", "cherry")
for fruit in thistuple:
    print(fruit)

# Ngoài ra, có thể dùng vòng for lặp qua cac chỉ mục của tuple
for i in range(len(thistuple)):
    print(thistuple[i])  # In ra từng mục theo chỉ mục

# Sử dụng vòng while để lặp qua tuple
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i +=1

# Sử dụng vòng for với hàm enumerate để lấy chỉ mục và giá trị
for index, fruit in enumerate(thistuple):
    print(f"Index {index}: {fruit}")  # In ra chỉ mục và giá trị tương ứng