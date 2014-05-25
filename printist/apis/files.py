"""
Super basic CRUD filesystem
"""
import os
from flask import Blueprint, abort, jsonify, request
from werkzeug.utils import secure_filename
from ..util.verifile import allowed_file

files = Blueprint('files', __name__)

"""
Grab a list of *all* the filenames!
"""
@files.route('/file', methods=['GET'])
def _GET_files():
  return jsonify(os.listdir('./files'))

"""
Post a file up to the service
"""
@files.route('/file', methods=['POST'])
def _POST_file():
  f = request.files['file']
  if f and allowed_file(f.filename):
    filename = secure_filename(f.filename)
    f.save(os.path.join('./files', filename))
    return jsonify({'success': True}), 201
  return jsonify({'success': False}), 403

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