Overview
========
- Tool made up of 3 main parts.
- 1) Database : MySQL Database with a table called "countries"
- 2) Server script : Script that runs within the DB Server , which perfoms SQL querries to the DB.
- 3) client end : Client script picks options, and sends a string over the network socket to a listening server. Server translates the string into an SQL query.
- Design obsifucates the SQL Server to external environment.

testing
=====
1) Unittests
-------------
- pytest is used to unit-test the client function which calls on all other functions and classes.No unittesting of server modules.

2) Integration testing
----------------------
- Workflow created in Jenkins server
- Workflow runs the unittest first and when all is good, integration tests next.
- Integration tests are done using Docker containers to simulate customers, who then run a client script with pre-defined data.

docker
=======
- A ready docker image built as per the Dockerfile attached.
- Docker images are created , script run and then destroyed, all within the ansible script, site.yml.

How to Use
==========
- Set environmental variables for that specific subshell i.e MYSQL_USER & MYSQL_PASSWORD
- Start the server with server.py


Author
======
254in61