import requests
import json

url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-A0010-001?Authorization=CWA-975B36C2-1364-443A-9CB1-DF7C18E97095&downloadType=WEB&format=JSON'

# 发送 HTTP GET 请求
data = requests.get(url)
data_json = data.json()

    
    # 确保你了解 JSON 数据的结构，然后访问正确的键
    # 以下是示例，假设 JSON 结构为 data -> agrWeatherForecasts -> weatherProfile
weather_profile = data_json["cwaopendata"]["resources"]["resource"]["data"]["agrWeatherForecasts"]["weatherProfile"]
locations = data_json["cwaopendata"]["resources"]["resource"]["data"]["agrWeatherForecasts"]["weatherForecasts"]["location"]

for location_data in locations:
    location_name = location_data["locationName"]
    print(f"地區: {location_name}")

    wx_data = location_data["weatherElements"]["Wx"]["daily"]
    temp_data = location_data["weatherElements"]["MaxT"]["daily"]
    
    first_day = wx_data[0]
    last_day = wx_data[-1]

    print(f"第一天日期: {first_day['dataDate']}")
    print(f"最後一天日期: {last_day['dataDate']}")

    for day, temp in zip(wx_data, temp_data):
        print(f"日期: {day['dataDate']}, 天气: {day['weather']}, 温度: {temp['temperature']} °C")
    print()


    
