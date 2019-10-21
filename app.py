# -*- coding: utf-8 -*-​
from chalice import Chalice

app = Chalice(app_name='Chalice-Devfest-CodeLab')

# TODO
# Activate BluePrints Feature and register the slack one
# See https://chalice.readthedocs.io/en/latest/topics/blueprints.html


@app.route('/')
def index():
    return {'hello': 'world'}
