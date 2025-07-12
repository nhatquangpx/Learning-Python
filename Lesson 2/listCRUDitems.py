# SỬA PHẦN TỬ TRONG LIST

# Sửa bằng chỉ mục
thislist = ["orange", "apple", "grape", "peach", "banana"]
thislist[1]= "mango"
print(thislist[1])

# Thay đổi phạm vi giá trị chỉ mục
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Nếu chèn số lượng phần tử vượt quá phạm vi chỉ mục, sẽ chèn thêm phần tử mới vào sau phần tử vừa chỉnh sửa
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# Nếu chèn số lượng phần tử ít hơn phạm vi chỉ mục, sẽ bỏ đí các phần tử ở các vị trí bị thiếu
thislist[1:3] = ["watermelon"]
print(thislist)

#------------------------------------------
# THÊM PHẦN TỬ VÀO LIST

# Thêm phần tử vào cuối list, dùng append
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# Chèn phần tử mới vào vị trí cụ thể trong list mà không thay đổi bất kì giá trị nào hiện có trong phần tử, dùng insert
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Thêm bằng cách ghép list khác vào cuối list hiện tại, dùng extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Thêm bằng cách ghép bất kì dạng đối tượng lặp lại nào
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#------------------------------------------
# XÓA PHẦN TỬ TRONG LIST

# Xóa giá trị chỉ định, dùng remove
# Nếu có nhiều hơn 2 giá trị giống nhau, xóa phần tử đầu tiên tìm được
thislist = ["apple", "banana", "cherry", "orange"]
thislist.remove("banana")
print(thislist)

# Xóa chỉ mục chỉ định, có 2 cách
# Dùng pop:
thislist.pop(1)
print(thislist)
# Nếu không có chỉ mục, auto xóa phần tử cuối cùng
thislist.pop()
print(thislist)

# Dùng del:
thislist = ["apple", "banana", "cherry", "orange"]
del thislist[2]
print(thislist)
# Nếu không có chỉ mục cụ thể sẽ xóa toàn bộ list, khi đó list không còn tồn tại
del thislist

# Muốn làm trống list, mà vẫn giữ lại list, dùng clear()
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)