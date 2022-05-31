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

## Development

### Built-in server

To use the built-in web server locally, in debug mode, execute the following commands:

    # first step can be skipped due to autodiscovery
    export FLASK_APP=app
    # debug mode ON
    export FLASK_ENV=development
    flask run

---

_This project is a work in progress and is considered unstable._
