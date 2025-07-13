# Sắp xếp danh sách theo thứ tự bảng chữ cái và số, dùng sort()
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sắp xếp theo thứ tự giảm dần, dùng reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Tùy chỉnh chức năng sắp xếp
# Sử dụng đối số từ khóa key = function
def myfunc(n):
  return abs(n - 50)                # Sắp xếp theo thứ tự các số càng gần 50 (từ nhỏ đến lớn)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Sắp xếp mặc định phân biệt chữ hoa, chữ thường. Thứ tự sẽ sắp xếp chữ hoa trước, chữ thường sau
# Nếu không muốn phân biệt, sử dụng str.lower làm hàm key
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Đảo ngược thứ tự hiện tại của các phần tử trong danh sách
thislist.reverse()
print(thislist)
