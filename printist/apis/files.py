"""
Super basic CRUD filesystem
"""
import os
from flask import Blueprint, abort, jsonify, request, current_app
from werkzeug.utils import secure_filename
from ..util.verifile import allowed_file

files = Blueprint('files', __name__)

"""
Grab a list of *all* the filenames!
"""
@files.route('/file', methods=['GET'])
def _GET_files():
  return jsonify(files = os.listdir(current_app.config['FILE_UPLOAD_LOCATION']))

"""
Get a specific file
"""
@files.route('/file/<filename>')
def _GET_file(filename):
  f = open(os.path.join(current_app.config['FILE_UPLOAD_LOCATION'], secure_filename(filename)))
  return f.read()

"""
Post a file up to the service
"""
@files.route('/file', methods=['POST'])
def _POST_file():
  f = request.files['file']
  if f and allowed_file(f.filename, current_app.config['ALLOWED_EXTENSIONS']):
    filename = secure_filename(f.filename)
    f.save(os.path.join(current_app.config['FILE_UPLOAD_LOCATION'], filename))
    return jsonify({'success': True}), 201
  return jsonify({'success': False}), 403

"""
Update a file
"""
@files.route('/file/<filename>', methods=['PUT'])
def _PUT_file(filename):
  f = request.files['file']
  if f and allowed_file(f.filename, current_app.config['ALLOWED_EXTENSIONS']):
    filename = secure_filename(f.filename)
    f.save(os.path.join(current_app.config['FILE_UPLOAD_LOCATION'], filename))
    return jsonify({'success': True}), 201
  return jsonify({'success': False}), 403

"""
Delete a file
"""
@files.route('/file/<filename>', methods=['DELETE'])
def _DELETE_file(filename):
  os.remove(os.path.join(current_app.config['FILE_UPLOAD_LOCATION'], secure_filename(filename)))
  return jsonify({'success': True}), 204