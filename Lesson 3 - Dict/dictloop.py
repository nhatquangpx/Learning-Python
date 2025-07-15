# Lặp bằng vòng lặp for, sẽ in ra các khóa trong từ điển
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
for x in thisdict:
    print(x)
# Hoặc
for x in thisdict.keys():
    print(x)

# Lặp bằng vòng lặp for, sẽ in ra các giá trị trong từ điển
for x in thisdict:
    print(thisdict[x])
# Hoặc
for x in thisdict.values():
    print(x)

# Lặp bằng vòng lặp for, sẽ in ra các cặp khóa-giá trị trong từ điển
for x, y in thisdict.items():
    print(x, y)