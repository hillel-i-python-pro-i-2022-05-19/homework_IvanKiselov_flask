import json
from flask import Flask, request
from faker import Faker
import aiohttp
import requests

app = Flask(__name__)


@app.route('/requirements/')
def get_requirements():
    file = request.args.get('file','file.txt')
    fileq = open(file)
    text = fileq.read()
    return text

@app.route('/generate-users/')
def generate_users():
    amount=request.args.get('amount',100)
    fake = Faker()
    resp_list = []
    for i in range (amount):
        resp_list.append(f'{fake.name()} {fake.email()}')

    response = "<br>".join(resp_list)
    return response

@app.route('/space/')
async def space():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://api.open-notify.org/astros.json') as response:
            res = await response.text()
            resp = json.loads(res).get("number")
            print("Содержимое:",type(resp))

    return f'Количество космонавтов в данный момент: {resp}'

@app.route('/mean/')
def average_mean():
    res = requests.get('https://drive.google.com/uc?export=download&id=1yM0a4CSf0iuAGOGEljdb7qcWyz82RBxl',headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:100.0) Gecko/20100101 Firefox/100.0'})
    res= str(res.text)
    resspl = res.replace('\n', ',').split(',')
    del (resspl[0:3])
    del (resspl[-2:])

    height_list = []
    weight_list = []

    i = 1
    for el in range(len(resspl)//3):
        height_list.append(float(resspl[i]))
        i = i + 3

    i = 2
    for el in range(len(resspl) // 3):
        weight_list.append(float(resspl[i]))
        i = i + 3

    height_avg = sum(height_list) / len(height_list)
    weight_avg = sum(weight_list)/len(weight_list)

    return f'Средний вес {round(height_avg, 2)} кг, средний рост {round(weight_avg, 2)} см'



if __name__ == '__main__':
    app.run(debug=True)









