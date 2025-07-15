# Sao chép list, sử dụng phương thức copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Ngoài ra có thể sử dụng phương thức list()
mylist2= list(thislist)
print(mylist2)

# Sử dụng toán tử slice ":"
mylist3= thislist[:]
print(mylist3)
