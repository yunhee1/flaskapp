from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '대박 배포 성공!'
