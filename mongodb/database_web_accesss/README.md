# database\_web\_accesss

# Module Groups

-------------

Web access to the database, including rest, jsonp, and http.

- src/mongo/db/dbwebserver.cpp   (mongod, mongos)
- src/mongo/db/dbwebserver.h
- src/mongo/db/restapi.cpp   (mongod)
- src/mongo/db/restapi.h
- src/mongo/db/clientlistplugin.cpp   (mongod)
- src/mongo/util/net/miniwebserver.cpp   (mongod, tools, mongos)
- src/mongo/util/net/miniwebserver.h

## Interface


### src/mongo/db/dbwebserver.cpp

<pre>mongo::webServerThread(mongo::AdminAccess const*)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::DbWebHandler::DbWebHandler(std::string const&, double, bool)</pre>

#### Used By:

- [src/mongo/db/repl/replset\_web\_handler.cpp](../replication)

<pre>mongo::WebStatusPlugin::WebStatusPlugin(std::string const&, double, std::string const&)</pre>

#### Used By:

- [src/mongo/db/stats/snapshots\_webplugins.cpp](../utilities)

### src/mongo/db/restapi.cpp

<pre>vtable for mongo::RestAdminAccess</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
