print('Hello, world')
from flask import Flask

app = Flask (__name__)

# @app.route('/')
# def main():
#     return "<h1>Hello, world<h1>"

@app.route('/')
def main():
    return "<h1>Hello, world<h1> <br> <a href='/index1'>перейти на 2-ю страницу</a> \
        <br> <a href='/index2'>перейти на 3-ю страницу</a>"

@app.route('/index1')
def index1():
    return "It's my first project"

@app.route('/index2/<x>/<y>')
def index2(x, y):
    return f"Результат: {int(x) + int(y)}"
# в адресной строке надо после указанной ссылки ввести через слеш еще два числа, 
# тогда мы перейдем на страницу, где будет выводиться сумма этих чисел
# Например, вводим "...index2/2/3"
# Получаем "Результат: 5"

# Это называется "Передача аргументов через адресную строку"

if __name__ == '__main__':
    app.run()