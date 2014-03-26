# Cpp Client Driver

# Module Groups

-------------

# Replica Set Monitor
Code to manage and store the current state of a connection to a replica set.  It is designed to allow the state to be shared across multiple threads so that each thread in our connection pool does not need to make a network call to get the current replica set state

## Files
- src/mongo/client/replica\_set\_monitor\_internal.h   (mongod, tools, mongos)
- src/mongo/client/replica\_set\_monitor.cpp   (mongod, tools, mongos)
- src/mongo/client/replica\_set\_monitor.h   (mongod, tools, mongos)
- src/mongo/client/replica\_set\_monitor\_test.cpp   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

# TODO: Name this group
Stubs so that the client driver can build alone since our deps are screwed up. We have symbols  that are required by shared code that are very internal to the server, so if we didn't have these  files we'd either need to include the whole server (which we want to avoid) or the build wouldn't  successfully link.

## Files
- src/mongo/client/clientAndShell.cpp   ()
- src/mongo/client/clientOnly-private.h   ()
- src/mongo/client/clientOnly.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

# Client Driver Initializers
Stubs to initialize the client driver when it is used standalone. Calls MONGO\_INITIALIZERs among  other things. Not built into the server.

## Files
- src/mongo/client/init.cpp   ()
- src/mongo/client/init.h   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

# TODO: Name this group
The Core C++ Client Driver Library   who uses these, and why? maybe this description should be broken up into   some components, e.g. what exactly is a 'dbclient', a 'dbclientcursor'   and a 'syncclusterconnection' ?

## Files
- src/mongo/client/connpool.cpp   (mongod, tools, mongos)
- src/mongo/client/connpool.h   (mongod, tools, mongos)
- src/mongo/client/constants.h   (mongod, tools, mongos)
- src/mongo/client/dbclient.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclient.h   ()
- src/mongo/client/dbclient\_rs.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclient\_rs.h   (mongod, tools, mongos)
- src/mongo/client/dbclient\_rs\_test.cpp   ()
- src/mongo/client/dbclientcursor.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclientcursor.h   (mongod, tools, mongos)
- src/mongo/client/dbclientinterface.h   (mongod, tools, mongos)
- src/mongo/client/dbclientmockcursor.h   (mongod, tools)
- src/mongo/client/scoped\_db\_conn\_test.cpp   ()

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

# Config Servers Connection
Class to manage the connections to our config servers in a sharded setup.

## Files
- src/mongo/client/syncclusterconnection.cpp   (mongod, tools, mongos)
- src/mongo/client/syncclusterconnection.h   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

# TODO: Name this group
Utilities for keeping track of the data needed for getLastError (part of legacy wire protocol).

## Files
- src/mongo/db/lasterror.cpp   (mongod, tools, mongos)
- src/mongo/db/lasterror.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

# TODO: Name this group
Examples of how to use the client driver that get built in the server

## Files
- src/mongo/client/examples/authTest.cpp   ()
- src/mongo/client/examples/clientTest.cpp   ()
- src/mongo/client/examples/first.cpp   ()
- src/mongo/client/examples/httpClientTest.cpp   ()
- src/mongo/client/examples/rs.cpp   ()
- src/mongo/client/examples/second.cpp   ()
- src/mongo/client/examples/tutorial.cpp   ()
- src/mongo/client/examples/whereExample.cpp   ()

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

# TODO: Name this group
Old performance testing utility. Builds the "mongoperf" binary.

## Files
- src/mongo/client/examples/mongoperf.cpp   (tools)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

# TODO: Name this group
Macro hacks! Apparently we pollute the namespace with tons of crazy macros that cause problems  for consumers of the client driver if we leave them in. I guess users don't like it when we  redefine things like "malloc" and "verify" in their programs.

## Files
- src/mongo/client/export\_macros.h   (mongod, tools, mongos)
- src/mongo/client/undef\_macros.h   (mongod, tools, mongos)
- src/mongo/client/redef\_macros.h   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

# TODO: Name this group
More fun macros! MONGO\_likely and MONGO\_unlikely as well as LOG\_SOME, which only logs every once  in a while. w00! Party!

## Files
- src/mongo/server.h   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

# TODO: Name this group
Gridfs wrapper around the client driver.

## Files
- src/mongo/client/gridfs.cpp   (tools)
- src/mongo/client/gridfs.h   (tools)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)

-------------

# TODO: Name this group
Cursor that represents a connection to a bunch of shards. You would think that this only makes  sense in mongos, but it turns out it's built into mongod for purposes of map reduce (the final  destination shard of a map reduce job uses this in the "mapreduce.shardedfinish" command).

## Files
- src/mongo/client/parallel.cpp   (mongod, tools, mongos)
- src/mongo/client/parallel.h   (mongod, tools, mongos)

#### [Interface](interface/11)

#### [Dependencies](dependencies/11)

-------------

# TODO: Name this group
Hookup of client to sasl authentication.  The real meat of built in when user passes --use-sasl-client.  TODO: regenerate this data with --use-sasl-client to show the rest of the sasl related client driver files

## Files
- src/mongo/client/sasl\_client\_authenticate.cpp   (mongod, tools, mongos)
- src/mongo/client/sasl\_client\_authenticate.h   (mongod, tools, mongos)

#### [Interface](interface/12)

#### [Dependencies](dependencies/12)
