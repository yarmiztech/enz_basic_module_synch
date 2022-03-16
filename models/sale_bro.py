import requests

from odoo import http
from odoo.http import request
from datetime import datetime
from num2words import num2words
import urllib.parse as urlparse
from urllib.parse import parse_qs
from odoo import models,fields,api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    basic_synch_partner = fields.Char(string="Basic Synch Partner")
