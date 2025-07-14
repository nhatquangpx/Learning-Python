# Từ điển lồng nhau (nested dictionary) là một từ điển chứa các từ điển khác bên trong nó
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
# Hoặc tạo 3 từ điển con riêng biệt và sau đó thêm chúng vào từ điển cha
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",   
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

# Truy cập các mục trong từ điển lồng nhau, sử dụng tên từ điển, từ từ điển bên ngoài
print(myfamily["child1"]["name"])  

# Lặp qua từ điển lồng nhau
for child, info in myfamily.items():
    print(child)

    for key in info:
        print(key + ":", info[key])