# Replica Set State
Non persistent runtime state of a replica set.


-------------

## Replica Set Heartbeats
Contains the replica set heartbeat command implementation as well as the task that actually sends the heartbeat commands to check the health of other nodes in the set.

#### Files
- [src/mongo/db/repl/heartbeat.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/heartbeat.cpp)   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Heath Status Helpers
Grab bag of miscellaneous helpers that report the status of a replica set or replica set node.  Most of this could be pushed into other files more connected with the classes they come from

#### Files
- [src/mongo/db/repl/health.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/health.cpp)   (mongod, tools)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Dead Code
HealthOptions class is not really used anywhere

#### Files
- [src/mongo/db/repl/health.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/health.h)   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Top Level Replica Set Classes
The top level classes for replcation.  Contains the class representing an entire replica set as well as the class representing information about a node of a replica set.  Note that the header contains a mix of different classes.

#### Files
- [src/mongo/db/repl/rs.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/rs.cpp)   (mongod, tools)
- [src/mongo/db/repl/rs.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/rs.h)   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Master Check Helpers
Helpers to check in code whether this node is a "master", since there are things that we can only do if we are a master (primary).  Note that this is not the "isMaster" command.  That lives in replication\_server\_status.cpp

#### Files
- [src/mongo/db/repl/is\_master.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/is_master.h)   (mongod, tools)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Replication Server Status Section
Code to add replication information to the server status results. Also currently has the implementation of the "isMaster" command

#### Files
- [src/mongo/db/repl/replication\_server\_status.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/replication_server_status.cpp)   (mongod, tools)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## State Transition Manager
Thin layer on top of the main replica set class.  Seems to be intended to manage state transitions in a replica set.  It does things like look at the current state of our set to determine if the node should step down or try to elect ourself as primary.  This gets called by the heartbeat thread when a state change is detected.

#### Files
- [src/mongo/db/repl/manager.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/manager.cpp)   (mongod, tools)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Reads Allowed
Code to check if we can read from this node.  Checks if we are the primary or slaveOk is true.

#### Files
- [src/mongo/db/repl/repl\_reads\_ok.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/repl_reads_ok.cpp)   (mongod, tools)
- [src/mongo/db/repl/repl\_reads\_ok.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/repl_reads_ok.h)   (mongod, tools)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Member State Information
Contains class holding all possible states of a replica set member. Also contains class defining the heartbeat information.

#### Files
- [src/mongo/db/repl/rs\_member.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/repl/rs_member.h)   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)
