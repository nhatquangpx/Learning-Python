# DÙNG VÒNG LẶP VỚI LIST

# Dùng vòng lặp for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Lặp bằng tham số chỉ mục
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

# Dùng vòng lặp while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

# Dùng list comprehension - cú pháp ngắn nhất
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]