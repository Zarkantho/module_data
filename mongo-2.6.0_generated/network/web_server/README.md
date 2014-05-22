# Web Server
Database web server.  Handles various types of requests, such as rest and jsonp.  This is completely orthogonal to our wire protocol


-------------

## Web Server
Web access to the database, including rest, jsonp, and http.

#### Files
- [src/mongo/db/dbwebserver.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/dbwebserver.cpp)   (mongod, mongos)
- [src/mongo/db/dbwebserver.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/dbwebserver.h)   (mongod, tools, mongos)
- [src/mongo/db/restapi.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/restapi.cpp)   (mongod)
- [src/mongo/db/restapi.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/restapi.h)   (mongod)
- [src/mongo/db/clientlistplugin.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/clientlistplugin.cpp)   (mongod)
- [src/mongo/util/net/miniwebserver.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/net/miniwebserver.cpp)   (mongod, tools, mongos)
- [src/mongo/util/net/miniwebserver.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/util/net/miniwebserver.h)   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
