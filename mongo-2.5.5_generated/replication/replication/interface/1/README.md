
# Interface

### src/mongo/db/repl/master\_slave.cpp

<div></div>

    mongo::replAllDead

- Used By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../storage\_layer\_structure)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/restapi.cpp](../web\_server)
    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::DatabaseIgnorer::ignoreAt(std::string const&, mongo::OpTime const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::replInfo

- Used By:

    - [src/mongo/db/restapi.cpp](../web\_server)

<div></div>

    mongo::DatabaseIgnorer::doIgnoreUntilAfter(std::string const&, mongo::OpTime const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::ReplSource::ReplSource(mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<div></div>

    mongo::ReplSource::applyOperation(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
