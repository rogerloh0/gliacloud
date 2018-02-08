from bs4 import BeautifulSoup
import requests
import json
from random import randint
from flask import Flask, render_template_string, request

app = Flask(__name__)

url = 'http://wiki.python.org.tw/The%20Zen%20Of%20Python'
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml").select('.line874')

zen_list=[]
for line in soup:
    zen_list.append(line.text)


@app.route('/')

def index():
    rdm = randint(0,30)
    return render_template_string('{{zen}}', zen=zen_list[rdm])


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)