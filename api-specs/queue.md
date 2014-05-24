Queue APIs
==========

* GET `/queue`: Get currently queued parts
* POST `/queue`: Enqueue a part by its filename
* DELETE `/queue/<id>`: Delete a queued part by its id.
* POST `/queue/print`: Start the print queue
* DELETE `/queue/print`: Stop the print queue