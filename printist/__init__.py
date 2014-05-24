from flask import Flask
from apis.printer import printer

printist = Flask(__name__)

printist.register_blueprint(printer, url_prefix='/api')