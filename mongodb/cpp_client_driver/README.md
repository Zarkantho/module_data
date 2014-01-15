# cpp\_client\_driver

# Module Groups

-------------

Stubs so that the client driver can build alone since our deps are screwed up. We have symbols  that are required by shared code that are very internal to the server, so if we didn't have these  files we'd either need to include the whole server (which we want to avoid) or the build wouldn't  successfully link.

- src/mongo/client/clientAndShell.cpp   (cppclientdriver)
- src/mongo/client/clientOnly-private.h
- src/mongo/client/clientOnly.cpp   (cppclientdriver)

-------------

Stubs to initialize the client driver when it is used standalone. Calls MONGO\_INITIALIZERs among  other things. Not built into the server.

- src/mongo/client/init.cpp   (cppclientdriver)
- src/mongo/client/init.h

-------------

The Core C++ Client Driver Library   who uses these, and why? maybe this description should be broken up into   some components, e.g. what exactly is a 'dbclient', a 'dbclientcursor'   and a 'syncclusterconnection' ?

- src/mongo/client/connpool.cpp   (cppclientdriver)
- src/mongo/client/connpool.h
- src/mongo/client/constants.h
- src/mongo/client/dbclient.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclient.h
- src/mongo/client/dbclient\_rs.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclient\_rs.h
- src/mongo/client/dbclient\_rs\_test.cpp   ()
- src/mongo/client/dbclientcursor.cpp   (mongod, tools, mongos)
- src/mongo/client/dbclientcursor.h
- src/mongo/client/dbclientinterface.h
- src/mongo/client/dbclientmockcursor.h
- src/mongo/client/scoped\_db\_conn\_test.cpp   ()
- src/mongo/client/syncclusterconnection.cpp   (cppclientdriver)
- src/mongo/client/syncclusterconnection.h

-------------

Legacy wire protocol in the client driver   what is the new equivalent, and where?

- src/mongo/db/dbmessage.cpp   (cppclientdriver)
- src/mongo/db/dbmessage.h

-------------

Utilities for keeping track of the data needed for getLastError (part of legacy wire protocol).

- src/mongo/db/lasterror.cpp   (cppclientdriver)
- src/mongo/db/lasterror.h

-------------

Examples of how to use the client driver that get built in the server

- src/mongo/client/examples/authTest.cpp   (cppclientdriver)
- src/mongo/client/examples/clientTest.cpp   (cppclientdriver)
- src/mongo/client/examples/first.cpp   (cppclientdriver)
- src/mongo/client/examples/httpClientTest.cpp   (cppclientdriver)
- src/mongo/client/examples/rs.cpp   (cppclientdriver)
- src/mongo/client/examples/second.cpp   (cppclientdriver)
- src/mongo/client/examples/tutorial.cpp   (cppclientdriver)
- src/mongo/client/examples/whereExample.cpp   (cppclientdriver)

-------------

Old performance testing utility. Builds the "mongoperf" binary.

- src/mongo/client/examples/mongoperf.cpp   (tools)

-------------

Macro hacks! Apparently we pollute the namespace with tons of crazy macros that cause problems  for consumers of the client driver if we leave them in. I guess users don't like it when we  redefine things like "malloc" and "verify" in their programs.

- src/mongo/client/export\_macros.h
- src/mongo/client/undef\_macros.h
- src/mongo/client/redef\_macros.h

-------------

More fun macros! MONGO\_likely and MONGO\_unlikely as well as LOG\_SOME, which only logs every once  in a while. w00! Party!

- src/mongo/server.h

-------------

Gridfs wrapper around the client driver.

- src/mongo/client/gridfs.cpp   (tools)
- src/mongo/client/gridfs.h

-------------

Cursor that represents a connection to a bunch of shards. You would think that this only makes  sense in mongos, but it turns out it's built into mongod for purposes of map reduce (the final  destination shard of a map reduce job uses this in the "mapreduce.shardedfinish" command).

- src/mongo/client/parallel.cpp   (mongod, tools, mongos)
- src/mongo/client/parallel.h

-------------

Hookup of client to sasl authentication. Only built in when user passes --use-sasl-client

- src/mongo/client/sasl\_client\_authenticate.cpp   (mongod, tools, mongos)
- src/mongo/client/sasl\_client\_authenticate.h
