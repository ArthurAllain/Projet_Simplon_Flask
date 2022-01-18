from flask import Flask, render_template
app = Flask(__name__, template_folder='../Html_Script', static_folder= '../Css_Script') # rename des folder "templates" et "static" en "Html_Script" et "Css_Script"

@app.route("/")
def hello():    #Fct retournant la page home.html renderisé
    return render_template("home.html", message = "Hello World!")

if __name__ == "__main__":
    app.run(debug=True)