from flask import Flask, render_template, request
import json
import random
import os
from datetime import datetime
import re

app = Flask(__name__)

@app.route('/')
def home():
     return render_template('index.html', timestamp=int(datetime.now().timestamp()))

@app.route('/test1', methods=['GET','POST'])
def test1():
    level = request.form.get('level')  # e.g., "N5"
    mode = request.form.get('mode')    # e.g., "中對日"

    # 根據等級載入不同 JSON
    filename = f"{level}.json"
    path = os.path.join(os.getcwd(), filename)
    with open(path, 'r', encoding='utf-8') as f:
        options=[]
        data = json.load(f)
        if mode=="中對日":
            right = random.choice(data)
            if  re.search(r'[A-Za-z]', right["平假名"]):
                ans=right["日文"]
                options.append(right["日文"])
            else:
                ans=right["平假名"]
                options.append(right["平假名"])
            # 從data裡排除正確答案，隨機抽3個錯誤日文選項
            all = [item for item in data if item != right]
            wrong = random.sample(all, 3)
            for i in range(0,3):
                if  re.search(r'[A-Za-z]', wrong[i]["平假名"]):
                    options.append(wrong[i]["日文"])

                else:
                    options.append(wrong[i]["平假名"])
                
            # 將正確答案和錯誤選項合併後打亂順序
            
            random.shuffle(options)
            
            # 傳給前端題目中文、選項列表、正確答案
            print(right['中文'],options,right['平假名'])

            return render_template('test1.html', question=right['中文'], options=options, answer=ans)
        else:
            
            right = random.choice(data)

            # 題目是平假名或片假名
            if re.search(r'[A-Za-z]', right["平假名"]):
                question = right["日文"]
            else:
                question = right["平假名"]

            ans = right["中文"]

            # 錯誤選項（中文）
            wrong_pool = [item['中文'] for item in data if item != right]
            wrong_choices = random.sample(wrong_pool, 3)

            # 建立選項列表（正確答案 + 錯誤答案），並打亂
            options = wrong_choices + [ans]
            random.shuffle(options)

            print(question, options, ans)

            return render_template(
                'test1.html',
                question=question,
                options=options,
                answer=ans
            )

if __name__ == '__main__':
    app.run(debug=True)
