# Cpp Client Driver
Internal driver used by the MongoDB tools, the mongo shell, and cluster nodes to communicate with other nodes in the cluster.  The C++ driver that should be used by clients is at https://github.com/mongodb/mongo-cxx-driver.


-------------

## Replica Set Monitor
Code to manage and store the current state of a connection to a replica set.  It is designed to allow the state to be shared across multiple threads so that each thread in our connection pool does not need to make a network call to get the current replica set state

#### Files
- src/mongo/client/replica\_set\_monitor\_internal.h   (mongod, tools, mongos)
- src/mongo/client/replica\_set\_monitor.cpp   (mongod, tools, mongos)
- src/mongo/client/replica\_set\_monitor.h   (mongod, tools, mongos)
- src/mongo/client/replica\_set\_monitor\_test.cpp   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Client stubs
Stubs so that the client driver can build alone since our dependencies are not well defined. We have symbols that are required by shared code that are very internal to the server, so if we did not have these files we would either need to include the whole server (which we want to avoid) or the build would not successfully link.

#### Files
- src/mongo/client/clientAndShell.cpp   ()
- src/mongo/client/clientOnly-private.h   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Client Driver Initializers
Stubs to initialize the client driver when it is used standalone. Calls MONGO\_INITIALIZERs among  other things. Not built into the server.

#### Files
- src/mongo/client/init.h   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Cpp Driver Core
The Core C++ Client Driver Library

TODO: Split into smaller components and document

#### Files
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

## Config Servers Connection
Class to manage the connections to our config servers in a sharded setup.

#### Files
- src/mongo/client/syncclusterconnection.cpp   (mongod, tools, mongos)
- src/mongo/client/syncclusterconnection.h   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Connection Pool Options
Startup configuration for client side connection pools.

#### Files
- src/mongo/db/conn\_pool\_options.h   (mongod, tools, mongos)
- src/mongo/db/conn\_pool\_options.cpp   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Mongoperf
Old performance testing utility. Builds the "mongoperf" binary.  Not to be confused with mongo-perf.

#### Files
- src/mongo/client/examples/mongoperf.cpp   (tools)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Marcro Hacks
Macro hacks! Apparently we pollute the namespace with tons of crazy macros that cause problems  for consumers of the client driver if we leave them in. I guess users don't like it when we  redefine things like "malloc" and "verify" in their programs.

#### Files
- src/mongo/client/export\_macros.h   (mongod, tools, mongos)
- src/mongo/client/undef\_macros.h   (mongod, tools, mongos)
- src/mongo/client/redef\_macros.h   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Legacy Macros
More fun macros! MONGO\_likely and MONGO\_unlikely as well as LOG\_SOME, which only logs every once  in a while. w00! Party!

#### Files
- src/mongo/server.h   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Gridfs Driver
Gridfs wrapper around the client driver.

#### Files
- src/mongo/client/gridfs.cpp   (tools)
- src/mongo/client/gridfs.h   (tools)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Sasl Client Authentication
Hookup of client to sasl authentication.  The real meat of built in when user passes --use-sasl-client.  TODO: regenerate this data with --use-sasl-client to show the rest of the sasl related client driver files

#### Files
- src/mongo/client/sasl\_client\_authenticate.cpp   (mongod, tools, mongos)
- src/mongo/client/sasl\_client\_authenticate.h   (mongod, tools, mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)
