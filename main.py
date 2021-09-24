from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, world. How are you?"

@app.route("/max")
def max():
    return "Hello, Max. How are you?"



if __name__ == "__main__":
    app.run(debug=True)

