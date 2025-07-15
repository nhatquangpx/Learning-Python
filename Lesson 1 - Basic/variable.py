# Biến không cần khai báo kiểu dữ liệu, nó được tạo cùng với giá trị
x=10
y="hello"

# Biến có thể bị đổi kiểu dữ liệu sau khi gán các giá trị khác
x=10.5   
x="thanks"  

# Nếu muốn chỉ định kiểu dữ liệu, cần ép kiểu
x = int (10)
y = str (10)
z = float (10)

# Cú pháp lấy kiểu dữ liệu của biến
x = 10
print (type(x))
x = str (10)
print (type(x))

# Biến string có thể khai báo bằng dấu ngoặc đơn và dấu ngoặc kép
x = "hello"
#is the same as
x = 'hello'

# Có phân biệt chữ hoa chữ thường
a = 120
A = "Hi"

# Có 3 cách viết tên biến
myLove = "1" # Cách viết theo quy tắc camel case
MyLove = "2" # Cách viết theo quy tắc Pascal case
my_love = "3" # Cách viết theo quy tắc snake case

# Gán giá trị nhiều biến trên một dòng
x, y, z = 1,2,3
print (x,y,z)

# Unpack một mảng các giá trị
fruits = ["1","2","3"]
x, y, z = fruits
print (x,y,z)

# Biến toàn cục
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# Nếu có biến cục bộ trong hàm, ưu tiên dùng biến cục bộ
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# Tạo biến toàn cục trong một hàm
# Sử dùng từ khóa 'global'
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

# Thay đổi giá trị biến toàn cục (ở ngoài hàm) trong một hàm
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

