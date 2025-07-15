# Truy cập vào các mục trong tuple, sử dụng chỉ mục
thistuple = ("apple", "banana", "cherry")
print(thistuple[0])  # In ra 'apple'

# Chỉ số âm được hỗ trợ, cho phép truy cập từ cuối tuple
print(thistuple[-1])  # In ra 'cherry'

# Phạm vi chỉ mục 
thistuple2 = ("apple", "banana", "cherry", "date")
print(thistuple2[1:3])  # In ra ('banana', 'cherry') - từ chỉ mục 1 đến 2 (không bao gồm 3)

# Nếu bỏ qua chỉ mục bắt đầu, nó sẽ bắt đầu từ đầu tuple
print(thistuple2[:2])  # In ra ('apple', 'banana') -

# Nếu bỏ qua chỉ mục kết thúc, nó sẽ lấy đến cuối tuple
print(thistuple2[2:])  # In ra ('cherry', 'date') - từ chỉ mục 2 đến hết

# Nếu bỏ qua cả hai chỉ mục, nó sẽ lấy toàn bộ tuple
print(thistuple2[:])  # In ra ('apple', 'banana', 'cherry', 'date')

# Phạm vi chỉ mục có thể sử dụng chỉ mục âm
print(thistuple2[-3:-1])  # In ra ('banana', 'cherry') - từ chỉ mục -3 đến -2 (không bao gồm -1)

# Kiểm tra xem mục có tồn tại trong tuple hay không
print("banana" in thistuple2)  # In ra True - 'banana' có trong tuple