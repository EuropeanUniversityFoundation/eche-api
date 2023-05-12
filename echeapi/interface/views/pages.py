
from flask import flash
from flask_cachecontrol import cache_for

from echeapi import app, settings
from echeapi.interface.utils import render_to_string
from echeapi.utils import api, db, doctree, issues


@app.route("/")
@cache_for(seconds=settings.CACHE_CONTROL_MAX_AGE)
def index():
    return render_to_string('page/home.html', {
        'menu_parent': 'index',
    })


@app.route("/docs/")
@app.route("/docs/<path:params>")
@cache_for(seconds=settings.CACHE_CONTROL_MAX_AGE)
def docs(params=''):
    if not params:
        params = settings.DOCS_DEFAULT

    display, content = doctree.fetch(params.split('/'))

    if display is doctree.Display.DIR:
        flash(f'This is a directory: docs/{params}', category='warning')
    elif display is doctree.Display.ERROR:
        flash(f'Path is invalid: {params}', category='error')

    # Build the sidebar menu.
    menu = doctree.tree()

    # Build the page.
    return render_to_string('page/docs.html', {
        'menu_parent': 'docs',
        'content': content,
        'menu': menu,
    })


@app.route("/explore/")
@cache_for(seconds=settings.CACHE_CONTROL_MAX_AGE)
def explore():
    content = api.as_html(
        fields=settings.ECHE_KEYS,
        table_id='echeTable',
        classes=['table', 'table-striped', 'small'],
    )
    return render_to_string('page/explore.html', {
        'menu_parent': 'explore',
        'content': content,
    })


@app.route("/report/")
@cache_for(seconds=settings.CACHE_CONTROL_MAX_AGE)
def report():
    issues_data = issues.detect_all(db.fetch())
    issues_items = []

    for msg, severity, df, issue_class in issues_data:
        table = df.to_html(
            justify='inherit',
            index=False,
            na_rep='',
            classes=['table', 'table-striped', 'small', 'issues', issue_class],
        ) if not df.empty else ''
        issues_items.append((msg, severity, len(df.index), table))

    return render_to_string('page/report.html', {
        'menu_parent': 'report',
        'issues': issues_items,
    })


@app.route("/openapi/")
@cache_for(seconds=settings.CACHE_CONTROL_MAX_AGE)
def openapi():
    return render_to_string('redoc/index.html')
