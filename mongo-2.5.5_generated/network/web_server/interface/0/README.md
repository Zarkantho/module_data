
# Interface for Web Server
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/dbwebserver.cpp

<div></div>

    mongo::webServerThread(mongo::AdminAccess const*)

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::DbWebHandler::DbWebHandler(std::string const&, double, bool)

- Used By:

    - [src/mongo/db/repl/replset\_web\_handler.cpp](../../../../replication/replication\_web\_interface)

<div></div>

    mongo::WebStatusPlugin::WebStatusPlugin(std::string const&, double, std::string const&)

- Used By:

    - [src/mongo/db/stats/snapshots\_webplugins.cpp](../../../../utilities/utilities)

### src/mongo/db/restapi.cpp

<div></div>

    vtable for mongo::RestAdminAccess

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
