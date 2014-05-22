# Replication Initialization
Code to initialize the replication subsystem


-------------

## Replication Startup Entry Point
Entry point for starting up replication when we are initializing the server.  Will check whether we are using replication or master/slave and do the proper initialization

#### Files
- [src/mongo/db/repl/repl\_start.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/repl_start.cpp)   (mongod, tools)
- [src/mongo/db/repl/repl\_start.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/repl_start.h)   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
