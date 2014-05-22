# MongoDB Server Codebase Map
Categorization and documentation of the MongoDB server codebase.  This is a work in progress, and is by no means comprehensive.  Feel free to submit pull requests or suggestions.

NOTE:  This README and entire subtree is automatically generated.

* Build flags: --jobs 8 --mute --dbg=off --opt=off --ssl --cpppath /usr/local/Cellar/openssl/1.0.1e/include --libpath /usr/local/Cellar/openssl/1.0.1e/lib
* Build platform: macosx-10.8-intel
* Version hash: 1c1c76aeca21c5983dc178920f5052c298db616c
* Version branch: (no branch)
* Version tag: r2.6.0

## [Third Party](third\_party)
Third Party systems used in MongoDB

## [Tests](tests)
MongoDB Unit Tests and Unit Test Helpers

## [Mongo Shell](mongo\_shell)
The mongo shell

## [Javascript](javascript)
MongoDB Javascript support

## [Utilities](utilities)
General utilities that don not necessarily represent a specific layer of the database

## [Replication](replication)
Code related specifically to replication support in MongoDB.  See http://docs.mongodb.org/manual/replication/ for a high level description.

## [Sharding](sharding)
Code related specifically to sharding support in MongoDB.  See http://docs.mongodb.org/manual/sharding/ for a high level description.

## [BSON](bson)
MongoDB BSON support

## [Query And Operation Handling](query\_and\_operation\_handling)
Different operations that are supported in MongoDB, along with operation management code.

## [Core Query System](core\_query\_system)
Query execution framework.  Handles query parsing, optimization, and execution.

TODO: High level description of the phases of query execution.

## [Tools](tools)
MongoDB tools like mongodump and mongorestore

## [Process Management](process\_management)
Process management code.  Handles shutdown, startup, and configuration of a MongoDB process

## [Network](network)
The MongoDB network stack

## [Storage](storage)
Storage layer for MongoDB.  Includes structural metadata as well as code to access data files, metadata files, and the journal on disk

## [Dead Code](dead\_code)
Code to ignore.  Either dead or going away.

## [Security](security)
MongoDB security code

