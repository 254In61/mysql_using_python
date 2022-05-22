OVERVIEW
========
Project's end goal is to enable querries by devices to the MySQL DB.

DESIGN
======
server side
-----------
- DB is hosted by a MySQL Server.
- There's a python script, server.py, that is constantly "on" on the server side.
- Server script creates a server socket that listens to incoming connections and messages.
- Based on the in-string, server perfoms a MySQL DB query using the mysql-connector api to querry the server.
- Server sends back response in a JSON String format to the client.

client side
-----------
- Client runs a script client.py
- Client creates a socket and connects to the server.
- Based on the user input, client side creates a string with specific pattern and sends it over to the server.
- Server responds with a JSON string query results.

TESTING
========
- Test cases found in the tests/ directory.
- They are run from the run-unittest bash script.


AUTHOR
=======
Allan Maseghe

