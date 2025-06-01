import time
import requests
import json
from bs4 import BeautifulSoup
list1 = []
data=[]

for i in range(1,11):
        url=f"https://www.sigure.tw/learn-japanese/vocabulary/n3/{i:02d}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", class_="word")
        row1 = table.find_all("tr")[2:]
        row1 = row1[:-1]
        time.sleep(0.5)
        for html in row1:
            if html is None:
                continue
            text = html.get_text().strip()
            list1.append(text)

# 存成 JSON
for row in list1:
            cells = row.split("\n")
            if len(cells)==4:
              japanese1=cells[0]
              japanese = cells[1]
              chinese = cells[3]
            data.append({
                    "日文": japanese1,
                    "平假名": japanese,
                    "中文": chinese
                })
with open("N3.json", "w", encoding="utf-8") as f:
 json.dump(data, f, ensure_ascii=False, indent=2)

print("successful")
