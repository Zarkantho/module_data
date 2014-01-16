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

-------------

# Group Description
Files containing the structural metadata about the databases/data files/collections/indexes.  TODO: Add more details here about the relationships between these files.

# Files
- src/mongo/db/namespace\_details-inl.h
- src/mongo/db/namespace\_details.cpp   (mongod, tools)
- src/mongo/db/namespace\_details.h
- src/mongo/db/database.cpp   (mongod, tools)
- src/mongo/db/database.h
- src/mongo/db/database\_holder.cpp   (mongod, tools)
- src/mongo/db/database\_holder.h
- src/mongo/db/storage/index\_details.cpp   (mongod, tools)
- src/mongo/db/storage/index\_details.h
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
- src/mongo/db/structure/btree/state-inl.h
- src/mongo/db/structure/btree/state.cpp   (mongod, tools)
- src/mongo/db/structure/btree/state.h
- src/mongo/db/structure/collection.cpp   (mongod, tools)
- src/mongo/db/structure/collection.h
- src/mongo/db/structure/collection\_info\_cache.cpp   (mongod, tools)
- src/mongo/db/structure/collection\_info\_cache.h
- src/mongo/db/structure/collection\_iterator.cpp   (mongod, tools)
- src/mongo/db/structure/collection\_iterator.h
- src/mongo/db/structure/record\_store.cpp   (mongod, tools)
- src/mongo/db/structure/record\_store.h
- src/mongo/db/cap.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_catalog.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_catalog.h
- src/mongo/db/catalog/index\_create.cpp   (mongod, tools)
- src/mongo/db/catalog/index\_create.h
- src/mongo/db/catalog/ondisk/namespace-inl.h
- src/mongo/db/catalog/ondisk/namespace.cpp   (mongod, tools, mongos)
- src/mongo/db/catalog/ondisk/namespace.h
- src/mongo/db/catalog/ondisk/namespace\_index.cpp   (mongod, tools)
- src/mongo/db/catalog/ondisk/namespace\_index.h
- src/mongo/db/catalog/ondisk/namespace\_test.cpp   ()

# Interface

### src/mongo/db/namespace\_details.cpp

    mongo::bucketSizes

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

    mongo::NamespaceDetails::quantizeAllocationSpace(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

    mongo::NamespaceDetails::alloc(mongo::StringData const&, int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

    mongo::NamespaceDetails::quantizePowerOf2AllocationSpace(int)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

    mongo::NamespaceDetails::maxCappedDocs() const

- Used By:

    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::NamespaceDetails::syncUserFlags(std::string const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/index\_legacy.cpp](../indexing)

    mongo::NamespaceDetails::setStats(long long, long long)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)

    mongo::NamespaceDetails::getRecordAllocationSize(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

    mongo::NamespaceDetails::setUserFlag(int)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/index\_legacy.cpp](../indexing)

    mongo::NamespaceDetails::findIndexByName(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

    mongo::NamespaceDetails::findIndexByKeyPattern(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::NamespaceDetails::orphanDeletedList()

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)

    mongo::NamespaceDetails::writingWithExtra()

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)

    mongo::NamespaceDetails::setPaddingFactor(double)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

    mongo::NamespaceDetails::findIndexByPrefix(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

    mongo::NamespaceDetails::updateTTLIndex(int, mongo::BSONElement const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::NamespaceDetails::setLastExtentSize(int)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)

    mongo::NamespaceDetails::incrementStats(long long, long long)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)

    mongo::NamespaceDetails::clearUserFlag(int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::NamespaceDetails::setIndexIsMultikey(int, bool)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

    mongo::legalClientSystemNS(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/ops/delete.cpp](../query\_system)

### src/mongo/db/database.cpp

    mongo::Database::clearTmpCollections()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs.cpp](../replication)

    mongo::Database::setProfilingLevel(int, std::string&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::Database::renameCollection(mongo::StringData const&, mongo::StringData const&, bool)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)

    mongo::Database::getOrCreateCollection(mongo::StringData const&)

- Used By:

    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

    mongo::Database::getCollection(mongo::StringData const&)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../query\_system)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/group.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/index\_builder.cpp](../indexing)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../query\_system)
    - [src/mongo/db/exec/text.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/exec/2d.cpp](../query\_system)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/tools/dump.cpp](../tools)

    mongo::Database::duplicateUncasedName(bool, std::string const&, std::string const&, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

    mongo::Database::dropCollection(mongo::StringData const&)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)

    mongo::Database::_initExtentFreeList()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::Database::Database(char const*, bool&, std::string const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

### src/mongo/db/database\_holder.cpp

    mongo::DatabaseHolder::closeAll(std::string const&, mongo::BSONObjBuilder&, bool)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::DatabaseHolder::getOrCreate(std::string const&, std::string const&, bool&)

- Used By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/storage\_options.cpp

    mongo::getJournalCommitInterval()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

    mongo::setJournalCommitInterval(unsigned int)

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

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
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/dur\_preplogbuffer.cpp](../journaling)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
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
    - [src/mongo/dbtests/mmaptests.cpp](../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_sync.cpp](../replication)
    - [src/mongo/db/dur\_recover.cpp](../journaling)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/dbeval.cpp](../database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/dbtests/framework\_options.cpp](../unit\_tests)

    mongo::isJournalingEnabled()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

### src/mongo/db/structure/btree/btree.cpp

    mongo::BtreeBucket<mongo::BtreeData_V0>::bt_insert(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::wouldCreateDup(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::KeyV1 const&, mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V0>::locate(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V0>::wouldCreateDup(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::KeyBson const&, mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::locate(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::advanceTo(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V0>::customLocate(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V0>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyBson const&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::unindex(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::bt_insert(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V0>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V0>::addBucket(mongo::BtreeInMemoryState*)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V0>::findSingle(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::advance(mongo::DiskLoc const&, int&, int, char const*) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::addBucket(mongo::BtreeInMemoryState*)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyV1 const&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V0>::advanceTo(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V0>::unindex(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::findSingle(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::customLocate(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V0>::advance(mongo::DiskLoc const&, int&, int, char const*) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

    mongo::BtreeBucket<mongo::BtreeData_V1>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)

### src/mongo/db/structure/btree/btreebuilder.cpp

    mongo::BtreeBuilder<mongo::BtreeData_V0>::BtreeBuilder(bool, mongo::BtreeInMemoryState*)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

    mongo::BtreeBuilder<mongo::BtreeData_V1>::BtreeBuilder(bool, mongo::BtreeInMemoryState*)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

    mongo::BtreeBuilder<mongo::BtreeData_V1>::commit(bool)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

    mongo::BtreeBuilder<mongo::BtreeData_V0>::addKey(mongo::BSONObj&, mongo::DiskLoc)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

    mongo::BtreeBuilder<mongo::BtreeData_V1>::addKey(mongo::BSONObj&, mongo::DiskLoc)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

    mongo::BtreeBuilder<mongo::BtreeData_V0>::commit(bool)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

### src/mongo/db/structure/btree/key.cpp

    mongo::KeyV1::dataSize() const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

    mongo::KeyV1Owned::KeyV1Owned(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

    mongo::KeyV1::woCompare(mongo::KeyV1 const&, mongo::Ordering const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

    mongo::KeyV1::woEqual(mongo::KeyV1 const&) const

- Used By:

    - [src/mongo/dbtests/perftests.cpp](../unit\_tests)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

    mongo::KeyV1::toBson() const

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

    mongo::oldCompare(mongo::BSONObj const&, mongo::BSONObj const&, mongo::Ordering const&)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

    mongo::KeyBson::woCompare(mongo::KeyBson const&, mongo::Ordering const&) const

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

### src/mongo/db/structure/btree/state.cpp

    mongo::BtreeInMemoryState::head() const

- Used By:

    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
    - [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)

    mongo::BtreeInMemoryState::setMultikey()

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

    mongo::BtreeInMemoryState::setHead(mongo::DiskLoc)

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

### src/mongo/db/structure/collection.cpp

    mongo::Collection::storageSize(int*, mongo::BSONArrayBuilder*) const

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

    mongo::Collection::docFor(mongo::DiskLoc const&)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

    mongo::Collection::dataSize() const

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::Collection::isCapped() const

- Used By:

    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/ops/delete.cpp](../query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

    mongo::Collection::insertDocument(mongo::DocWriter const*, bool)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

    mongo::Collection::getIterator(mongo::DiskLoc const&, bool, mongo::CollectionScanParams::Direction const&) const

- Used By:

    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)

    mongo::Collection::numRecords() const

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::Collection::insertDocument(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/ops/update.cpp](../query\_system)
    - [src/mongo/dbtests/extsorttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

    mongo::Collection::updateDocument(mongo::DiskLoc const&, mongo::BSONObj const&, bool, mongo::OpDebug*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

    mongo::Collection::deleteDocument(mongo::DiskLoc const&, bool, bool, mongo::BSONObj*)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)
    - [src/mongo/db/ops/delete.cpp](../query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

### src/mongo/db/structure/collection\_info\_cache.cpp

    mongo::CollectionInfoCache::computeIndexKeys()

- Used By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

    mongo::CollectionInfoCache::reset()

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)

    mongo::CollectionInfoCache::getPlanCache() const

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)

### src/mongo/db/structure/record\_store.cpp

    mongo::RecordStore::recordFor(mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

### src/mongo/db/cap.cpp

    mongo::NamespaceDetails::cappedTruncateAfter(char const*, mongo::DiskLoc, bool)

- Used By:

    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)

    mongo::NamespaceDetails::emptyCappedCollection(char const*)

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)

### src/mongo/db/catalog/index\_catalog.cpp

    mongo::IndexCatalog::IndexBuildBlock::IndexBuildBlock(mongo::IndexCatalog*, mongo::StringData const&, mongo::DiskLoc const&)

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

    mongo::IndexCatalog::IndexBuildBlock::~IndexBuildBlock()

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

    mongo::IndexCatalog::findIndexByName(mongo::StringData const&, bool)

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

    mongo::IndexCatalog::getDescriptor(int)

- Used By:

    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
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

    mongo::IndexCatalog::findIndexByKeyPattern(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/exec/s2near.cpp](../query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)

    mongo::IndexCatalog::numIndexesTotal() const

- Used By:

    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::IndexCatalog::ensureHaveIdIndex()

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../unit\_tests)

    mongo::IndexCatalog::numIndexesReady() const

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

    mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/db/exec/2d.cpp](../query\_system)

    mongo::IndexCatalog::dropIndex(int)

- Used By:

    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)

    mongo::IndexCatalog::findIdIndex()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)

    mongo::IndexCatalog::prepOneUnfinishedIndex()

- Used By:

    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

    mongo::IndexCatalog::findIndexByPrefix(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::IndexCatalog::blowAwayInProgressIndexEntries()

- Used By:

    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

    mongo::IndexCatalog::dropAllIndexes(bool)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

    mongo::IndexCatalog::ok() const

- Used By:

    - [src/mongo/db/ops/update.cpp](../query\_system)

    mongo::IndexCatalog::fixIndexKey(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

    mongo::IndexCatalog::getBtreeBasedIndex(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)

    mongo::IndexCatalog::getBtreeIndex(mongo::IndexDescriptor const*)

- Used By:

    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)

    mongo::IndexCatalog::IndexBuildBlock::success()

- Used By:

    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

    mongo::IndexCatalog::createIndex(mongo::BSONObj, bool)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
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

    mongo::IndexCatalog::_getAccessMethodName(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/index\_legacy.cpp](../indexing)
    - [src/mongo/db/exec/index\_scan.cpp](../query\_system)

### src/mongo/db/catalog/ondisk/namespace\_index.cpp

    mongo::NamespaceIndex::getNamespaces(std::list<std::string, std::allocator<std::string> >&, bool) const

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)

    mongo::NamespaceIndex::details(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/exec/oplogstart.cpp](../query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/replsettests.cpp](../unit\_tests)
    - [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/dbtests/clienttests.cpp](../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/repl/sync.cpp](../replication)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/ops/count.cpp](../query\_system)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/tools/dump.cpp](../tools)

    mongo::NamespaceIndex::_init()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

-------------

# Group Description
A DiskLoc is simply a file number and offset into the file for a db. You can think of this as an  "address" into our database's storage space.

# Files
- src/mongo/db/diskloc.h
- src/mongo/db/diskloc\_test.cpp   ()

# Interface
(not used outside this module)

-------------

# Group Description
A record is simply a "node" in a linked list. It contains "prev" and "next" offsets, as well as  the offset of the extent in the current file.

# Files
- src/mongo/db/storage/record.cpp   (mongod, tools)
- src/mongo/db/storage/record.h

# Interface

### src/mongo/db/storage/record.cpp

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
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/geo/haystack.cpp](../geo\_queries)
    - [src/mongo/dbtests/dbhelper\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/exec/2dnear.cpp](../query\_system)
    - [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
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

    mongo::Record::touch(bool) const

- Used By:

    - [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
    - [src/mongo/db/query/plan\_executor.cpp](../query\_system)
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::Record::likelyInPhysicalMemory() const

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::DiskLoc::rec() const

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
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

    mongo::Record::_accessing() const

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
    - [src/mongo/db/index/btree\_interface.cpp](../indexing)
    - [src/mongo/db/exec/oplogstart.cpp](../query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

    mongo::Record::MemoryTrackingEnabled

- Used By:

    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

    mongo::DiskLoc::drec() const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

    mongo::Record::likelyInPhysicalMemory(char const*)

- Used By:

    - [src/mongo/db/exec/fetch.cpp](../query\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../query\_system)

    mongo::DiskLoc::ext() const

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/exec/oplogstart.cpp](../query\_system)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)

    mongo::DeletedRecord::_accessing() const

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

-------------

# Group Description
An extent is a bucket of records. Extents themselves are in a kind of linked list, except instead  of offsets into a single datafile, their "prev" and "next" members are DiskLocs.

# Files
- src/mongo/db/storage/extent.cpp   (mongod, tools)
- src/mongo/db/storage/extent.h

# Interface

### src/mongo/db/storage/extent.cpp

    mongo::Extent::dump()

- Used By:

    - [src/mongo/db/commands/validate.cpp](../database\_commands)

    mongo::Extent::initialSize(int)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

    mongo::Extent::followupSize(int, int)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

    mongo::Extent::markEmpty()

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)

    mongo::Extent::validates(mongo::DiskLoc, mongo::BSONArrayBuilder*)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

    mongo::Extent::maxSize()

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

-------------

# Group Description
Sits above an extent and has helper functions to manage them as a whole. This is the new way to  iterate extents.

# Files
- src/mongo/db/storage/extent\_manager.cpp   (mongod, tools)
- src/mongo/db/storage/extent\_manager.h

# Interface

### src/mongo/db/storage/extent\_manager.cpp

    mongo::ExtentManager::getExtent(mongo::DiskLoc const&, bool) const

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

    mongo::ExtentManager::flushFiles(bool)

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

    mongo::ExtentManager::freeExtents(mongo::DiskLoc, mongo::DiskLoc)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)

    mongo::ExtentManager::quantizeExtentSize(int)

- Used By:

    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

    mongo::ExtentManager::getFile(int, int, bool)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::ExtentManager::getNextExtent(mongo::Extent*) const

- Used By:

    - [src/mongo/tools/dump.cpp](../tools)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
    - [src/mongo/db/commands/touch.cpp](../database\_commands)

    mongo::ExtentManager::fileSize() const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::ExtentManager::getNextRecordInExtent(mongo::DiskLoc const&) const

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

-------------

# Group Description
Utilities to clone entire collections and databases

# Files
- src/mongo/db/cloner.cpp   (mongod, tools)
- src/mongo/db/cloner.h

# Interface

### src/mongo/db/cloner.cpp

    mongo::Cloner::cloneFrom(mongo::Client::Context&, std::string const&, mongo::CloneOptions const&, std::string&, int*, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)

    mongo::Cloner::Cloner()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

    mongo::Cloner::copyCollectionFromRemote(std::string const&, std::string const&, std::string&)

- Used By:

    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)

    mongo::Cloner::go(mongo::Client::Context&, std::string const&, mongo::CloneOptions const&, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*, std::string&, int*)

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

-------------

# Group Description
One of the very hairy, very old parts of the server. Contains code for the DBDirectClient, which  is an implementation of the "DBClientBase" class in the client driver. The DBDirectClient has the  same interface as the client driver, except that instead of connecting over the network it is just  doing operations on the local server behind the scenes.   This also has code for the "BSONElementManipulator which is what allows us to do in place  updates in the old code. It appears now that it is only used in updating the "expireAfterSeconds"  field for a document in a TTL index.   Also have random things like "getDatabaseNames" which just iteratest the db directory getting all  the names of the files there. Also has the version of "inShutdown" and "dbexit" for mongod.   clarify relationship between instance.cpp and the various ops/* (insert/update etc)

# Files
- src/mongo/db/instance.cpp   (mongod, tools)
- src/mongo/db/instance.h

# Interface

### src/mongo/db/instance.cpp

    typeinfo for mongo::DBDirectClient

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::exitCleanly(mongo::ExitCode)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

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

    mongo::createDirectClient()

- Used By:

    - [src/mongo/scripting/engine.cpp](../javascript\_libraries)
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

    mongo::DBDirectClient::_lookupAvailableOptions()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::lockFile

- Used By:

    - [src/mongo/dbtests/framework.cpp](../unit\_tests)

    mongo::_diaglog

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

    mongo::mongoAbort(char const*)

- Used By:

    - [src/mongo/db/dur.cpp](../journaling)

    mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

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

    mongo::DiagLog::flush()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

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
    - [src/mongo/client/distlock.cpp](../sharding)
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
    - [src/mongo/s/strategy\_shard.cpp](../sharding)
    - [src/mongo/util/concurrency/task.cpp](../utilities)
    - [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)
    - [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
    - [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

    mongo::assembleResponse(mongo::Message&, mongo::DbResponse&, mongo::HostAndPort const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

    mongo::dbexit(mongo::ExitCode, char const*)

- Used By:

    - [src/mongo/s/config.cpp](../sharding)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/util/net/message\_server\_port.cpp](../network)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

    mongo::DiagLog::setLevel(int)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

    mongo::DBDirectClient::killCursor(long long)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::dbExecCommand

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

    non-virtual thunk to mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::acquirePathLock(bool)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/dbtests/framework.cpp](../unit\_tests)

    mongo::BSONElementManipulator::initTimestamp()

- Used By:

    - [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

    mongo::replHasDatabases()

- Used By:

    - [src/mongo/db/repl/heartbeat.cpp](../replication)

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
    - [src/mongo/db/compact.cpp](../database\_commands)
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
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::Database::closeDatabase(std::string const&, std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

    mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    non-virtual thunk to mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::getDatabaseNames(std::vector<std::string, std::allocator<std::string> >&, std::string const&)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/index\_rebuilder.cpp](../indexing)
    - [src/mongo/db/repl/rs.cpp](../replication)

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

    mongo::inDBRepair

- Used By:

    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

    mongo::allocateSpaceForANewRecord(char const*, mongo::NamespaceDetails*, int, bool)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

    mongo::dbSize(char const*)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::dropDatabase(std::string const&)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

    mongo::dbHolderUnchecked()

- Used By:

    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/restapi.cpp](../database\_web\_accesss)

    mongo::addRecordToRecListInExtent(mongo::Record*, mongo::DiskLoc)

- Used By:

    - [src/mongo/db/compact.cpp](../database\_commands)
    - [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

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

    mongo::_deleteDataFiles(char const*)

- Used By:

    - [src/mongo/db/durop.cpp](../journaling)

    mongo::dropAllDatabasesExceptLocal()

- Used By:

    - [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

    mongo::isValidNS(mongo::StringData const&)

- Used By:

    - [src/mongo/dbtests/basictests.cpp](../unit\_tests)

    mongo::repairDatabase(std::string, std::string&, bool, bool)

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
