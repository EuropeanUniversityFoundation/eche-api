# ECHE API

This repository contains the specification of the ECHE API, along with its documentation.

## Introduction

### What is the ECHE API?

The **ECHE API** is designed to expose the list of institutions holding the _Erasmus Charter for Higher Education_, as published by the European Commission, in a machine readable format.

## Installation

The main app is built with Flask and it requires Python 3.8+ to run. To start the virtual environment and install the required libraries, execute the following commands:

    # generate and activate a virtual environment
    python3 -m venv venv
    source venv/bin/activate
    # install required libraries
    pip install -r requirements.txt

In order to run the app, some preparatory steps are needed:

    # check the local settings
    cp echeapi/settings/default.py echeapi/settings/local.py
    nano echeapi/settings/local.py
    # create a database
    python echeapi/manage.py initialize
    # populate the database
    python echeapi/manage.py populate

## Development

### Built-in server

To use the built-in web server locally, in debug mode, execute the following commands:

    # first step can be skipped due to autodiscovery
    export FLASK_APP=echeapi
    # debug mode ON
    export FLASK_ENV=development
    flask run

Or:

    python echeapi/manage.py run


## Depoyment

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
