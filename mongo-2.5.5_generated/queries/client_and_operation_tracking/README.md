# Client And Operation Tracking


-------------

## Mongos Specific Client State
mongos version of a "Client". This is the big bucket of global state.  This ALSO has the definition of "Command::execCommand" for mongos (the function that actually runs commands registered using the Command class, which gets called whenever a query against the "$cmd" collection is made)

#### Files
- src/mongo/s/s\_only.cpp   (mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Mongod Client State Implementation
mongod version of a "Client". This is the big bucket of global state.  There is also the concept of a "Context" that one can take at the beginning of an operation that holds a subset of the global state. There is also a "ReadContext" and a "WriteContext" which take locks. These are all nested classes in "Client". It is a bizarre situation because "client.h" contains the declaration of the class, but there are two different definitions. One in "s\_only.cpp" for mongos, and one in "client.cpp" for mongod. This means that mongos files may contain "client.h" and pass compile fine when using something in it, but then may fail link because it happens to be something that is only defined in "client.cpp". I do not see any definitions so far for "Context" in mongos, and a grep for "Client::WriteContext::WriteContext" (the definition of the WriteContext constructor) only shows up in client.cpp, which is mongod only.

#### Files
- src/mongo/db/client.cpp   (mongod, tools)
- src/mongo/db/client.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Current Operation
The current "operation" within the current "Client"

#### Files
- src/mongo/db/curop-inl.h   (mongod, tools, mongos)
- src/mongo/db/curop.cpp   (mongod, tools)
- src/mongo/db/curop.h   (mongod, tools, mongos)
- src/mongo/db/curop\_test.cpp   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Kill Current Operation
Functions to kill the current "operation"

#### Files
- src/mongo/db/kill\_current\_op.cpp   (mongod, tools)
- src/mongo/db/kill\_current\_op.h   (mongod, tools)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Interupt Status Checks
Helpers to check whether the current operation in the current client has been interrupted.

#### Files
- src/mongo/db/interrupt\_status.h   (mongod, tools, mongos)
- src/mongo/db/interrupt\_status\_mongod.cpp   (mongod, tools)
- src/mongo/db/interrupt\_status\_mongod.h   (mongod, tools)
- src/mongo/s/interrupt\_status\_mongos.cpp   (mongos)
- src/mongo/s/interrupt\_status\_mongos.h   (mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Shared Client State Interface
Base class for a Client on mongod and mongos: ClientBasic

#### Files
- src/mongo/db/client\_basic.cpp   (mongod, tools, mongos)
- src/mongo/db/client\_basic.h   (mongod, tools, mongos)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Mongos Client State Implementation
Seems to be the "mongos version" of the "Client" class which inherits from "ClientBasic".  see ClientInfo in s\_only.cpp for more "mongos only" client state.  That class also inherits from ClientBasic

#### Files
- src/mongo/s/client\_info.cpp   (mongos)
- src/mongo/s/client\_info.h   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Client Cursor
The internal representation of a cursor from a client

#### Files
- src/mongo/db/clientcursor.cpp   (mongod, tools)
- src/mongo/db/clientcursor.h   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Legacy Local Access Helpers
Contains helper functions for running common operations against the local server. For example, has findOne, ensureIndex, upsert, etc. which all just run the respective operations on the server the code is running on.

#### Files
- src/mongo/db/dbhelpers.cpp   (mongod, tools)
- src/mongo/db/dbhelpers.h   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## System Profiler
Code to get a handle to the "system.profile" collection for a given Database

#### Files
- src/mongo/db/introspect.cpp   (mongod, tools)
- src/mongo/db/introspect.h   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Cursor Time Limit Special States
Just an enum for different cursor time limit values that have a special meaning, such as "-1" for "no timeout".

#### Files
- src/mongo/db/max\_time.h   (mongos)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)
