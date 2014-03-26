
# Interface for TODO: Name this group
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/ops/count.cpp

<div></div>

    mongo::runCount(std::string const&, mongo::BSONObj const&, std::string&, int&)

- Used By:

    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::applySkipLimit(long long, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../sharding/sharding)

### src/mongo/db/ops/delete.cpp

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Used By:

    - [src/mongo/db/ttl.cpp](../../../queries/indexing)
    - [src/mongo/db/catalog/database.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../../../queries/client\_and\_operation\_tracking)

### src/mongo/db/ops/insert.cpp

<div></div>

    mongo::fixDocumentForInsert(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::userAllowedWriteNS(mongo::NamespaceString const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../../../network/write\_commands)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../queries/database\_commands)
    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::userAllowedWriteNS(mongo::StringData const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::userAllowedWriteNS(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)

### src/mongo/db/ops/update.cpp

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../replication/replication)
    - [src/mongo/db/dbhelpers.cpp](../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::applyUpdateOperators(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*, mongo::UpdateDriver*, mongo::CanonicalQuery*)

- Used By:

    - [src/mongo/db/instance.cpp](../../../storage/storage\_layer\_structure)
