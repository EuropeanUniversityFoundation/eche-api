from flask import Flask, render_template, Markup, Response, redirect, flash
from jinja_markdown import MarkdownExtension
import doctree
import eche
import response

import local_settings

app = Flask(__name__)
app.jinja_env.add_extension(MarkdownExtension)
app.secret_key = local_settings.app_secret_key

@app.route("/")
def index():
    return render_template('page/home.html')

@app.route("/docs/")
@app.route("/docs/<path:params>")
def docs(params=''):
    display, content = doctree.fetch(params.split('/'))
    htag = 'h1'

    if display == doctree.display_md:
        htag = 'h5'
        markdown = content.read()
        main = Markup(
            render_template(
                'components/markdown.html',
                content=markdown
            )
        )

    if display == doctree.display_dir:
        main = content

    if display == doctree.display_err:
        main = ''
        flash('Path is invalid.', category='error')

    # Build the sidebar menu.
    menu = doctree.tree()
    sidebar = Markup(
        render_template(
            'components/list.html',
            element='ul',
            dict={'docs': menu}
        )
    )

    # Build the page.
    return render_template(
        'page/docs.html',
        menu_parent='docs',
        htag=htag,
        main=main,
        sidebar=sidebar,
        card_title='Directory tree'
    )
    # return render_template('page/placeholder.html', menu_parent='docs')

@app.route("/explore/")
def explore():
    content = Markup(eche.to_html(classes=['table', 'table-striped', 'small']))
    return render_template(
        'page/explore.html',
        menu_parent='explore',
        content=content
    )

@app.route("/openapi/")
def openapi():
    return render_template('redoc/index.html')

@app.route("/api/", methods = ['GET'])
@app.route("/api/<string:key>/<string:value>/", methods = ['GET'])
def api(key='', value=''):
    if key in local_settings.eche_headers.values():
        body = response.list(filter=(key, value))
    else:
        body = response.list()

    return Response(body, mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True)
