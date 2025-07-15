# Join 2 danh sách với nhau để kết nối 2 hay nhiều danh sách
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Cách khác: dùng vòng lặp kết hợp với append để thêm từng phần tử của list này vào list kia
for x in list2:
    list1.append(x)

print(list1)

# Cách khác: Sử dụng extend() để thêm list này vào cuối list kia
list1.extend(list2)
print(list1)
