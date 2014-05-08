# Consensus
Module for handling consensus between nodes of a replica set to ensure that one and only one node is the primary node.


-------------

## Elections
Commands that are sent and recieved during election as well as implementation of some class methods related to elections.  Note that there is not a clear class separation between things related to elections and things not related to elections, so the method implementations in this file span multiple classes.

#### Files
- src/mongo/db/repl/consensus.cpp   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Parallel Command Dispatching
Helpers to send a command to multiple servers in parallel and collect the results.  Used in the election process.

#### Files
- src/mongo/db/repl/multicmd.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)
