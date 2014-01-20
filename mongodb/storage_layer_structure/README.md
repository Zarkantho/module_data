# storage\_layer\_structure

# Module Groups

-------------

# Group Description
Helper to manage strings that look like "<db>.<collection>"

# Files
- src/mongo/db/namespace\_string-inl.h
- src/mongo/db/namespace\_string.h
- src/mongo/db/namespace\_string\_test.cpp   ()

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/namespace\_string\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::TestAssertion(char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

-------------

# Group Description
Files containing the structural metadata about the databases/data files/collections/indexes.  TODO: Add more details here about the relationships between these files.

# Files
- src/mongo/db/cap.cpp   (mongod, tools)
- src/mongo/db/catalog/collection.cpp
- src/mongo/db/catalog/collection.h
- src/mongo/db/catalog/collection\_info\_cache.cpp
- src/mongo/db/catalog/collection\_info\_cache.h
- src/mongo/db/catalog/database.cpp
- src/mongo/db/catalog/database.h
- src/mongo/db/catalog/database\_holder.cpp
- src/mongo/db/catalog/database\_holder.h
- src/mongo/db/catalog/index\_catalog.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_catalog.h
- src/mongo/db/catalog/index\_catalog\_entry.cpp
- src/mongo/db/catalog/index\_catalog\_entry.h
- src/mongo/db/catalog/index\_create.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_create.h
- src/mongo/db/storage\_options.cpp   (mongod, tools)
- src/mongo/db/storage\_options.h
- src/mongo/db/structure/btree/btree.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btree.h
- src/mongo/db/structure/btree/btree\_stats.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btree\_stats.h
- src/mongo/db/structure/btree/btreebuilder.cpp   (mongod, tools)
- src/mongo/db/structure/btree/btreebuilder.h
- src/mongo/db/structure/btree/key.cpp   (mongod, tools)
- src/mongo/db/structure/btree/key.h
- src/mongo/db/structure/catalog/index\_details.cpp
- src/mongo/db/structure/catalog/index\_details.h
- src/mongo/db/structure/catalog/namespace-inl.h
- src/mongo/db/structure/catalog/namespace.cpp
- src/mongo/db/structure/catalog/namespace.h
- src/mongo/db/structure/catalog/namespace\_details-inl.h
- src/mongo/db/structure/catalog/namespace\_details.cpp
- src/mongo/db/structure/catalog/namespace\_details.h
- src/mongo/db/structure/catalog/namespace\_index.cpp
- src/mongo/db/structure/catalog/namespace\_index.h
- src/mongo/db/structure/catalog/namespace\_test.cpp
- src/mongo/db/structure/collection\_compact.cpp
- src/mongo/db/structure/collection\_iterator.cpp   (mongod, tools)
- src/mongo/db/structure/collection\_iterator.h
- src/mongo/db/structure/record\_store.cpp   (mongod, tools)
- src/mongo/db/structure/record\_store.h

# Interface

### src/mongo/db/cap.cpp

<div></div>

    mongo::NamespaceDetails::cappedAlloc(mongo::StringData const&, int)

- Used By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::NamespaceDetails::cappedTruncateAfter(char const*, mongo::DiskLoc, bool)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::emptyCappedCollection(char const*)

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)

<div></div>

    mongo::NamespaceDetails::cappedCheckMigrate()

- Used By:

    - src/mongo/db/catalog/ondisk/namespace\_index.cpp

<div></div>

    mongo::NamespaceDetails::cappedFirstDeletedInCurExtent()

- Used By:

    - src/mongo/db/namespace\_details.cpp

### src/mongo/db/catalog/index\_catalog.cpp

<div></div>

    mongo::IndexCatalog::~IndexCatalog()

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::IndexCatalog::IndexBuildBlock::IndexBuildBlock(mongo::IndexCatalog*, mongo::StringData const&, mongo::DiskLoc const&)

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::IndexCatalog::IndexBuildBlock::~IndexBuildBlock()

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::IndexCatalog::findIndexByName(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::IndexCatalog::getDescriptor(int)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - src/mongo/db/structure/collection.cpp
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/db/exec/text.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::IndexCatalog::checkNoIndexConflicts(mongo::BSONObj const&)

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::IndexCatalog::findIndexByKeyPattern(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)

<div></div>

    mongo::IndexCatalog::numIndexesTotal() const

- Used By:

    - src/mongo/db/structure/collection.cpp
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::ensureHaveIdIndex()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - src/mongo/db/database.cpp

<div></div>

    mongo::IndexCatalog::numIndexesReady() const

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

<div></div>

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Used By:

    - src/mongo/db/structure/collection.cpp
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::IndexCatalog::dropIndex(int)

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::indexRecord(mongo::BSONObj const&, mongo::DiskLoc const&)

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::IndexCatalog::findIdIndex()

- Used By:

    - src/mongo/db/structure/collection.cpp
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::prepOneUnfinishedIndex()

- Used By:

    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

<div></div>

    mongo::IndexCatalog::markMultikey(mongo::IndexDescriptor const*, bool)

- Used By:

    - src/mongo/db/structure/btree/state.cpp

<div></div>

    mongo::IndexCatalog::IndexCatalog(mongo::Collection*, mongo::NamespaceDetails*)

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::IndexCatalog::findIndexByPrefix(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::IndexCatalog::blowAwayInProgressIndexEntries()

- Used By:

    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

<div></div>

    mongo::IndexCatalog::unindexRecord(mongo::BSONObj const&, mongo::DiskLoc const&, bool)

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::IndexCatalog::dropAllIndexes(bool)

- Used By:

    - src/mongo/db/compact.cpp
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - src/mongo/db/database.cpp

<div></div>

    mongo::IndexCatalog::ok() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::IndexCatalog::fixIndexKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::IndexCatalog::getBtreeBasedIndex(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - src/mongo/db/index/btree\_based\_builder.cpp
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)

<div></div>

    mongo::IndexCatalog::getBtreeIndex(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)

<div></div>

    mongo::IndexCatalog::IndexBuildBlock::success()

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool)

- Used By:

    - src/mongo/db/compact.cpp
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::IndexCatalog::_getAccessMethodName(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/index\_legacy.cpp](../indexing)
    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)

### src/mongo/db/storage\_options.cpp

<div></div>

    mongo::getJournalCommitInterval()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::setJournalCommitInterval(unsigned int)

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

<div></div>

    mongo::storageGlobalParams

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - src/mongo/db/database\_holder.cpp
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - src/mongo/db/database.cpp
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/repl/sync\_source\_feedback.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)
    - [src/mongo/tools/tool\_options.cpp](../tools)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/durop.cpp](../journaling)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/dbcommands\_admin.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - src/mongo/db/modules/subscription/src/snmp/snmp.cpp
    - [src/mongo/db/ops/count.cpp](../query\_system)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - src/mongo/db/structure/collection.cpp
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - src/mongo/db/compact.cpp
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - src/mongo/db/catalog/ondisk/namespace\_index.cpp
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

<div></div>

    mongo::isJournalingEnabled()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

### src/mongo/db/structure/btree/btree.cpp

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::bt_insert(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::wouldCreateDup(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::KeyV1 const&, mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::locate(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::wouldCreateDup(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::KeyBson const&, mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::locate(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::advanceTo(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::customLocate(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyBson const&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::unindex(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::bt_insert(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::addBucket(mongo::BtreeInMemoryState*)

- Used By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::findSingle(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::advance(mongo::DiskLoc const&, int&, int, char const*) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::addBucket(mongo::BtreeInMemoryState*)

- Used By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyV1 const&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::advanceTo(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::unindex(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::findSingle(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::customLocate(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V0>::advance(mongo::DiskLoc const&, int&, int, char const*) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

<div></div>

    mongo::BtreeBucket<mongo::BtreeData_V1>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

### src/mongo/db/structure/btree/btreebuilder.cpp

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::BtreeBuilder(bool, mongo::BtreeInMemoryState*)

- Used By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::BtreeBuilder(bool, mongo::BtreeInMemoryState*)

- Used By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::commit(bool)

- Used By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::addKey(mongo::BSONObj&, mongo::DiskLoc)

- Used By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V1>::addKey(mongo::BSONObj&, mongo::DiskLoc)

- Used By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::BtreeBuilder<mongo::BtreeData_V0>::commit(bool)

- Used By:

    - src/mongo/db/index/btree\_based\_builder.cpp

### src/mongo/db/structure/btree/key.cpp

<div></div>

    mongo::KeyV1::dataSize() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::KeyV1Owned::KeyV1Owned(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::KeyV1::woCompare(mongo::KeyV1 const&, mongo::Ordering const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::KeyV1::woEqual(mongo::KeyV1 const&) const

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::KeyV1::toBson() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::oldCompare(mongo::BSONObj const&, mongo::BSONObj const&, mongo::Ordering const&)

- Used By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::KeyBson::woCompare(mongo::KeyBson const&, mongo::Ordering const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

### src/mongo/db/structure/collection\_iterator.cpp

<div></div>

    mongo::CappedIterator::CappedIterator(mongo::Collection const*, mongo::DiskLoc const&, bool, mongo::CollectionScanParams::Direction const&)

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::FlatIterator::FlatIterator(mongo::Collection const*, mongo::DiskLoc const&, mongo::CollectionScanParams::Direction const&)

- Used By:

    - src/mongo/db/structure/collection.cpp

### src/mongo/db/structure/record\_store.cpp

<div></div>

    mongo::RecordStore::RecordStore(mongo::StringData const&)

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::RecordStore::init(mongo::NamespaceDetails*, mongo::ExtentManager*, bool)

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::RecordStore::insertRecord(char const*, int, int)

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::RecordStore::recordFor(mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

<div></div>

    mongo::RecordStore::insertRecord(mongo::DocWriter const*, int)

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::RecordStore::deleteRecord(mongo::DiskLoc const&)

- Used By:

    - src/mongo/db/structure/collection.cpp

# Dependencies

### src/mongo/db/cap.cpp

<div></div>

    mongo::NamespaceDetails::maybeComplain(mongo::StringData const&, int) const

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::Collection::deleteDocument(mongo::DiskLoc const&, bool, bool, mongo::BSONObj*)

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::NamespaceDetails::maxCappedDocs() const

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::NamespaceDetails::addDeletedRec(mongo::DeletedRecord*, mongo::DiskLoc)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::Helpers::findAll(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Collection::storageSize(int*, mongo::BSONArrayBuilder*) const

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ClientCursor::invalidate(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CollectionInfoCache::reset()

- Provided By:

    - src/mongo/db/structure/collection\_info\_cache.cpp

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/catalog/index\_catalog.cpp

<div></div>

    mongo::IndexNames::findPluginName(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::NamespaceDetails::swapIndex(int, int)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::FTSAccessMethod::FTSAccessMethod(mongo::BtreeInMemoryState*)

- Provided By:

    - [src/mongo/db/index/fts\_access\_method.cpp](../indexing)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::InternalRunner::InternalRunner(std::string const&, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../query\_system)

<div></div>

    mongo::HashAccessMethod::HashAccessMethod(mongo::BtreeInMemoryState*)

- Provided By:

    - [src/mongo/db/index/hash\_access\_method.cpp](../indexing)

<div></div>

    mongo::Collection::getExtentManager()

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::KeyPattern::isIdKeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/keypattern.cpp](../indexing)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::NamespaceDetails::clearSystemFlag(int)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IndexNames::GEO_2DSPHERE

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../query\_system)

<div></div>

    mongo::NamespaceDetails::findIndexByName(mongo::StringData const&, bool)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::ClientCursor::invalidate(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::IndexLegacy::postBuildHook(mongo::Collection*, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_legacy.cpp](../indexing)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IndexDetails::areIndexOptionsEquivalent(mongo::BSONObj const&) const

- Provided By:

    - src/mongo/db/storage/index\_details.cpp

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::NamespaceDetails::findIndexByKeyPattern(mongo::BSONObj const&, bool)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::IndexNames::HASHED

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::NamespaceDetails::_removeIndexFromMe(int)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../query\_system)

<div></div>

    mongo::CollectionInfoCache::clearQueryCache()

- Provided By:

    - src/mongo/db/structure/collection\_info\_cache.cpp

<div></div>

    mongo::NamespaceDetails::setIndexIsMultikey(int, bool)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::IndexNames::TEXT

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::HaystackAccessMethod::HaystackAccessMethod(mongo::BtreeInMemoryState*)

- Provided By:

    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::NamespaceIndex::add_ns(mongo::StringData const&, mongo::DiskLoc const&, bool)

- Provided By:

    - src/mongo/db/catalog/ondisk/namespace\_index.cpp

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Database::_clearCollectionCache(mongo::StringData const&)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::audit::logDropIndex(mongo::ClientBasic*, mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_indexes\_collections\_databases.cpp

<div></div>

    mongo::Collection::isCapped() const

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    typeinfo for mongo::BtreeBasedAccessMethod

- Provided By:

    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

<div></div>

    mongo::CollectionInfoCache::reset()

- Provided By:

    - src/mongo/db/structure/collection\_info\_cache.cpp

<div></div>

    mongo::TwoDAccessMethod::TwoDAccessMethod(mongo::BtreeInMemoryState*)

- Provided By:

    - [src/mongo/db/index/2d\_access\_method.cpp](../indexing)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::IndexLegacy::adjustIndexSpecObject(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/index\_legacy.cpp](../indexing)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BtreeAccessMethod::BtreeAccessMethod(mongo::BtreeInMemoryState*)

- Provided By:

    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

<div></div>

    mongo::Database::_initExtentFreeList()

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - src/mongo/db/catalog/ondisk/namespace\_index.cpp

<div></div>

    mongo::IndexNames::GEO_HAYSTACK

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::NamespaceDetails::setSystemFlag(int)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::Database::_addNamespaceToCatalog(mongo::StringData const&, mongo::BSONObj const*)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BtreeInMemoryState::BtreeInMemoryState(mongo::Collection*, mongo::IndexDescriptor const*, mongo::RecordStore*, mongo::IndexDetails*)

- Provided By:

    - src/mongo/db/structure/btree/state.cpp

<div></div>

    mongo::ErrorCodes::fromInt(int)

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/client\_build/mongo/base/error\_codes.cpp](../build\_generated\_files)

<div></div>

    mongo::NamespaceIndex::_init()

- Provided By:

    - src/mongo/db/catalog/ondisk/namespace\_index.cpp

<div></div>

    mongo::FieldRef::parse(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../update\_system)

<div></div>

    mongo::NamespaceDetails::getNextIndexDetails(char const*)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::IndexNames::GEO_2D

- Provided By:

    - [src/mongo/db/index\_names.cpp](../indexing)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForNs(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::FieldRef::getPart(unsigned long) const

- Provided By:

    - [src/mongo/db/field\_ref.cpp](../update\_system)

<div></div>

    mongo::S2AccessMethod::S2AccessMethod(mongo::BtreeInMemoryState*)

- Provided By:

    - [src/mongo/db/index/s2\_access\_method.cpp](../indexing)

<div></div>

    mongo::Database::_dropNS(mongo::StringData const&)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../query\_system)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BSONObj::isPrefixOf(mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

### src/mongo/db/catalog/index\_create.cpp

<div></div>

    mongo::ElapsedTracker::ElapsedTracker(int, int)

- Provided By:

    - [src/mongo/util/elapsed\_tracker.cpp](../utilities)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::InternalRunner::InternalRunner(std::string const&, mongo::PlanStage*, mongo::WorkingSet*)

- Provided By:

    - [src/mongo/db/query/internal\_runner.cpp](../query\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BackgroundOperation::BackgroundOperation(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::KeyPattern::isIdKeyPattern(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/keypattern.cpp](../indexing)

<div></div>

    mongo::Collection::numRecords() const

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ElapsedTracker::intervalHasElapsed()

- Provided By:

    - [src/mongo/util/elapsed\_tracker.cpp](../utilities)

<div></div>

    mongo::ProgressMeter::hit(int)

- Provided By:

    - [src/mongo/util/progress\_meter.cpp](../utilities)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Provided By:

    - [src/mongo/db/exec/working\_set.cpp](../query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    typeinfo for mongo::BackgroundOperation

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::BtreeBasedBuilder::fastBuildIndex(mongo::Collection*, mongo::BtreeInMemoryState*, bool)

- Provided By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::BtreeInMemoryState::setHead(mongo::DiskLoc)

- Provided By:

    - src/mongo/db/structure/btree/state.cpp

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::isWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::audit::logCreateIndex(mongo::ClientBasic*, mongo::BSONObj const*, mongo::StringData const&, mongo::StringData const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_indexes\_collections\_databases.cpp

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ClientCursor::deregisterRunner(mongo::Runner*)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Provided By:

    - [src/mongo/db/query/eof\_runner.cpp](../query\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BtreeBasedBuilder::makeEmptyIndex(mongo::BtreeInMemoryState*)

- Provided By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::Lock::nested()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ClientCursor::registerRunner(mongo::Runner*)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ClientCursor::suggestYieldMicros()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Provided By:

    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::this_thread::disable_interruption::~disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::BackgroundOperation::~BackgroundOperation()

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::CollectionInfoCache::reset()

- Provided By:

    - src/mongo/db/structure/collection\_info\_cache.cpp

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BtreeInMemoryState::head() const

- Provided By:

    - src/mongo/db/structure/btree/state.cpp

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - src/mongo/db/catalog/ondisk/namespace\_index.cpp

<div></div>

    boost::this_thread::interruption_point()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Collection::deleteDocument(mongo::DiskLoc const&, bool, bool, mongo::BSONObj*)

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::ElapsedTracker::resetLastTime()

- Provided By:

    - [src/mongo/util/elapsed\_tracker.cpp](../utilities)

<div></div>

    boost::this_thread::disable_interruption::disable_interruption()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::ClientCursor::staticYield(int, mongo::StringData const&, mongo::Record const*)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::detail::get_current_thread_data()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

### src/mongo/db/storage\_options.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    typeinfo for mongo::ServerParameter

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ExportedServerParameter<double>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ServerParameter::~ServerParameter()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ServerParameterSet::getGlobal()

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::ServerParameter::ServerParameter(mongo::ServerParameterSet*, std::string const&, bool, bool)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ExportedServerParameter<bool>::setFromString(std::string const&)

- Provided By:

    - [src/mongo/db/server\_parameters.cpp](../startup\_initialization)

### src/mongo/db/structure/btree/btree.cpp

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObj::jsonString(mongo::JsonStringFormat, int) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    vtable for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::wasserted(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::MsgAssertionException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Lock::somethingWriteLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::BtreeInMemoryState::setHead(mongo::DiskLoc)

- Provided By:

    - src/mongo/db/structure/btree/state.cpp

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BtreeInMemoryState::head() const

- Provided By:

    - src/mongo/db/structure/btree/state.cpp

<div></div>

    mongo::BtreeIndexCursor::aboutToDeleteBucket(mongo::DiskLoc const&)

- Provided By:

    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

### src/mongo/db/structure/btree/btree\_stats.cpp

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::ServerStatusSection::ServerStatusSection(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::ProcessInfo::blockCheckSupported()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::~ProcessInfo()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::ProcessInfo(mongo::ProcessId)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/structure/btree/btreebuilder.cpp

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::BtreeInMemoryState::setHead(mongo::DiskLoc)

- Provided By:

    - src/mongo/db/structure/btree/state.cpp

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

### src/mongo/db/structure/btree/key.cpp

<div></div>

    mongo::StartupTest::~StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::Ordering const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::StartupTest::StartupTest()

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    typeinfo for mongo::StartupTest

- Provided By:

    - [src/mongo/util/startup\_test.cpp](../utilities)
    - [src/mongo/client/clientOnly.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BSONObj::woCompare(mongo::BSONObj const&, mongo::BSONObj const&, bool) const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::OID::init()

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

### src/mongo/db/structure/collection\_iterator.cpp

<div></div>

    mongo::NamespaceDetails::lastRecord(mongo::DiskLoc const&) const

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::NamespaceDetails::firstRecord(mongo::DiskLoc const&) const

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::Collection::getExtentManager() const

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

### src/mongo/db/structure/record\_store.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::NamespaceDetails::addDeletedRec(mongo::DeletedRecord*, mongo::DiskLoc)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::NamespaceDetails::alloc(mongo::StringData const&, int)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::NamespaceDetails::getRecordAllocationSize(int)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::NamespaceDetails::incrementStats(long long, long long)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, std::string const&, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

-------------

# Group Description
A DiskLoc is simply a file number and offset into the file for a db. You can think of this as an  "address" into our database's storage space.

# Files
- src/mongo/db/diskloc.h
- src/mongo/db/diskloc\_test.cpp   ()

# Interface
(not used outside this module)

# Dependencies

### src/mongo/db/diskloc\_test.cpp

<div></div>

    mongo::unittest::Test::tearDown()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    typeinfo for mongo::unittest::Test

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::~Test()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::ComparisonAssertion::ComparisonAssertion(char const*, char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::~TestAssertion()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::add(std::string const&, boost::function<void ()> const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::TestAssertion::fail(std::string const&) const

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::run()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Suite::getSuite(std::string const&)

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

<div></div>

    mongo::unittest::Test::setUp()

- Provided By:

    - [src/mongo/unittest/unittest.cpp](../unit\_tests)

-------------

# Group Description
Type of a DiskLoc invalidation.

# Files
- src/mongo/db/invalidation\_type.h

# Interface
(not used outside this module)

# Dependencies
(no dependencies outside this module)

-------------

# Group Description
A record is simply a "node" in a linked list. It contains "prev" and "next" offsets, as well as  the offset of the extent in the current file.

# Files
- src/mongo/db/storage/record.cpp   (mongod, tools)
- src/mongo/db/storage/record.h

# Interface

### src/mongo/db/storage/record.cpp

<div></div>

    mongo::DiskLoc::obj() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/exec/working\_set\_common.cpp](../query\_system)
    - [src/mongo/db/exec/oplogstart.cpp](../query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - src/mongo/db/storage/index\_details.cpp
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - src/mongo/db/structure/collection\_info\_cache.cpp
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - src/mongo/db/namespace\_details.cpp
    - src/mongo/db/compact.cpp
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - src/mongo/db/database.cpp
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/exec/text.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

<div></div>

    mongo::Record::touch(bool) const

- Used By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
    - [src/mongo/db/query/plan\_executor.cpp](../query\_system)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::Record::likelyInPhysicalMemory() const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::DiskLoc::rec() const

- Used By:

    - src/mongo/db/compact.cpp
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/exec/fetch.cpp](../query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../query\_system)
    - [src/mongo/db/exec/oplogstart.cpp](../query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/exec/2dcommon.cpp](../query\_system)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    mongo::Record::_accessing() const

- Used By:

    - src/mongo/db/compact.cpp
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - src/mongo/db/structure/collection.cpp
    - [src/mongo/db/exec/oplogstart.cpp](../query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - src/mongo/db/namespace\_details.cpp
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

<div></div>

    mongo::Record::MemoryTrackingEnabled

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::Record::accessed()

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::DiskLoc::drec() const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - src/mongo/db/namespace\_details.cpp
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::Record::likelyInPhysicalMemory(char const*)

- Used By:

    - [src/mongo/db/exec/fetch.cpp](../query\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../query\_system)

<div></div>

    mongo::DiskLoc::ext() const

- Used By:

    - src/mongo/db/compact.cpp
    - [src/mongo/db/exec/oplogstart.cpp](../query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - src/mongo/db/namespace\_details.cpp
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)

<div></div>

    mongo::DeletedRecord::_accessing() const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - src/mongo/db/namespace\_details.cpp

# Dependencies

### src/mongo/db/storage/record.cpp

<div></div>

    mongo::Client::ReadContext::ReadContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::ServerStatusSection::ServerStatusSection(std::string const&)

- Provided By:

    - [src/mongo/db/commands/server\_status.cpp](../database\_commands)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::ProcessInfo::blockInMemory(void const*)

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::Client::allowedToThrowPageFaultException() const

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::ProcessInfo::blockCheckSupported()

- Provided By:

    - [src/mongo/util/processinfo\_darwin.cpp](../utilities)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBRead::~DBRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::PageFaultException::PageFaultException(mongo::Record const*)

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::Listener::_timeTracker

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

-------------

# Group Description
An extent is a bucket of records. Extents themselves are in a kind of linked list, except instead  of offsets into a single datafile, their "prev" and "next" members are DiskLocs.

# Files
- src/mongo/db/storage/extent.cpp   (mongod, tools)
- src/mongo/db/storage/extent.h

# Interface

### src/mongo/db/storage/extent.cpp

<div></div>

    mongo::Extent::dump()

- Used By:

    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::Extent::initialSize(int)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - src/mongo/db/database.cpp

<div></div>

    mongo::Extent::followupSize(int, int)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

<div></div>

    mongo::Extent::markEmpty()

- Used By:

    - src/mongo/db/compact.cpp

<div></div>

    mongo::Extent::validates(mongo::DiskLoc, mongo::BSONArrayBuilder*)

- Used By:

    - src/mongo/db/compact.cpp
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

<div></div>

    mongo::Extent::maxSize()

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

# Dependencies

### src/mongo/db/storage/extent.cpp

<div></div>

    mongo::DataFile::maxSize()

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<unsigned int>(unsigned int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::operator<<(std::ostream&, mongo::StringData const&)

- Provided By:

    - [src/mongo/base/string\_data.cpp](../base\_utilites)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

-------------

# Group Description
Sits above an extent and has helper functions to manage them as a whole. This is the new way to  iterate extents.

# Files
- src/mongo/db/storage/extent\_manager.cpp   (mongod, tools)
- src/mongo/db/storage/extent\_manager.h

# Interface

### src/mongo/db/storage/extent\_manager.cpp

<div></div>

    mongo::ExtentManager::getExtent(mongo::DiskLoc const&, bool) const

- Used By:

    - src/mongo/db/compact.cpp
    - src/mongo/db/structure/collection.cpp
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

<div></div>

    mongo::ExtentManager::~ExtentManager()

- Used By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::ExtentManager::flushFiles(bool)

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<div></div>

    mongo::ExtentManager::init(mongo::NamespaceDetails*)

- Used By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::ExtentManager::recordFor(mongo::DiskLoc const&) const

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::ExtentManager::reset()

- Used By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::ExtentManager::freeExtents(mongo::DiskLoc, mongo::DiskLoc)

- Used By:

    - src/mongo/db/compact.cpp
    - src/mongo/db/database.cpp

<div></div>

    mongo::ExtentManager::init()

- Used By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::ExtentManager::ExtentManager(mongo::StringData const&, mongo::StringData const&, mongo::NamespaceDetails*, bool)

- Used By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::ExtentManager::quantizeExtentSize(int)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

<div></div>

    mongo::ExtentManager::getFile(int, int, bool)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::ExtentManager::getNextExtent(mongo::Extent*) const

- Used By:

    - [src/mongo/tools/dump.cpp](../tools)
    - src/mongo/db/structure/collection.cpp
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

<div></div>

    mongo::ExtentManager::increaseStorageSize(std::string const&, mongo::NamespaceDetails*, int, int)

- Used By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::ExtentManager::fileSize() const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::ExtentManager::getNextRecordInExtent(mongo::DiskLoc const&) const

- Used By:

    - src/mongo/db/compact.cpp
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

# Dependencies

### src/mongo/db/storage/extent\_manager.cpp

<div></div>

    mongo::DataFile::openExisting(char const*)

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::NamespaceDetails::setFirstExtent(mongo::DiskLoc)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DataFile::open(char const*, int, bool)

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::Lock::isWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::DataFile::flush(bool)

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::NamespaceDetails::setLastExtentSize(int)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::DataFile::allocExtentArea(int)

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::NamespaceDetails::setLastExtent(mongo::DiskLoc)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::DurableMappedFile::~DurableMappedFile()

- Provided By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::DataFile::maxSize()

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::DataFile::badOfs(int) const

- Provided By:

    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::NamespaceDetails::addDeletedRec(mongo::DeletedRecord*, mongo::DiskLoc)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::DurableMappedFile::DurableMappedFile()

- Provided By:

    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)

-------------

# Group Description
Utilities to clone entire collections and databases

# Files
- src/mongo/db/cloner.cpp   (mongod, tools)
- src/mongo/db/cloner.h

# Interface

### src/mongo/db/cloner.cpp

<div></div>

    mongo::Cloner::cloneFrom(mongo::Client::Context&, std::string const&, mongo::CloneOptions const&, std::string&, int*, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::Cloner::Cloner()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<div></div>

    mongo::Cloner::copyCollectionFromRemote(std::string const&, std::string const&, std::string&)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)

<div></div>

    mongo::Cloner::go(mongo::Client::Context&, std::string const&, mongo::CloneOptions const&, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*, std::string&, int*)

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

# Dependencies

### src/mongo/db/cloner.cpp

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ActionType::insert

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../build\_generated\_files)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Client::Context::_finishInit()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Query::snapshot()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Command::parseNsFullyQualified(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ConnectionString::parse(std::string const&, std::string&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::replAuthenticate(mongo::DBClientBase*)

- Provided By:

    - [src/mongo/db/repl/oplogreader.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::TempRelease::TempRelease()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    vtable for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionSet const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    boost::detail::set_tss_data(void const*, boost::shared_ptr<boost::detail::tss_cleanup_function>, void*, bool)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Query::toString() const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../base\_utilites)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::Client::WriteContext::WriteContext(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::ActionSet::addAction(mongo::ActionType const&)

- Provided By:

    - [src/mongo/db/auth/action\_set.cpp](../authentication)

<div></div>

    typeinfo for mongo::Command

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Lock::TempRelease::~TempRelease()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::fassertFailed(int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::detail::get_tss_data(void const*)

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::Command::Command(mongo::StringData, bool, mongo::StringData)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::ActionType::createIndex

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../build\_generated\_files)

<div></div>

    mongo::copydb::checkAuthForCopydbCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands/copydb\_common.cpp](../database\_commands)

<div></div>

    mongo::NE

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::Command::checkAuthForCommand(mongo::ClientBasic*, std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    vtable for mongo::DBClientConnection

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::legalClientSystemNS(mongo::StringData const&, bool)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::Lock::nested()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::isLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::NIN

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::DBClientConnection::_numConnections

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::getErrField(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ConnectionString::connect(std::string&, double) const

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Command::parseNs(std::string const&, mongo::BSONObj const&) const

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::HostAndPort::isSelf() const

- Provided By:

    - [src/mongo/db/commands/isself.cpp](../database\_commands)

<div></div>

    mongo::Command::redactForLogging(mongo::mutablebson::Document*)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Command::stopIndexBuilds(std::string const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/commands.cpp](../database\_commands)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
One of the very hairy, very old parts of the server. Contains code for the DBDirectClient, which  is an implementation of the "DBClientBase" class in the client driver. The DBDirectClient has the  same interface as the client driver, except that instead of connecting over the network it is just  doing operations on the local server behind the scenes.   This also has code for the "BSONElementManipulator which is what allows us to do in place  updates in the old code. It appears now that it is only used in updating the "expireAfterSeconds"  field for a document in a TTL index.   Also have random things like "getDatabaseNames" which just iteratest the db directory getting all  the names of the files there. Also has the version of "inShutdown" and "dbexit" for mongod.   clarify relationship between instance.cpp and the various ops/* (insert/update etc)

# Files
- src/mongo/db/instance.cpp   (mongod, tools)
- src/mongo/db/instance.h

# Interface

### src/mongo/db/instance.cpp

<div></div>

    typeinfo for mongo::DBDirectClient

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::exitCleanly(mongo::ExitCode)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::DBDirectClient::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)

<div></div>

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<div></div>

    mongo::DBDirectClient::_lookupAvailableOptions()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::lockFile

- Used By:

    - [src/mongo/dbtests/framework.cpp](../unit\_tests)

<div></div>

    mongo::_diaglog

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::mongoAbort(char const*)

- Used By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::BSONElementManipulator::SetNumber(double)

- Used By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    vtable for mongo::DBDirectClient

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/s/d\_merge.cpp](../sharding)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - src/mongo/db/modules/subscription/src/snmp/serverstatus\_client.cpp
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/btreebuildertests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jstests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/directclienttests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - src/mongo/db/database.cpp
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/gridfstest.cpp](../unit\_tests)
    - [src/mongo/dbtests/perf/perftest.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/commandtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/updatetests.cpp](../unit\_tests)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

<div></div>

    mongo::DBDirectClient::count(std::string const&, mongo::BSONObj const&, int, int, int)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_config.cpp](../replication)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::BSONElementManipulator::SetLong(long long)

- Used By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::DiagLog::flush()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::inShutdown()

- Used By:

    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/util/assert\_util.cpp](../utilities)
    - [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
    - [src/mongo/db/repl/bgsync.cpp](../replication)
    - [src/mongo/db/range\_deleter.cpp](../sharding)
    - [src/mongo/db/dur\_journal.cpp](../journaling)
    - [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
    - [src/mongo/db/repl/write\_concern.cpp](../replication)
    - [src/mongo/db/stats/snapshots.cpp](../utilities)
    - [src/mongo/util/concurrency/task.cpp](../utilities)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/s/writeback\_listener.cpp](../sharding)
    - src/mongo/client/distlock.cpp
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/balance.cpp](../sharding)
    - [src/mongo/util/net/listen.cpp](../network)
    - [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
    - [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
    - [src/mongo/s/shardconnection.cpp](../sharding)
    - [src/mongo/db/dur.cpp](../journaling)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/util/assert\_util.cpp](../utilities)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - src/mongo/db/modules/subscription/src/snmp/snmp.cpp
    - src/mongo/s/strategy\_shard.cpp
    - [src/mongo/util/concurrency/task.cpp](../utilities)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<div></div>

    mongo::assembleResponse(mongo::Message&, mongo::DbResponse&, mongo::HostAndPort const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - src/mongo/db/catalog/ondisk/namespace\_index.cpp
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::DiagLog::setLevel(int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    mongo::DBDirectClient::killCursor(long long)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::dbExecCommand

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<div></div>

    non-virtual thunk to mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::acquirePathLock(bool)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)

<div></div>

    mongo::BSONElementManipulator::initTimestamp()

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<div></div>

    mongo::replHasDatabases()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)

<div></div>

    mongo::killCurrentOp

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/write\_concern.cpp](../replication)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/extsort.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - src/mongo/db/compact.cpp
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/interrupt\_status\_mongod.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - src/mongo/db/index/btree\_based\_builder.cpp
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

<div></div>

    mongo::Database::closeDatabase(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - src/mongo/db/database\_holder.cpp

<div></div>

    mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    non-virtual thunk to mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<div></div>

    mongo::getDatabaseNames(std::vector<std::string, std::allocator<std::string> >&, std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - src/mongo/db/database.cpp
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/repl/rs.cpp](../replication)

# Dependencies

### src/mongo/db/instance.cpp

<div></div>

    boost::filesystem3::path_traits::dispatch(boost::filesystem3::directory_entry const&, std::string&, std::codecvt<wchar_t, char, __mbstate_t> const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::DBClientWithCommands::simpleCommand(std::string const&, mongo::BSONObj*, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::_unlockFsync()

- Provided By:

    - [src/mongo/db/commands/fsync.cpp](../database\_commands)

<div></div>

    mongo::DBClientWithCommands::setRunCommandHook(boost::function<void (mongo::BSONObjBuilder*)>)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::replAllDead

- Provided By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

<div></div>

    mongo::tlogLevel

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::operator<<(std::ostream&, mongo::ProcessId)

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::UpdateLifecycleImpl::UpdateLifecycleImpl(bool, mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    mongo::DBClientBase::update(std::string const&, mongo::Query, mongo::BSONObj, bool, bool)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::FileAllocator::get()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::Client::Context::inDB(std::string const&, std::string const&) const

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CurOp::~CurOp()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::DBWrite::~DBWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::DBClientWithCommands::reIndex(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    vtable for mongo::DBClientWithCommands

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::DBRead::DBRead(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::filesystem3::detail::dir_itr_close(void*&, void*&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Client::clients

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::rawOut(mongo::StringData const&)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::LastErrorHolder::startRequest(mongo::Message&, mongo::LastError*)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::OpTime::getLast(mongo::mutex::scoped_lock const&)

- Provided By:

    - [src/mongo/bson/optime.cpp](../bson)

<div></div>

    mongo::audit::logInsertAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::OpTime::waitForDifferent(unsigned int)

- Provided By:

    - [src/mongo/bson/optime.cpp](../bson)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::theReplSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::UpdateDriver::~UpdateDriver()

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::LastErrorHolder::get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::PageFaultRetryableSection::~PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::flushMyDirectory(boost::filesystem3::path const&)

- Provided By:

    - [src/mongo/util/paths.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*, mongo::UpdateDriver*)

- Provided By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

<div></div>

    mongo::ClientCursor::erase(long long)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::causedBy(std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientBase::ConnectionIdSequence

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::operator<<(std::ostream&, mongo::OID const&)

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Status mongo::parseNumberFromStringWithBase<long>(mongo::StringData const&, int, long*)

- Provided By:

    - [src/mongo/base/parse\_number.cpp](../base\_utilites)

<div></div>

    mongo::sleepmillis(long long)

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(std::string const&, bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::replSettings

- Provided By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)

<div></div>

    boost::filesystem3::detail::directory_iterator_increment(boost::filesystem3::directory_iterator&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::ReplSet::shutdown()

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    mongo::Database::~Database()

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::getGlobalFailPointRegistry()

- Provided By:

    - [src/mongo/util/fail\_point\_service.cpp](../utilities)

<div></div>

    mongo::Timer::_countsPerSecond

- Provided By:

    - [src/mongo/util/timer.cpp](../utilities)

<div></div>

    mongo::DBClientWithCommands::dropIndexes(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::resetIndexCache()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::audit::logShutdown(mongo::ClientBasic*)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_shutdown.cpp

<div></div>

    mongo::ClientCursor::eraseIfAuthorized(int, long long*)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    vtable for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::insert(std::string const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ClientBasic::getAuthorizationSession() const

- Provided By:

    - [src/mongo/db/client\_basic.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::FailPoint::FailPoint()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../utilities)

<div></div>

    mongo::OpTime::now(mongo::mutex::scoped_lock const&)

- Provided By:

    - [src/mongo/bson/optime.cpp](../bson)

<div></div>

    mongo::DBClientBase::INVALID_SOCK_CREATION_TIME

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::AuthorizationSession::startRequest()

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::nsGetDB(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::shardingState

- Provided By:

    - [src/mongo/s/d\_state.cpp](../sharding)

<div></div>

    mongo::ExceptionInfo::append(mongo::BSONObjBuilder&, char const*, char const*) const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::CurOp::reset(mongo::HostAndPort const&, int)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::newGetMore(char const*, int, long long, mongo::CurOp&, int, bool&, bool*)

- Provided By:

    - [src/mongo/db/query/new\_find.cpp](../query\_system)

<div></div>

    mongo::oplogCheckCloseDatabase(mongo::Database*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    boost::thread::start_thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::PageFaultException::touch()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::PageFaultRetryableSection::PageFaultRetryableSection()

- Provided By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)

<div></div>

    mongo::audit::logKillOpAuthzCheck(mongo::ClientBasic*, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::lockedForWriting()

- Provided By:

    - [src/mongo/db/commands/fsync.cpp](../database\_commands)

<div></div>

    mongo::FailPoint::slowShouldFailOpenBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../utilities)

<div></div>

    mongo::userAllowedWriteNS(mongo::NamespaceString const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../query\_system)

<div></div>

    mongo::GlobalInitializerRegisterer::GlobalInitializerRegisterer(std::string const&, boost::function<mongo::Status (mongo::InitializerContext*)> const&, std::vector<std::string, std::allocator<std::string> > const&, std::vector<std::string, std::allocator<std::string> > const&)

- Provided By:

    - [src/mongo/base/global\_initializer\_registerer.cpp](../startup\_initialization)

<div></div>

    mongo::BSONObjBuilder::numStrs

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::ActionType::inprog

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../build\_generated\_files)

<div></div>

    mongo::ClientCursor::invalidate(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::dur::haveJournalFiles(bool)

- Provided By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    mongo::ActionType::unlock

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../build\_generated\_files)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::ProcessId::getCurrent()

- Provided By:

    - [src/mongo/platform/process\_id.cpp](../utilities)

<div></div>

    mongo::replyToQuery(int, mongo::Message&, mongo::DbResponse&, mongo::BSONObj)

- Provided By:

    - [src/mongo/db/dbmessage.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::DBClientWithCommands::runCommand(std::string const&, mongo::BSONObj const&, mongo::BSONObj&, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    typeinfo for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::CurOp::info()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::detail::thread_data_base::~thread_data_base()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::audit::logUpdateAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, bool, mongo::ErrorCodes::Error)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::nsGetCollection(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBException::traceIfNeeded(mongo::DBException const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::userAllowedWriteNS(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../query\_system)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, mongo::BSONObj)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::replSet

- Provided By:

    - [src/mongo/db/repl/rs.cpp](../replication)

<div></div>

    vtable for mongo::DBException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::DBClientInterface::findOne(std::string const&, mongo::Query const&, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::filesystem3::path::wchar_t_codecvt_facet()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

<div></div>

    mongo::Lock::DBRead::~DBRead()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::ActionType::killop

- Provided By:

    - [build/darwin/cpppath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_include/libpath\_\_usr\_local\_Cellar\_openssl\_1.0.1e\_lib/ssl/mongo/db/auth/action\_type.cpp](../build\_generated\_files)

<div></div>

    mongo::DBClientWithCommands::logout(std::string const&, mongo::BSONObj&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::CurOp::ensureStarted()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::MessagingPort::closeAllSockets(unsigned int)

- Provided By:

    - [src/mongo/util/net/message\_port.cpp](../network)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::lastError

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    typeinfo for mongo::UserException

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::globalOpCounters

- Provided By:

    - [src/mongo/db/stats/counters.cpp](../utilities)

<div></div>

    mongo::validateBSON(char const*, unsigned long long)

- Provided By:

    - [src/mongo/bson/bson\_validate.cpp](../bson)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::BSONObjBuilder::numStrsReady

- Provided By:

    - [src/mongo/bson/oid.cpp](../bson)

<div></div>

    mongo::runCount(char const*, mongo::BSONObj const&, std::string&, int&)

- Provided By:

    - [src/mongo/db/ops/count.cpp](../query\_system)

<div></div>

    mongo::DBClientBase::remove(std::string const&, mongo::Query, bool)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::ListeningSockets::get()

- Provided By:

    - [src/mongo/util/net/listen.cpp](../network)

<div></div>

    mongo::fixDocumentForInsert(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/insert.cpp](../query\_system)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::KillCurrentOp::killAll()

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::dur::journalCleanup(bool)

- Provided By:

    - [src/mongo/db/dur\_journal.cpp](../journaling)

<div></div>

    typeinfo for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    vtable for mongo::UpdateLifecycleImpl

- Provided By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<div></div>

    mongo::dur::commitJob

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::AuthorizationSession::checkAuthForQuery(mongo::NamespaceString const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::KillCurrentOp::kill(mongo::AtomicUInt)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::checkAuthForInsert(mongo::NamespaceString const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::FailPoint::shouldFailCloseBlock()

- Provided By:

    - [src/mongo/util/fail\_point.cpp](../utilities)

<div></div>

    mongo::AuthorizationSession::checkAuthForGetMore(mongo::NamespaceString const&, long long)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::DBClientBase::getMore(std::string const&, long long, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::isW()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::DBException::toString() const

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::audit::logQueryAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::OpTime::m

- Provided By:

    - [src/mongo/bson/optime.cpp](../bson)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Client::shutdown()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::AuthorizationSession::isAuthorizedForActionsOnResource(mongo::ResourcePattern const&, mongo::ActionType)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::audit::logInProgAuthzCheck(mongo::ClientBasic*, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::Helpers::getSingleton(char const*, mongo::BSONObj&)

- Provided By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::OpDebug::reset()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBClientWithCommands::dropIndex(std::string const&, std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::UpdateDriver::UpdateDriver(mongo::UpdateDriver::Options const&)

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::AuthorizationSession::checkAuthForDelete(mongo::NamespaceString const&, mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::BSONObj::valid() const

- Provided By:

    - [src/mongo/db/jsobj.cpp](../bson)

<div></div>

    mongo::FailPointRegistry::addFailPoint(std::string const&, mongo::FailPoint*)

- Provided By:

    - [src/mongo/util/fail\_point\_registry.cpp](../utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::directory_iterator_construct(boost::filesystem3::directory_iterator&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::AuthorizationSession::checkAuthForUpdate(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, bool)

- Provided By:

    - [src/mongo/db/auth/authorization\_session.cpp](../authentication)

<div></div>

    mongo::readlocktry::readlocktry(int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::curTimeMicros64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::MongoFile::closeAllFiles(std::basic_stringstream<char, std::char_traits<char>, std::allocator<char> >&)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    boost::thread::~thread()

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::BSONObj const&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Matcher2::matches(mongo::BSONObj const&, mongo::MatchDetails*) const

- Provided By:

    - [src/mongo/db/matcher/matcher.cpp](../query\_system)

<div></div>

    mongo::profile(mongo::Client const&, int, mongo::CurOp&)

- Provided By:

    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::audit::logDeleteAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, mongo::BSONObj const&, mongo::ErrorCodes::Error)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::UpdateDriver::parse(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)

<div></div>

    mongo::readlocktry::~readlocktry()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::DBClientBase::query(boost::function<void (mongo::DBClientCursorBatchIterator&)>, std::string const&, mongo::Query, mongo::BSONObj const*, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::audit::logFsyncUnlockAuthzCheck(mongo::ClientBasic*, mongo::ErrorCodes::Error)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    boost::filesystem3::path::m_erase_redundant_separator(unsigned long)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::DBClientWithCommands::ensureIndex(std::string const&, mongo::BSONObj, bool, std::string const&, bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientBase::insert(std::string const&, mongo::BSONObj, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::_auth(mongo::BSONObj const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::DBClientWithCommands::getIndexes(std::string const&)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Lock::isReadLocked()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    typeinfo for mongo::DBClientBase

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    boost::filesystem3::path::m_append_separator_if_needed()

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::OpDebug::recordStats()

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::Lock::DBWrite::DBWrite(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::_handlePossibleShardedMessage(mongo::Message&, mongo::DbResponse*)

- Provided By:

    - [src/mongo/s/d\_logic.cpp](../sharding)

<div></div>

    vtable for boost::detail::thread_data_base

- Provided By:

    - [src/third\_party/boost/libs/thread/src/pthread/thread.cpp](../boost\_thread)

<div></div>

    mongo::DBClientWithCommands::_lookupAvailableOptions()

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::curTimeMillis64()

- Provided By:

    - [src/mongo/util/time\_support.cpp](../utilities)

<div></div>

    mongo::DBClientWithCommands::isMaster(bool&, mongo::BSONObj*)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::audit::logGetMoreAuthzCheck(mongo::ClientBasic*, mongo::NamespaceString const&, long long, mongo::ErrorCodes::Error)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp

<div></div>

    mongo::_makeStringVector(int, ...)

- Provided By:

    - [src/mongo/base/make\_string\_vector.cpp](../startup\_initialization)

<div></div>

    mongo::OpDebug::report(mongo::CurOp const&) const

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Client::clientsMutex

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::CurOp::CurOp(mongo::Client*, mongo::CurOp*)

- Provided By:

    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::DBClientWithCommands::getLastErrorDetailed(bool, bool, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::BackgroundOperation::inProgForDb(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::fromjson(char const*, int*)

- Provided By:

    - [src/mongo/db/json.cpp](../bson)

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::FileAllocator::waitUntilFinished() const

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::newRunQuery(mongo::Message&, mongo::QueryMessage&, mongo::CurOp&, mongo::Message&)

- Provided By:

    - [src/mongo/db/query/new\_find.cpp](../query\_system)

<div></div>

    mongo::LastErrorHolder::_get(bool)

- Provided By:

    - [src/mongo/db/lasterror.cpp](../cpp\_client\_driver)

<div></div>

    mongo::errnoWithDescription(int)

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Provided By:

    - [src/mongo/db/ops/delete.cpp](../query\_system)

<div></div>

    mongo::DBClientWithCommands::_countCmd(std::string const&, mongo::BSONObj const&, int, int, int)

- Provided By:

    - [src/mongo/client/dbclient.cpp](../cpp\_client\_driver)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
This is another really hairy, really old legacy file. At this point it's easier to just write out  all the functions in the interface than describe what it does. I believe "pdfile" is short for  "persistent data file". It contains a bunch of old legacy things to manipulate data files and  data file metadata.   Here are all the functions in pdfile.cpp that are currently used in the project.   mongo::inDBRepair  mongo::allocateSpaceForANewRecord(char const*, mongo::NamespaceDetails*, int, bool)  mongo::dbSize(char const*)  mongo::dropDatabase(std::string const&)  mongo::dbHolderUnchecked()  mongo::addRecordToRecListInExtent(mongo::Record*, mongo::DiskLoc)  mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)  mongo::\_deleteDataFiles(char const*)  mongo::dropAllDatabasesExceptLocal()  mongo::isValidNS(mongo::StringData const&)  mongo::repairDatabase(std::string, std::string&, bool, bool)

# Files
- src/mongo/db/pdfile.cpp   (mongod, tools)
- src/mongo/db/pdfile.h
- src/mongo/db/pdfile\_private.h
- src/mongo/db/pdfile\_version.h

# Interface

### src/mongo/db/pdfile.cpp

<div></div>

    mongo::inDBRepair

- Used By:

    - src/mongo/db/index/btree\_based\_builder.cpp

<div></div>

    mongo::allocateSpaceForANewRecord(char const*, mongo::NamespaceDetails*, int, bool)

- Used By:

    - src/mongo/db/compact.cpp
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::dbSize(char const*)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::dropDatabase(std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::dbHolderUnchecked()

- Used By:

    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)
    - src/mongo/db/database.cpp

<div></div>

    mongo::addRecordToRecListInExtent(mongo::Record*, mongo::DiskLoc)

- Used By:

    - src/mongo/db/compact.cpp
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<div></div>

    mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::_deleteDataFiles(char const*)

- Used By:

    - [src/mongo/db/durop.cpp](../journaling)

<div></div>

    mongo::dropAllDatabasesExceptLocal()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<div></div>

    mongo::isValidNS(mongo::StringData const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<div></div>

    mongo::repairDatabase(std::string, std::string&, bool, bool)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

# Dependencies

### src/mongo/db/pdfile.cpp

<div></div>

    mongo::FileAllocator::waitUntilFinished() const

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    mongo::NamespaceDetails::setMaxCappedDocs(long long)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::FileAllocator::get()

- Provided By:

    - [src/mongo/util/file\_allocator.cpp](../file\_allocation)

<div></div>

    boost::filesystem3::path::operator/=(char const*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::StaticObserver::_destroyingStatics

- Provided By:

    - [src/mongo/util/util.cpp](../utilities)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../utilities)

<div></div>

    mongo::getcurns

- Provided By:

    - [src/mongo/util/log.cpp](../logging\_system)

<div></div>

    mongo::BackgroundOperation::assertNoBgOpInProgForDb(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/background.cpp](../utilities)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Provided By:

    - [src/mongo/db/kill\_current\_op.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::Lock::GlobalWrite::GlobalWrite(bool, int)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::dur::DurableInterface::_impl

- Provided By:

    - [src/mongo/db/dur.cpp](../journaling)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogstreamBuilder const&)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::detail::rename(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Lock::assertWriteLocked(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    boost::filesystem3::detail::remove(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Provided By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    mongo::audit::logDropDatabase(mongo::ClientBasic*, mongo::StringData const&)

- Provided By:

    - src/mongo/db/modules/subscription/src/audit/audit\_indexes\_collections\_databases.cpp

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../logging\_system)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../utilities)

<div></div>

    boost::filesystem3::detail::status(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::path::operator/=(boost::filesystem3::path const&)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::File::freeSpace(std::string const&)

- Provided By:

    - [src/mongo/util/file.cpp](../file\_interface)

<div></div>

    boost::filesystem3::detail::create_directory(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::MongoFile::flushAll(bool)

- Provided By:

    - [src/mongo/util/mmap.cpp](../mmap)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    boost::filesystem3::detail::file_size(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::filesystem3::detail::remove_all(boost::filesystem3::path const&, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    mongo::Collection::increaseStorageSize(int, bool)

- Provided By:

    - src/mongo/db/structure/collection.cpp

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::NamespaceDetails::alloc(mongo::StringData const&, int)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::legalClientSystemNS(mongo::StringData const&, bool)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::Client::Context::~Context()

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

<div></div>

    boost::filesystem3::detail::copy_file(boost::filesystem3::path const&, boost::filesystem3::path const&, boost::filesystem3::copy_option::enum_type, boost::system::error_code*)

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/operations.cpp](../boost\_filesystem)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../client\_and\_operation\_tracking)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../utilities)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Provided By:

    - src/mongo/db/catalog/ondisk/namespace\_index.cpp

<div></div>

    mongo::NamespaceDetails::replaceUserFlags(int)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::Lock::GlobalWrite::~GlobalWrite()

- Provided By:

    - [src/mongo/db/d\_concurrency.cpp](../concurrency)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../logging\_system)

<div></div>

    boost::filesystem3::path::filename() const

- Provided By:

    - [src/third\_party/boost/libs/filesystem/v3/src/path.cpp](../boost\_filesystem)

<div></div>

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Provided By:

    - src/mongo/db/database.cpp

<div></div>

    mongo::NamespaceDetails::validMaxCappedDocs(long long*)

- Provided By:

    - src/mongo/db/namespace\_details.cpp

<div></div>

    mongo::serverGlobalParams

- Provided By:

    - [src/mongo/db/server\_options.cpp](../startup\_initialization)

<div></div>

    mongo::Client::Context::Context(std::string const&, std::string const&, bool)

- Provided By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
