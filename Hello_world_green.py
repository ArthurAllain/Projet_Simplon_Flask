from flask import Flask, render_template
app = Flask(__name__, template_folder='Html Script', static_folder= 'Css Script')

@app.route("/")
def hello():
    return render_template("home.html", message = "Hello World!")

if __name__ == "__main__":
    app.run()