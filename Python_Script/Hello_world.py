from flask import Flask  # pip install flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Test!"

if __name__ == "__main__":
    app.run()