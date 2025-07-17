# Pandas là thư viện giúp:
# - Đọc dữ liệu từ file CSV, Excel, SQL, JSON...
# - Xử lý dữ liệu: lọc, nhóm, thống kê, biến đổi... (dạng bảng)
# - Phân tích dữ liệu: tính toán thống kê, trực quan hóa...
# - Làm việc với dữ liệu lớn: tối ưu bộ nhớ, tốc độ xử lý...

# Dữ liệu được lưu trong cấu trúc DataFrame (tương tự bảng trong SQL):
# - Hàng (row): Mỗi hàng là một bản ghi dữ liệu.
# - Cột (column): Mỗi cột là một thuộc tính của dữ liệu.

# Giả sử bạn có file CSV students.csv chứa dữ liệu về sinh viên
# Ta sẽ đọc file này bằng pandas
import pandas as pd
df = pd.read_csv('D:\Self-learning\Learning-Python\Lesson 7 - Pandas & Web API\pandas\students.csv')
print(df.head())  # Hiển thị 5 dòng đầu tiên của DataFrame

# Giải thích:
# - df là viết tắt của DataFrame
# - pd.read_csv() là hàm đọc file CSV và trả về DataFrame
# Mỗi cột là một Series, còn cả bảng là DataFrame
# Xem trước dữ liệu
print(df.info())  # Hiển thị thông tin về DataFrame
print(df.describe())  # Hiển thị thống kê mô tả của các cột số

# Các thao tác cơ bản với DataFrame:
# 1. Lọc dữ liệu
# Lọc sinh viên có điểm lớn hơn hoặc bằng 8
filtered_df = df[df["score"] >= 8]
print(filtered_df)

# 2.Tính điểm trung bình
mean_score = df["score"].mean()
print(f"Mean score: {mean_score}")

# 3. Đếm số lượng sinh viên theo giới tính
gender_count = df["gender"].value_counts()
print(gender_count)

# 4.Thêm cột mới
df["passed"] = df["score"] >= 5  # Thêm cột 'passed' dựa trên điều kiện điểm
print(df.head())

# 5. Xóa cột
df.drop("passed", axis = 1, inplace=True)
print(df.head())  # Hiển thị DataFrame sau khi xóa cột 'passed'

# 6. Ghi dữ liệu ra file CSV mới
df.to_csv('D:\Self-learning\Learning-Python\Lesson 7 - Pandas & Web API\pandas\students_updated.csv', index=False)

# 7. Làm việc với Excel
# Cần cài thêm thư viện openpyxl để làm việc với file Excel
# df_excel = pd.read_excel('D:\Self-learning\Learning-Python\Lesson 7 - Pandas & Web API\pandas\students.xlsx')
# print(df_excel.head())  # Hiển thị 5 dòng đầu tiên của DataFrame từ file Excel

