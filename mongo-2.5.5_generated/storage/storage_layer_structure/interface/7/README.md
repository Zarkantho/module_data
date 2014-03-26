
# Interface for Collection Class
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/catalog/collection.cpp

<div></div>

    mongo::Collection::storageSize(int*, mongo::BSONArrayBuilder*) const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Collection::docFor(mongo::DiskLoc const&)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Collection::dataSize() const

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)

<div></div>

    mongo::Collection::getIterator(mongo::DiskLoc const&, bool, mongo::CollectionScanParams::Direction const&) const

- Used By:

    - [src/mongo/db/commands/rename\_collection.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/exec/collection\_scan.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::CompactOptions::toString() const

- Used By:

    - [src/mongo/db/commands/compact.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Collection::requiresIdIndex() const

- Used By:

    - [src/mongo/tools/admin.cpp](../../../tools/tools)

<div></div>

    mongo::Collection::isCapped() const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/compact.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/introspect.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/ops/delete.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/repl/sync.cpp](../../../replication/replication)
    - [src/mongo/db/commands/validate.cpp](../../../queries/database\_commands)

<div></div>

    mongo::Collection::insertDocument(mongo::DocWriter const*, bool)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)

<div></div>

    mongo::Collection::numRecords() const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../queries/indexing)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../replication/replication)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../replication/replication)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/ops/count.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../../../replication/replication)
    - [src/mongo/db/commands/test\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/introspect.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../network/write\_commands)
    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/repl/sync.cpp](../../../replication/replication)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::Collection::updateDocument(mongo::DiskLoc const&, mongo::BSONObj const&, bool, mongo::OpDebug*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::Collection::deleteDocument(mongo::DiskLoc const&, bool, bool, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/repltests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../../../queries/core\_query\_system)
