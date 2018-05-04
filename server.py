from flask import Flask, render_template
app = Flask(__name__)

@app.route("/<col>/<row>")
def index(col, row):
    return render_template("index.html", column = int(col), row = int(row), colorOdd = "red", colorEven = "black")

@app.route("/<col>/<row>/<colorOdd>/<colorEven>")
def indexWithColor(col, row, colorOdd, colorEven):
    return render_template("index.html", column = int(col), row = int(row), colorOdd = colorOdd, colorEven = colorEven)


if __name__ == "__main__":
    app.run(debug = True)