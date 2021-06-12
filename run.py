from flask import render_template, request, flash
from app import app

import controllers.controller_index
import controllers.controller_profile

app.run(host='0.0.0.0')
