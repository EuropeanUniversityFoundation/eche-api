# ECHE List API

This repository contains the specification of the ECHE List API, along with its documentation.

## Introduction

### What is the ECHE List API?

The **ECHE List API** is designed to expose the list of institutions holding the _Erasmus Charter for Higher Education_, as published by the European Commission, in a machine readable format.

## Installation

The main app is built with Flask, and it requires Python 3.8+ to run. To start the virtual environment and install the required libraries, execute the following commands:

    # generate and activate a virtual environment
    python3 -m venv venv
    source venv/bin/activate
    # install required libraries
    pip install -r requirements.txt

In order to run the app, some preparatory steps are needed:

    # check the local settings
    cp echeapi/settings/default.py echeapi/settings/local.py
    nano echeapi/settings/local.py
    # create empty database
    python echeapi/manage.py initialize
    # populate the database
    python echeapi/manage.py populate

## Development

When developing the Python application, install the development packages as well:

    # install required libraries
    pip install -r requirements-dev.txt

Inside the `redoc` directory there is a `README` file with detailed instructions to build the interactive specification.

### Built-in server

To use the built-in web server locally, in debug mode, execute the following command:

    python echeapi/manage.py run

Or:

    export FLASK_APP=echeapi
    export FLASK_ENV=development
    flask run

## Deployment

By default, this application is deployed on a server with the Plesk web admin panel. Alternative deployment methods are also suggested below.

### Plesk + nginx + Phusion Passenger

Deploy the code to the `DOCROOT`; for a top-level domain, it will be `httpdocs`; for a subdomain, it will look like `sub.domain.tld`. Follow the installation instructions above.

**After** the code is deployed, go to _Hosting settings_ and change the _Document root_ to `DOCROOT/echeapi`.

Then, go to _Apache & nginx Settings_ and do the following:

1. under _nginx settings_ turn off __Proxy mode__ to stop using Apache;
2. under _Additional nginx directives_ add `passenger_enabled on;` and save.

_Phusion Passenger_ by convention will read the `passenger_wsgi.py` file from one level above the new _Document root_ and use the correct Python binary from the `venv` created upon installation.

### Apache2 + uWSGI

Requirements:

    apt install apache2 uwsgi libapache2-mod-proxy-uwsgi uwsgi-plugin-python3
    a2enmod proxy proxy_http proxy_uwsgi alias headers deflate

To deploy using Apache2 and uWSGI, copy configuration file templates:

    # copy Apache2 config
    cp deploy/apache.conf /etc/apache2/sites-available/eche-api.conf
    ln -s /etc/apache2/sites-available/eche-api.conf /etc/apache2/sites-enabled/eche-api.conf
    # copy uWSGI config
    cp deploy/uwsgi.ini /etc/uwsgi/apps-available/eche-api.ini
    ln -s /etc/uwsgi/apps-available/eche-api.ini /etc/uwsgi/apps-enabled/eche-api.ini

NOTE: These config files are only templates, it will be necessary to adjust some paths and other parameters.

Once the config files are ready:

    # restart services
    service apache2 restart
    service uwsgi restart


---

_This project is a work in progress and is considered unstable._
