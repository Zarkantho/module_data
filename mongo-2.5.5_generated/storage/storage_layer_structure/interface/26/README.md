
# Interface

### src/mongo/db/pdfile.cpp

<div></div>

    mongo::inDBRepair

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)

<div></div>

    mongo::dbSize(char const*)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::dropDatabase(std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::dbHolderUnchecked()

- Used By:

    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/db/client.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/restapi.cpp](../../../web\_server)

<div></div>

    mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/db/introspect.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::_deleteDataFiles(char const*)

- Used By:

    - [src/mongo/db/durop.cpp](../../../journaling)

<div></div>

    mongo::dropAllDatabasesExceptLocal()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication)

<div></div>

    mongo::repairDatabase(std::string, std::string&, bool, bool)

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
