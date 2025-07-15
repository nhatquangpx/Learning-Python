# List là kiểu dữ liệu dùng để lưu trữ nhiều giá trị trong một biến duy nhất 
thislist = ["banana","apple","orange"]
print(thislist)

# Nếu thêm giá trị mới vào list, giá trị đó sẽ được đặt ở cuối danh sách
# Có thể update các giá trị trong list sau khi đã được tạo
# Các giá trị trong 1 list có thể trùng lặp

# Độ dài danh sách
print(len(thislist))

# Một danh sách có thể lưu 1 hoặc nhiều kiểu dữ liệu khác nhau
thatlist = [12, 1.4, "hi"]
print(thatlist)

# Kiểu dữ liệu của list là list
print(type(thatlist))

# Sử dụng hàm list() để tạo list mới, chú ý khi này dùng hai dấu ngoặc đơn ((...))
theselist = list((1,2,3,4))
print(theselist)

#-----------------------------------#
# CHỈ MỤC

# Lấy giá trị bằng chỉ mục
print(thislist[0])

# Chỉ mục âm sẽ lấy từ dưới lên, bắt đầu từ -1 là phần tử cuối cùng, -2 là phần tử thứ 2 từ dưới lên
print(thislist[-1])

# Phạm vi chỉ mục [a:b] -> từ phần tử thứ a đến phần tử thứ b-1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# Nếu bỏ trống phần đầu thì bắt đầu từ phần tử thứ 0
print(thislist[:4])
# Nếu bỏ trống phần cuối thì tiếp tục đến khi hết phần từ cuối cùng (có bao gồm phần tử cuối)
print(thislist[2:])
# Nếu phạm vi chỉ mục âm [a,b], làm như bình thường, chú ý không lấy phần tử thứ b
print(thislist[-4:-1])

# Kiểm tra xem phần tử có nằm trong list không, dùng in
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#-----------------------------------#







