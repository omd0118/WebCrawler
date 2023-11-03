import requests
from bs4 import BeautifulSoup
url = "https://www.cpc.com.tw/GetOilPriceJson.aspx?type=TodayOilPriceString"
response = requests.get(url)
data = response.json()
t_UpOrDown = data.get('UpOrDown_Html')
if t_UpOrDown:
# 使用Beautiful Soup解析HTML
    soup = BeautifulSoup(t_UpOrDown, "html.parser")
# 找到 "調降" 文本
down_element = soup.find(class_="sys")

# 找到調降多少文本
rate_element = soup.find(class_="rate").find("i")

if down_element and rate_element:
    down_text = down_element.get_text()
    rate_text = rate_element.get_text()

# 取得 PriceUpdate 的資訊
t_PriceUpdate = data.get('PriceUpdate')
print(f"{t_PriceUpdate}零時起實施")
print(f"本週油價{down_text}{rate_text}")
print(f"92無鉛：{data.get('sPrice1')}元/公升")
print(f"95無鉛：{data.get('sPrice2')}元/公升")
print(f"98無鉛：{data.get('sPrice3')}元/公升")
print(f"酒精汽油：{data.get('sPrice4')}元/公升")
print(f"超級柴油：{data.get('sPrice5')}元/公升")
print(f"液化石油氣：{data.get('sPrice6')}元/公升")