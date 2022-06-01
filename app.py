from flask import Flask, render_template, Markup, url_for, redirect
import doctree

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('page/home.html')

@app.route("/docs")
@app.route("/docs/<path:params>")
def docs(params=''):
    menu = doctree.tree()
    sidebar = Markup(
        render_template(
            'components/list.html',
            element='ul',
            dict={'docs': menu}
        )
    )

    doctree.fetch(params.split('/'))

    return render_template(
        'page/docs.html',
        sidebar=sidebar,
    )
    # return render_template('page/placeholder.html', menu_parent='docs')

@app.route("/openapi")
def openapi():
    return render_template('redoc/index.html')

@app.route("/api")
def api():
    return render_template('page/placeholder.html', menu_parent='api')

if __name__ == '__main__':
    app.run(debug=True)
