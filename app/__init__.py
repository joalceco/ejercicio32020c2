from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = "j089iwerf3j90fe90"

from app import routes