# Định nghĩa hàm sử dụng từ khóa def
def func():
    print("This is a function")

# Gọi hàm
func()

# Truyền đối số vào hàm
# Tham số là danh sách các biến được liệt kê trong phần định nghĩa hàm
# Đối số là giá trị được gửi đến hàm khi nó được gọi
def argfunc(name):
    print ("I am " + name)

argfunc("Quang")

# Đối số tùy ý: Dùng * trước tên biến để có thể truyền số lượng đối số tùy ý vào hàm
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Đối số từ khóa: Truyền đối số vào với cú pháp key = value
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# Đối số từ khóa tùy ý:  Dùng ** trước tên biến
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

# Giá trị tham số mặc định
# Nếu như gọi hàm mà không truyền đối số thì sẽ sử dụng giá trị mặc định trong định nghĩa hàm
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Truyền một list như một đối số
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Trả về sử dụng từ khóa return
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Nếu cần bỏ trống nội dung function, dùng từ khóa pass
def passfunc():
    pass

