File APIs
=========

* GET `/file`: return list of all uploaded files for this user(authkey) 
* GET `/file/<name>`: Pull the file down
* POST `/file`: push file up to the system for this user(authkey)
* PUT `/file/<name>`: replace file on system (!)
* DELETE `/file/<name>`: delete file on system (!)