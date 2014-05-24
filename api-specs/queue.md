Queue APIs
==========

* GET `/queue`: Get currently queued parts
* POST `/queue`: Enqueue a part by its filename
* DELETE `/queue/<name>`: Delete a queued part by its filename.
* POST `/queue/print`: Start the print queue
* DELETE `/queue/print`: Stop the print queue