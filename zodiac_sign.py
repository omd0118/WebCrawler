import requests
from bs4 import BeautifulSoup

zodiacSigns_convent = {
    '牡羊': '0',
    '金牛': '1',
    '雙子': '2',
    '巨蟹': '3',
    '獅子': '4',
    '處女': '5',
    '天秤': '6',
    '天蠍': '7',
    '射手': '8',
    '摩羯': '9',
    '水瓶': '10',
    '雙魚': '11'
}

# 用户输入星座名称
user_input = input("輸入星座：")
zodiac_sign = user_input.strip()  

zodiac_code = zodiacSigns_convent.get(zodiac_sign)
if zodiac_code is not None:
    url = f"https://astro.click108.com.tw/daily_{zodiac_code}.php?iAstro={zodiac_code}"
    
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    div_element = soup.find('div', class_='TODAY_CONTENT') 
    paragraphs = div_element.find_all('p')
    for paragraph in paragraphs:
        text = paragraph.get_text()
        print(text)
