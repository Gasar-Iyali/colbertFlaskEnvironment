from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return "Hello World. Say stay with coding and persevere in your programmimg to Zack Amata!"
    return render_template('index.html', pageTitle='Zack Amata Flask Web App')
@app.route('/zack')
def zack():
    return render_template('zack.html', pageTitle=' Amata Zack  Flask Web App')
@app.route('/base')
def base():
    return render_template('base.html', pageTitle=' Amata Flask Web App Zack  ')


    if __name__ == '__main__':
        app.run(debug=True)
