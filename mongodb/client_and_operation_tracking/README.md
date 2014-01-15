# client\_and\_operation\_tracking

# Module Groups

-------------

mongos's version of a "Client". This is the big bucket of global state. This ALSO has the  definition of Command::execCommand for mongos (the function that actually runs commands registered  using the Command class, which gets called whenever a query against the "$cmd" collection is made)

- src/mongo/s/s\_only.cpp   (mongos)

-------------

mongod's version of a "Client". This is the big bucket of global state.  There is also the concept of a "Context" that one can take at the beginning of an operation that  holds a subset of the global state. There is also a "ReadContext" and a "WriteContext which  take locks. These are all nested classes in "Client". It's a bizarre situation because  "client.h" contains the declaration of the class, but there are two different definitions. One in  "s\_only.cpp" for mongos, and one in "client.cpp" for mongod. This means that mongos files may  contain "client.h" and pass compile fine when using something in it, but then may fail link  because it happens to be something that's only defined in "client.cpp". I don't see any  definitions so far for "Context" in mongos, and a grep for "Client::WriteContext::WriteContext"  (the definition of the WriteContext constructor) only shows up in client.cpp, which is mongod  only.

- src/mongo/db/client.cpp   (mongod, tools)
- src/mongo/db/client.h

-------------

The current "operation" within the current "Client"

- src/mongo/db/curop-inl.h
- src/mongo/db/curop.cpp   (mongod, tools)
- src/mongo/db/curop.h
- src/mongo/db/curop\_test.cpp   ()

-------------

Functions to kill the current "operation"

- src/mongo/db/kill\_current\_op.cpp   (mongod, tools)
- src/mongo/db/kill\_current\_op.h

-------------

Helpers to check whether the current operation in the current client has been interrupted.

- src/mongo/db/interrupt\_status.h
- src/mongo/db/interrupt\_status\_mongod.cpp   (mongod, tools)
- src/mongo/db/interrupt\_status\_mongod.h
- src/mongo/s/interrupt\_status\_mongos.cpp   (mongos)
- src/mongo/s/interrupt\_status\_mongos.h

-------------

Base class for a Client on mongod and mongos: ClientBasic

- src/mongo/db/client\_basic.cpp   (mongod, tools, mongos)
- src/mongo/db/client\_basic.h

-------------

Seems to be the "mongos only" version of the "Client" class: ClientInfo Also inherits from ClientBasic

- src/mongo/s/client\_info.cpp   (mongos)
- src/mongo/s/client\_info.h

-------------

The database's internal concept of a cursor from a client

- src/mongo/db/clientcursor.cpp   (mongod, tools)
- src/mongo/db/clientcursor.h

-------------

Contains helper functions for running common operations against the local server. For example,  has findOne, ensureIndex, upsert, etc. which all just run the respective options on the server the  code is running on.

- src/mongo/db/dbhelpers.cpp   (mongod, tools)
- src/mongo/db/dbhelpers.h

-------------

Code to get a handle to the "system.profile" collection for a given Database

- src/mongo/db/introspect.cpp   (mongod, tools)
- src/mongo/db/introspect.h

-------------

Just an enum for different cursor time limit states.

- src/mongo/db/max\_time.h
