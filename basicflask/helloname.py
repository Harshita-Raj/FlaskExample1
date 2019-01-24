from flask import Flask
app = Flask(__name__)

@app.route('/hi/<name>')
def hello_name(name):
    return 'Hello ' + name

@app.route('/hello/<int:value>')
def number(value):
    return 'Hello %d ' % value

@app.route('/float/<float:val>')
def number1(val):
    return 'Float %f ' % val

if __name__ == "__main__":
    app.run(debug=True)
