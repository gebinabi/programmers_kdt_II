from flask import Flask, render_template

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# import a module / component using its blueprint handler variable
from app.EDA.controllers import EDA

# Register blueprint(s)
app.register_blueprint(EDA)

