# -*- coding: utf-8 -*-

from flask import Flask

"""__name__ is set to the name of the module used 
Flask uses the loc of the module passed here as a starting point when need to 
load associated resources such as template files"""

app = Flask(__name__)

from app import routes