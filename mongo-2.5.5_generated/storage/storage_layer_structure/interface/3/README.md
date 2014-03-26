
# Interface

### src/mongo/db/catalog/index\_catalog.cpp

<div></div>

    mongo::IndexCatalog::findIndexByType(std::string const&, std::vector<mongo::IndexDescriptor*, std::allocator<mongo::IndexDescriptor*> >&) const

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../../../database\_commands)
    - [src/mongo/db/exec/text.cpp](../../../core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../../../core\_query\_system)
    - [src/mongo/db/geo/haystack.cpp](../../../geo\_queries)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../core\_query\_system)

<div></div>

    mongo::IndexCatalog::getAndClearUnfinishedIndexes()

- Used By:

    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)

<div></div>

    mongo::IndexCatalog::haveIdIndex() const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/tools/admin.cpp](../../../tools)

<div></div>

    mongo::IndexCatalog::findIdIndex() const

- Used By:

    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/dbtests/namespacetests.cpp](../../../unit\_tests)
    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/dbhash.cpp](../../../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)

<div></div>

    mongo::IndexCatalog::findIndexByName(mongo::StringData const&, bool) const

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)

<div></div>

    mongo::IndexCatalog::updateTTLSetting(mongo::IndexDescriptor const*, long long)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)

<div></div>

    mongo::IndexCatalog::numIndexesTotal() const

- Used By:

    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)

<div></div>

    mongo::IndexCatalog::findIndexByPrefix(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../../../sharding)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::IndexCatalog::ensureHaveIdIndex()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../replication)
    - [src/mongo/dbtests/repltests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../unit\_tests)

<div></div>

    mongo::IndexCatalog::numIndexesReady() const

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)

<div></div>

    mongo::IndexCatalog::okToAddIndex(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../../../core\_query\_system)
    - [src/mongo/db/geo/haystack.cpp](../../../geo\_queries)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/db/exec/index\_scan.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../../../core\_query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/db/exec/distinct\_scan.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/2d.cpp](../../../core\_query\_system)

<div></div>

    mongo::IndexCatalog::dropIndex(mongo::IndexDescriptor*)

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)

<div></div>

    mongo::IndexCatalog::IndexIterator::next()

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/db/query/get\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)

<div></div>

    mongo::IndexCatalog::IndexIterator::more()

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/db/query/get\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)

<div></div>

    mongo::IndexCatalog::IndexIterator::IndexIterator(mongo::IndexCatalog const*, bool)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/db/prefetch.cpp](../../../page\_fault\_utilities)
    - [src/mongo/db/query/get\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)

<div></div>

    mongo::IndexCatalog::_getAccessMethodName(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index\_legacy.cpp](../../../indexing)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool, mongo::IndexCatalog::ShutdownBehavior)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../../../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)

<div></div>

    mongo::IndexCatalog::findIndexByKeyPattern(mongo::BSONObj const&, bool) const

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../../../core\_query\_system)
    - [src/mongo/db/ttl.cpp](../../../indexing)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../core\_query\_system)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/db/query/stage\_builder.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../../../core\_query\_system)
    - [src/mongo/db/dbhelpers.cpp](../../../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../unit\_tests)
    - [src/mongo/db/exec/2d.cpp](../../../core\_query\_system)

<div></div>

    mongo::IndexCatalog::dropAllIndexes(bool)

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../../../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../../../indexing)

<div></div>

    mongo::IndexCatalog::ok() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../core\_query\_system)

<div></div>

    mongo::IndexCatalog::fixIndexKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*) const

- Used By:

    - [src/mongo/db/query/idhack\_runner.cpp](../../../core\_query\_system)

<div></div>

    mongo::IndexCatalog::isMultikey(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/index\_scan.cpp](../../../core\_query\_system)
    - [src/mongo/db/exec/count.cpp](../../../core\_query\_system)

### src/mongo/db/catalog/index\_catalog\_entry.cpp

<div></div>

    mongo::IndexCatalogEntry::setMultikey()

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)

<div></div>

    mongo::IndexCatalogEntry::head() const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../../../indexing)

<div></div>

    mongo::IndexCatalogEntry::setHead(mongo::DiskLoc)

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)

<div></div>

    mongo::IndexCatalogEntry::isReady() const

- Used By:

    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)
