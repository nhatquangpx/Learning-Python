# Mini project: Lấy giá bitcoin từ API và lưu vào file CSV
import requests
import pandas as pd
from datetime import datetime

def get_btc_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    data = requests.get(url).json()
    return dâta['bpi']['USD']['rate']

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
price = get_btc_price()

df = pd.DataFrame([{
    'timestamp': now,
    'currency': 'USD',
    'price': price
}])
df.to_csv('D:\Self-learning\Learning-Python\Lesson 7 - Pandas & Web API\miniproject_btc_price.csv', mode='a', header=not pd.io.file_exists("D:\Self-learning\Learning-Python\Lesson 7 - Pandas & Web API\miniproject_btc_price.csv"), index=False)