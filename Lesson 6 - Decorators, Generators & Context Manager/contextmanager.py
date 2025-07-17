# Context Mangager:
# Quản lí tài nguyên (file, network, database) một cách an toàn và hiệu quả, tự động giải phóng tài nguyên khi không còn sử dụng.
class MyContextManager:
    def __enter__(self):
        print("Start conbtext")
        return "Context Manager has been initialized"
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exit context")

with MyContextManager() as val:
    print(f"Inside context: {val}")
