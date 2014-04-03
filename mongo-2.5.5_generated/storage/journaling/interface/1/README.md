
# Interface for TODO: Name this group
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

    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/replication)
    - [src/mongo/db/catalog/index\_catalog\_entry.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/catalog/database\_holder.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/replication)
    - [src/mongo/db/structure/catalog/namespace\_details.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/record\_store.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/ops/update.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/storage/extent.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/fsync.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/catalog/cap.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/replication)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)
    - [src/mongo/db/ops/delete.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/mmap\_file\_interface)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::dur::startup()

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../../../../tools/tools)
    - [src/mongo/dbtests/framework.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::dur::releasingWriteLock()

- Used By:

    - [src/mongo/db/d\_concurrency.cpp](../../../../queries/concurrency)

### src/mongo/db/dur\_journal.cpp

<div></div>

    mongo::dur::getJournalDir()

- Used By:

    - [src/mongo/db/dbcommands\_admin.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::dur::haveJournalFiles(bool)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::dur::journalCleanup(bool)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/storage/durable\_mapped\_file.cpp

<div></div>

    mongo::DurableMappedFile::create(std::string const&, unsigned long long&, bool)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/mmap\_file\_interface)

<div></div>

    mongo::DurableMappedFile::open(std::string const&, bool)

- Used By:

    - [src/mongo/db/structure/catalog/namespace\_index.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/storage/data\_file.cpp](../../../../storage/mmap\_file\_interface)

<div></div>

    mongo::DurableMappedFile::~DurableMappedFile()

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DurableMappedFile::DurableMappedFile()

- Used By:

    - [src/mongo/dbtests/mmaptests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/perftests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/storage/extent\_manager.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
