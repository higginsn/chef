from flask import Flask

#config corresponds to the config.py file, while Config corresponds to the class Config
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
