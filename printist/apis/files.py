"""
Super basic CRUD filesystem
"""
from flask import Blueprint, abort, jsonify

files = Blueprint('files', __name__)

"""
Grab a list of *all* the filenames!
"""
@files.route('/file', methods=['GET'])
def _GET_files():
  abort(501)

"""
Post a file up to the service
"""
@files.route('/file', methods=['POST'])
def _POST_file():
  abort(501)

"""
Update a file
"""
@files.route('/file/<name>', methods=['PUT'])
def _PUT_file():
  abort(501)

"""
Delete a file
"""
@files.route('/file/<name>', methods=['DELETE'])
def _DELETE_file():
  abort(501)