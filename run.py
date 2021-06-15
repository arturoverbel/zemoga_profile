from flask import render_template, request, flash
from app import app

import routing.api_profile
import routing.templates

app.run(host='0.0.0.0')
