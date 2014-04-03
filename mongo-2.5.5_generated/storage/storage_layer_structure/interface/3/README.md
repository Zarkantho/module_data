
# Interface for Index Catalog
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/catalog/index\_catalog.cpp

<div></div>

    mongo::IndexCatalog::findIndexByType(std::string const&, std::vector<mongo::IndexDescriptor*, std::allocator<mongo::IndexDescriptor*> >&) const

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/text.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/geo/haystack.cpp](../../../../queries/geo\_queries)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::IndexCatalog::getAndClearUnfinishedIndexes()

- Used By:

    - [src/mongo/db/index\_rebuilder.cpp](../../../../queries/indexing)

<div></div>

    mongo::IndexCatalog::haveIdIndex() const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/tools/admin.cpp](../../../../tools/tools)

<div></div>

    mongo::IndexCatalog::findIdIndex() const

- Used By:

    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::IndexCatalog::findIndexByName(mongo::StringData const&, bool) const

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::IndexCatalog::updateTTLSetting(mongo::IndexDescriptor const*, long long)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::IndexCatalog::numIndexesTotal() const

- Used By:

    - [src/mongo/db/commands/create\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../queries/indexing)

<div></div>

    mongo::IndexCatalog::findIndexByPrefix(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)

<div></div>

    mongo::IndexCatalog::ensureHaveIdIndex()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/replication)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::IndexCatalog::numIndexesReady() const

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::IndexCatalog::okToAddIndex(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/create\_indexes.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/geo/haystack.cpp](../../../../queries/geo\_queries)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/exec/distinct\_scan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::IndexCatalog::dropIndex(mongo::IndexDescriptor*)

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::IndexCatalog::IndexIterator::next()

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::IndexCatalog::IndexIterator::more()

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::IndexCatalog::IndexIterator::IndexIterator(mongo::IndexCatalog const*, bool)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/prefetch.cpp](../../../../storage/page\_fault\_utilities)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::IndexCatalog::_getAccessMethodName(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index\_legacy.cpp](../../../../queries/indexing)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool, mongo::IndexCatalog::ShutdownBehavior)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../queries/indexing)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/index\_builder.cpp](../../../../queries/indexing)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)

<div></div>

    mongo::IndexCatalog::findIndexByKeyPattern(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/ttl.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/stage\_builder.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/2d.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::IndexCatalog::dropAllIndexes(bool)

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../../queries/indexing)

<div></div>

    mongo::IndexCatalog::ok() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::IndexCatalog::fixIndexKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*) const

- Used By:

    - [src/mongo/db/query/idhack\_runner.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::IndexCatalog::isMultikey(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/index\_scan.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../../../../queries/core\_query\_system)

### src/mongo/db/catalog/index\_catalog\_entry.cpp

<div></div>

    mongo::IndexCatalogEntry::setMultikey()

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::IndexCatalogEntry::head() const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../../queries/indexing)

<div></div>

    mongo::IndexCatalogEntry::setHead(mongo::DiskLoc)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)

<div></div>

    mongo::IndexCatalogEntry::isReady() const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
