from flask import Blueprint, abort, jsonify

printer = Blueprint('printer', __name__)


"""
Grab a full status report from the printer, and return as JSON.
Not implemented.
"""
@printer.route('/printer', methods=['GET'])
def _GET_printer():
  abort(501)
  
"""
Is the printer printing?
Not implemented.
"""
@printer.route('/printer/printing', methods=['GET'])
def _GET_printing():
  abort(501)

"""
Print a file (uploaded to server as user ?)
Not implemented.
"""
@printer.route('/printer/print', methods=['POST'])
def _POST_print():
  abort(501)

"""
Stop a running print.
Not implemented.
"""
@printer.route('/printer/print', methods=['POST'])
def _POST_stop():
  abort(501)

"""
Is there a lock?
"""
@printer.route('/printer/lock', methods=['GET'])
def _GET_lock():
  return jsonify(locked=False)

"""
Remove a lock
"""
@printer.route('/printer/lock', methods=['DELETE'])
def _DELETE_lock():
  abort(501)