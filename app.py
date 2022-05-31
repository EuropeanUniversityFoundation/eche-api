from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('page/home.html')

@app.route("/openapi")
def openapi():
    return render_template('redoc/index.html')

if __name__ == '__main__':
    app.run(debug=True)
