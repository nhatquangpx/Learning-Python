# API là cổng để lấy dữ liệu từ dịch vụ khác 
# Khi gọi API, thường nhận lại dữ liệu ở dạng JSON
import requests

url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
response = requests.get(url)
data = response.json()

usd_price = data['bpi']['USD']['rate']
print(f"Current Bitcoin price in USD: {usd_price}")

# Giải thích
# requests.get(url) gửi yêu cầu GET đến URL đã chỉ định.
# response.json() chuyển đổi dữ liệu JSON nhận được thành một đối tượng Python (dạng dict)

# Lưu dữ liệu từ API vào file CSV
import pandas as pd
df = pd.DataFrame([{
    'currency': 'USD',
    'price': usd_price
}])
df.to_csv('bitcoin_price.csv', index=False)