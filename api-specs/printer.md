Printer API
===========

* GET `/printer`: Get the full state of the printer
* GET `/printer/printing`: Return if the printer is printing, and if so, what?
* ~~GET `/printer/head/<head>/temp`: Get the temperature of the head~~
* ~~GET `/printer/bed/temp`: Get the temperature of the heated bed~~
* POST `/printer/print`: Print `file` in JSON request on printer.
* POST `/printer/print/stop`: Stop print.