from flask import Flask
from flask import url_for

app = Flask(__name__)
app.config.from_object('config')

from app import views
