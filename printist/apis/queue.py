from flask import Blueprint, abort, jsonify

queue = Blueprint('queue', __name__)

"""
Get currently queued parts
"""
@queue.route('/queue', methods=['GET'])
def _GET_queue():
  abort(501)

"""
Push a filename onto the queue
"""
@queue.route('/queue', methods=['POST'])
def _POST_queue():
  abort(501)

"""
Delete a part from the queue by its queueid
"""
@queue.route('/queue/<id:int>',  methods=['DELETE'])
def _DELETE_queue_part(idf):
  abort(501)

"""
Start the print queue
"""
@queue.route('/queue/print', methods=['POST'])
def _POST_queue_print():
  abort(501)

"""
Stop the print queue
"""
@queue.route('/queue/print', methods=['DELETE'])
def _DELETE_queue_print():
  abort(501)