from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/max")
def max():
    return "Hello, Max. How are you?"



if __name__ == "__main__":
    app.run(debug=True)

