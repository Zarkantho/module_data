# legacy\_code

# Module Groups

-------------

# Group Description
Legacy files that should go away. Global class called "d" that used to contain a bunch of mongod  global variables.

# Files
- src/mongo/db/d\_globals.cpp   (mongod, tools)
- src/mongo/db/d\_globals.h   (mongod, tools)

# Interface

### src/mongo/db/d\_globals.cpp

<div></div>

    mongo::d

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

# Dependencies

### src/mongo/db/d\_globals.cpp

<div></div>

    mongo::BackgroundJob::BackgroundJob(bool)

- Provided By:

    - [src/mongo/util/background.cpp](../utilities)

<div></div>

    vtable for mongo::ClientCursorMonitor

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
