
# Interface for Journaling Main
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/dur.cpp

<div></div>

    mongo::dur::Stats::S::_asCSV()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::dur::Stats::S::_asObj()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::dur::commitJob

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::dur::stats

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::dur::Stats::S::_CSVHeader()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::dur::Stats::S::reset()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::dur::DurableInterface::_impl

- Used By:

    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/fsync.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/structure/catalog/cap.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/extent.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/data\_files)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/structure/record\_store.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::dur::startup()

- Used By:

    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)

<div></div>

    mongo::dur::releasingWriteLock()

- Used By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../query\_and\_operation\_handling/concurrency)
