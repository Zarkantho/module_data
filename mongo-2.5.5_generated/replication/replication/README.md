# replication

# Module Groups

-------------

# Group Description
Implementation of "resync" command

## Files
- src/mongo/db/repl/resync.cpp   (mongod, tools)

## [Interface](interface/0)

## [Dependencies](dependencies/0)

-------------

# Group Description
Legacy Master/Slave implementation

## Files
- src/mongo/db/repl/master\_slave.cpp   (mongod, tools)
- src/mongo/db/repl/master\_slave.h   (mongod, tools)

## [Interface](interface/1)

## [Dependencies](dependencies/1)

-------------

# Group Description
Code to do sync and inital sync.  Note that this is a complex class heirarchy, and the files do not map one to one with class definitions and implementation.  The sync thread is started and run in "rs\_sync.cpp".  It handles doing the initial sync if applicable, then tailing the oplog.

## Files
- src/mongo/db/repl/rs\_initialsync.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_sync.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_sync.h   (mongod, tools, mongos)
- src/mongo/db/repl/sync.cpp   (mongod, tools)
- src/mongo/db/repl/sync.h   (mongod, tools, mongos)

## [Interface](interface/2)

## [Dependencies](dependencies/2)

-------------

# Group Description
Threads that actually handle syncing the oplog from the sync source. This includes the thread that actually reads the data from the source as well as the thread that notifies the source of how far it read

## Files
- src/mongo/db/repl/bgsync.cpp   (mongod, tools)
- src/mongo/db/repl/bgsync.h   (mongod, tools)

## [Interface](interface/3)

## [Dependencies](dependencies/3)

-------------

# Group Description
Code to tell the sync source how far we have progressed in the oplog.  For new versions this is the "replSetUpdatePosition command, but for old versions this was a "ghost cursor" which would only be advanced when the batch had been processed

## Files
- src/mongo/db/repl/sync\_source\_feedback.cpp   (mongod, tools)
- src/mongo/db/repl/sync\_source\_feedback.h   (mongod, tools, mongos)

## [Interface](interface/4)

## [Dependencies](dependencies/4)

-------------

# Group Description
Class to handle the details of how we are querying the oplog.  The interface is something like the interface for a cursor.

## Files
- src/mongo/db/repl/oplogreader.cpp   (mongod, tools)
- src/mongo/db/repl/oplogreader.h   (mongod, tools, mongos)

## [Interface](interface/5)

## [Dependencies](dependencies/5)

-------------

# Group Description
Class to manage remote connections.  Contains only one connection per remote host, protected by a mutex.  Note that this also means only one thread can be contacting a given host at a time using this class.

## Files
- src/mongo/db/repl/connections.h   (mongod, tools, mongos)

## [Interface](interface/6)

## [Dependencies](dependencies/6)

-------------

# Group Description
Commands that are sent and recieved during election as well as implementation of some class methods related to elections.  Note that there is not a clear class separation between things related to elections and things not related to elections, so the method implementations in this file span multiple classes.

## Files
- src/mongo/db/repl/consensus.cpp   (mongod, tools)

## [Interface](interface/7)

## [Dependencies](dependencies/7)

-------------

# Group Description
Contains class holding all possible states of a replica set member. Also contains class defining the heartbeat information.

## Files
- src/mongo/db/repl/rs\_member.h   (mongod, tools, mongos)

## [Interface](interface/8)

## [Dependencies](dependencies/8)

-------------

# Group Description
The top level classes for replcation.  Contains the class representing an entire replica set as well as the class representing information about a node of a replica set.  Note that the header contains a mix of different classes.

## Files
- src/mongo/db/repl/rs.cpp   (mongod, tools)
- src/mongo/db/repl/rs.h   (mongod, tools, mongos)

## [Interface](interface/9)

## [Dependencies](dependencies/9)

-------------

# Group Description
Helpers to check in code whether this node is a "master", since there are things that we can only do if we are a master (primary).  Note that this is not the "isMaster" command.  That lives in replication\_server\_status.cpp

## Files
- src/mongo/db/repl/is\_master.h   (mongod, tools)

## [Interface](interface/10)

## [Dependencies](dependencies/10)

-------------

# Group Description
Global configuration options for replication from the command line.

## Files
- src/mongo/db/repl/replication\_server\_status.h   (mongod, tools)

## [Interface](interface/11)

## [Dependencies](dependencies/11)

-------------

# Group Description
Code to add replication information to the server status results. Also currently has the implementation of the "isMaster" command

## Files
- src/mongo/db/repl/replication\_server\_status.cpp   (mongod, tools)

## [Interface](interface/12)

## [Dependencies](dependencies/12)

-------------

# Group Description
HealthOptions class is not really used anywhere

## Files
- src/mongo/db/repl/health.h   (mongod, tools, mongos)

## [Interface](interface/13)

## [Dependencies](dependencies/13)

-------------

# Group Description
Grab bag of miscellaneous helpers that report the status of a replica set or replica set node.  Most of this could be pushed into other files more connected with the classes they come from

## Files
- src/mongo/db/repl/health.cpp   (mongod, tools)

## [Interface](interface/14)

## [Dependencies](dependencies/14)

-------------

# Group Description
Helpers to send a command to multiple servers in parallel and collect the results.  Used in the election process.

## Files
- src/mongo/db/repl/multicmd.h   (mongod, tools, mongos)

## [Interface](interface/15)

## [Dependencies](dependencies/15)

-------------

# Group Description
Thin layer on top of the main replica set class.  Seems to be intended to manage state transitions in a replica set.  It does things like look at the current state of our set to determine if the node should step down or try to elect ourself as primary.  This gets called by the heartbeat thread when a state change is detected.

## Files
- src/mongo/db/repl/manager.cpp   (mongod, tools)

## [Interface](interface/16)

## [Dependencies](dependencies/16)

-------------

# Group Description
Contains the replica set heartbeat command implementation as well as the task that actually sends the heartbeat commands to check the health of other nodes in the set.

## Files
- src/mongo/db/repl/heartbeat.cpp   (mongod, tools)

## [Interface](interface/17)

## [Dependencies](dependencies/17)

-------------

# Group Description
Entry point for starting up replication when we are initializing the server.  Will check whether we are using replication or master/slave and do the proper initialization

## Files
- src/mongo/db/repl/repl\_start.cpp   (mongod, tools)
- src/mongo/db/repl/repl\_start.h   (mongod, tools)

## [Interface](interface/18)

## [Dependencies](dependencies/18)

-------------

# Group Description
Class that manages the configuration of a replica set.  This is the static configuration in which changes are only really triggered by the user.  See the output of rs.conf(), which queries the current replica set configuration from the local database.

## Files
- src/mongo/db/repl/rs\_config.cpp   (mongod, tools)
- src/mongo/db/repl/rs\_config.h   (mongod, tools, mongos)

## [Interface](interface/19)

## [Dependencies](dependencies/19)

-------------

# Group Description
Free helper functions to create the oplog, log operations into the oplog and apply operations from the oplog.

## Files
- src/mongo/db/repl/oplog.cpp   (mongod, tools)
- src/mongo/db/repl/oplog.h   (mongod, tools)

## [Interface](interface/20)

## [Dependencies](dependencies/20)

-------------

# Group Description
Exceptions that can be thrown from replication code

## Files
- src/mongo/db/repl/rs\_exception.h   (mongod, tools, mongos)

## [Interface](interface/21)

## [Dependencies](dependencies/21)

-------------

# Group Description
Commands related to replica sets

## Files
- src/mongo/db/repl/replset\_commands.cpp   (mongod, tools)

## [Interface](interface/22)

## [Dependencies](dependencies/22)

-------------

# Group Description
Code to handle the web page that reports replica set information. See the database web server code for more details.

## Files
- src/mongo/db/repl/replset\_web\_handler.cpp   (mongod)

## [Interface](interface/23)

## [Dependencies](dependencies/23)

-------------

# Group Description
Code to check if we can read from this node.  Checks if we are the primary or slaveOk is true.

## Files
- src/mongo/db/repl/repl\_reads\_ok.cpp   (mongod, tools)
- src/mongo/db/repl/repl\_reads\_ok.h   (mongod, tools)

## [Interface](interface/24)

## [Dependencies](dependencies/24)

-------------

# Group Description
rs.initiate() (replSetInitiate) command

## Files
- src/mongo/db/repl/rs\_initiate.cpp   (mongod, tools)

## [Interface](interface/25)

## [Dependencies](dependencies/25)

-------------

# Group Description
Code to handle rollbacks when two nodes got different writes (in the case where two nodes thought they were primary for some period of time).

## Files
- src/mongo/db/repl/rs\_rollback.cpp   (mongod, tools)

## [Interface](interface/26)

## [Dependencies](dependencies/26)

-------------

# Group Description
Helpers to wait for the appropriate write concern

## Files
- src/mongo/db/write\_concern.cpp   (mongod, tools)
- src/mongo/db/write\_concern.h   (mongod, tools, mongos)

## [Interface](interface/27)

## [Dependencies](dependencies/27)

-------------

# Group Description
Actual meat of the waiting for write concern code

## Files
- src/mongo/db/repl/write\_concern.cpp   (mongod, tools)
- src/mongo/db/repl/write\_concern.h   (mongod, tools, mongos)

## [Interface](interface/28)

## [Dependencies](dependencies/28)

-------------

# Group Description
Helper to parse write concern options out of a BSONObj

## Files
- src/mongo/db/write\_concern\_options.cpp   (mongod, tools, mongos)
- src/mongo/db/write\_concern\_options.h   (mongod, tools, mongos)

## [Interface](interface/29)

## [Dependencies](dependencies/29)
