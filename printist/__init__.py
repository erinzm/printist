from flask import Flask
from apis.printer import printer
from apis.files import files
import config

printist = Flask(__name__)
printist.config.from_object(config)

printist.register_blueprint(printer, url_prefix='/api')
printist.register_blueprint(files, url_prefix='/api')