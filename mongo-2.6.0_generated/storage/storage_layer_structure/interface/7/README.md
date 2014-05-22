
# Interface for Collection Class
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/catalog/collection.cpp

<div></div>

    mongo::Collection::dataSize() const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Collection::numRecords() const

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/ops/count.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Collection::updateDocument(mongo::DiskLoc const&, mongo::BSONObj const&, bool, mongo::OpDebug*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool, mongo::PregeneratedKeys const*)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/pdfiletests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Collection::docFor(mongo::DiskLoc const&)

- Used By:

    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Collection::insertDocument(mongo::DocWriter const*, bool)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Collection::getIterator(mongo::DiskLoc const&, bool, mongo::CollectionScanParams::Direction const&) const

- Used By:

    - [src/mongo/db/exec/collection\_scan.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Collection::storageSize(int*, mongo::BSONArrayBuilder*) const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, mongo::MultiIndexBlock&)

- Used By:

    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)

<div></div>

    mongo::CompactOptions::toString() const

- Used By:

    - [src/mongo/db/commands/compact.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::Collection::isCapped() const

- Used By:

    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/repl/sync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/compact.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/introspect.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::Collection::deleteDocument(mongo::DiskLoc const&, bool, bool, mongo::BSONObj*)

- Used By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
