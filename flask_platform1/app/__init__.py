# -*- coding: utf-8 -*-

"""Top-level package for flask_platform1."""

__author__ = """Pavinee Kavanagh"""
__email__ = 'pavinee.kavanagh@ucdconnect.ie'
__version__ = '0.1.0'

from flask import Flask
app = Flask(__name__)
from app import views