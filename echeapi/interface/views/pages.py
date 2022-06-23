
from flask import flash, Markup, render_template

from echeapi import app, settings
from echeapi.utils import api, doctree


@app.route("/")
def index():
    return render_template(
        'page/home.html',
        menu_parent='index',
    )


@app.route("/docs/")
@app.route("/docs/<path:params>")
def docs(params=''):
    if not params:
        params = settings.DOCS_DEFAULT

    display, content = doctree.fetch(params.split('/'))
    htag = 'h1'
    main = Markup(render_template('snippets/docs-placeholder.html'))

    if display == doctree.DISPLAY_MD:
        htag = 'h5'
        main = Markup(
            render_template(
                'components/markdown.html',
                content=content,
            ),
        )

    elif display == doctree.DISPLAY_DIR:
        if params:
            flash(content, category='warning')

    elif display == doctree.DISPLAY_ERR:
        flash(f'Path is invalid: {params}', category='error')

    else:
        raise ValueError(display)

    # Build the sidebar menu.
    menu = doctree.tree()
    sidebar = Markup(
        render_template(
            'components/list.html',
            element='ul',
            dict=menu,
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


@app.route("/explore/")
def explore():
    content = Markup(api.as_html(
        table_id='echeTable',
        classes=['table', 'table-striped', 'small'],
    ))
    return render_template(
        'page/explore.html',
        menu_parent='explore',
        content=content,
    )


@app.route("/openapi/")
def openapi():
    return render_template('redoc/index.html')
