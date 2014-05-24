from flask import Flask
from apis.printer import printer
import config

printist = Flask(__name__)
printist.config.from_object(config)

printist.register_blueprint(printer, url_prefix='/api')