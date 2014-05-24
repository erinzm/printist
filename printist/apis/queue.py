from flask import Blueprint, abort, jsonify

queue = Blueprint('queue', __name__)