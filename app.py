from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World. Say stay with coding and persevere in your programmimg to Zack Amata!"

@app.route('/zack')
def zack():
    return "Hello Zack Amata. Stay with coding and persevere in your programmimg!"


    if __name__ == '__main__':
        app.run(debug=True)
