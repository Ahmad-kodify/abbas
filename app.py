from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return "Hello, my name is Ahmad with Abbas."

if _name_ == '_main_':
    app.run(debug=True)
