# encoding: utf-8

import ckan.lib.base as base
import ckan.lib.helpers as helpers
from flask import Blueprint
render = base.render

hn_theme = Blueprint(u'hn_theme', __name__)
