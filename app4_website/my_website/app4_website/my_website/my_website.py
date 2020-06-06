#step 1: import Flask class from flask module
from flask import Flask, render_template

#step 2: create variable that store flask application
app = Flask(__name__)

#step 3: Integrator, page path, function or contents
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug = True )


