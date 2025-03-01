from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, my name is Ahmad <span color : "yellow"> with </span>Abbas."

if __name__ == '__main__':
    app.run(debug=True)
