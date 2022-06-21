
from flask import flash, Markup, render_template

from echeapi import app
from echeapi.utils import doctree, eche


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
        main = Markup(
            render_template(
                'components/markdown.html',
                content=content,
            ),
        )

    elif display == doctree.display_dir:
        main = content

    elif display == doctree.display_err:
        main = ''
        flash(f'Path is invalid: {params}', category='error')

    else:
        raise ValueError(display)

    # Build the sidebar menu.
    menu = doctree.tree()
    sidebar = Markup(
        render_template(
            'components/list.html',
            element='ul',
            dict={'docs': menu},
            prefix='docs',
        ),
    )

    # Build the page.
    return render_template(
        'page/docs.html',
        menu_parent='docs',
        htag=htag,
        main=main,
        sidebar=sidebar,
        card_title='Directory tree',
    )
    # return render_template('page/placeholder.html', menu_parent='docs')


@app.route("/explore/")
def explore():
    content = Markup(eche.to_html(classes=['table', 'table-striped', 'small']))
    return render_template(
        'page/explore.html',
        menu_parent='explore',
        content=content,
    )


@app.route("/openapi/")
def openapi():
    return render_template('redoc/index.html')
