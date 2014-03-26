
# Interface for Legacy Pdfile File
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/pdfile.cpp

<div></div>

    mongo::inDBRepair

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::dbSize(char const*)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::dropDatabase(std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::dbHolderUnchecked()

- Used By:

    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/db/client.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/introspect.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)

<div></div>

    mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/introspect.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)

<div></div>

    mongo::_deleteDataFiles(char const*)

- Used By:

    - [src/mongo/db/durop.cpp](../../../../storage/journaling)

<div></div>

    mongo::dropAllDatabasesExceptLocal()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/replication)

<div></div>

    mongo::repairDatabase(std::string, std::string&, bool, bool)

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
