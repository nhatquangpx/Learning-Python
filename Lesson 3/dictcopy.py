# Sao chép từ điển bằng phương thức copy()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
newdict = thisdict.copy()
print(newdict)

# Sao chép từ điển bằng hàm dict()
newdict = dict(thisdict)
print(newdict)