
# Interface for Master Slave
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/repl/master\_slave.cpp

<div></div>

    mongo::replAllDead

- Used By:

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/restapi.cpp](../../../network/web\_server)
    - [src/mongo/s/d\_state.cpp](../../../sharding/sharding)

<div></div>

    mongo::DatabaseIgnorer::ignoreAt(std::string const&, mongo::OpTime const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::replInfo

- Used By:

    - [src/mongo/db/restapi.cpp](../../../network/web\_server)

<div></div>

    mongo::DatabaseIgnorer::doIgnoreUntilAfter(std::string const&, mongo::OpTime const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ReplSource::ReplSource(mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ReplSource::applyOperation(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)
