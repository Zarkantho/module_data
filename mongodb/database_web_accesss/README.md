# database\_web\_accesss

# Module Groups

-------------

# Group Description
Web access to the database, including rest, jsonp, and http.

# Files
- src/mongo/db/dbwebserver.cpp   (mongod, mongos)
- src/mongo/db/dbwebserver.h
- src/mongo/db/restapi.cpp   (mongod)
- src/mongo/db/restapi.h
- src/mongo/db/clientlistplugin.cpp   (mongod)
- src/mongo/util/net/miniwebserver.cpp   (mongod, tools, mongos)
- src/mongo/util/net/miniwebserver.h

# Interface

### src/mongo/db/dbwebserver.cpp

<div></div>

    mongo::webServerThread(mongo::AdminAccess const*)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::DbWebHandler::DbWebHandler(std::string const&, double, bool)

- Used By:

    - [src/mongo/db/repl/replset\_web\_handler.cpp](../replication)

<div></div>

    mongo::WebStatusPlugin::WebStatusPlugin(std::string const&, double, std::string const&)

- Used By:

    - [src/mongo/db/stats/snapshots\_webplugins.cpp](../utilities)

### src/mongo/db/restapi.cpp

<div></div>

    vtable for mongo::RestAdminAccess

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
