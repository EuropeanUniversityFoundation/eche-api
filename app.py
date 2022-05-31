from flask import Flask
from flask import render_template
import docs

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('page/home.html')

@app.route("/docs")
@app.route("/docs/<path:params>")
def read_docs(params=''):
    docs.fetch(params.split('/'))
    return render_template('page/placeholder.html', menu_parent='docs')

@app.route("/openapi")
def openapi():
    return render_template('redoc/index.html')

@app.route("/api")
def api():
    return render_template('page/placeholder.html', menu_parent='api')

if __name__ == '__main__':
    app.run(debug=True)
