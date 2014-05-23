Printer API
===========

* GET `/printer`: Get the full state of the printer
* ~~GET `/printer/head/<head>/temp`: Get the temperature of the head~~
* ~~GET `/printer/bed/temp`: Get the temperature of the heated bed~~
* POST `/printer/print`: Print `file` in JSON request on printer.