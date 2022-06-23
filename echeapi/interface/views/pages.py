
from flask import flash, Markup, render_template
from flask_cachecontrol import cache_for

from echeapi import app, cache, settings
from echeapi.utils import api, doctree


@app.route("/")
@cache_for(seconds=settings.CACHE_CONTROL_MAX_AGE)
def index():
    return render_template(
        'page/home.html',
        menu_parent='index',
    )


@app.route("/docs/")
@app.route("/docs/<path:params>")
@cache_for(seconds=settings.CACHE_CONTROL_MAX_AGE)
def docs(params=''):
    if not params:
        params = settings.DOCS_DEFAULT

    display, content = doctree.fetch(params.split('/'))
    htag = 'h1'
    main = Markup(render_template('snippets/docs-placeholder.html'))

    if display == doctree.Display.FILE:
        htag = 'h5'
        main = Markup(
            render_template(
                'components/markdown.html',
                content=content,
            ),
        )

    elif display == doctree.Display.DIR:
        if params:
            flash(content, category='warning')

    elif display == doctree.Display.ERROR:
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
@cache_for(seconds=settings.CACHE_CONTROL_MAX_AGE)
def explore():
    _key = 'explore-table'

    table = cache.get(_key)
    if table is None:
        table = Markup(api.as_html(
            table_id='echeTable',
            classes=['table', 'table-striped', 'small'],
        ))
        cache.set(_key, table, timeout=settings.DATA_CACHE_TIMEOUT)

    return render_template(
        'page/explore.html',
        menu_parent='explore',
        content=table,
    )


@app.route("/openapi/")
@cache_for(seconds=settings.CACHE_CONTROL_MAX_AGE)
def openapi():
    return render_template('redoc/index.html')
