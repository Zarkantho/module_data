# storage\_layer\_structure

# Module Groups

-------------

Helper to manage strings that look like "<db>.<collection>"

- src/mongo/db/namespace\_string-inl.h
- src/mongo/db/namespace\_string.h
- src/mongo/db/namespace\_string\_test.cpp   ()

## Interface

(not used outside this module)

-------------

Files containing the structural metadata about the databases/data files/collections/indexes.  TODO: Add more details here about the relationships between these files.

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

## Interface


### src/mongo/db/namespace\_details.cpp

<pre>mongo::bucketSizes</pre>

#### Used By:

- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<pre>mongo::NamespaceDetails::quantizeAllocationSpace(int)</pre>

#### Used By:

- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/commands/validate.cpp](../database\_commands)

<pre>mongo::NamespaceDetails::alloc(mongo::StringData const&, int)</pre>

#### Used By:

- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<pre>mongo::NamespaceDetails::quantizePowerOf2AllocationSpace(int)</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/commands/validate.cpp](../database\_commands)

<pre>mongo::NamespaceDetails::maxCappedDocs() const</pre>

#### Used By:

- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::NamespaceDetails::syncUserFlags(std::string const&)</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/index\_legacy.cpp](../indexing)

<pre>mongo::NamespaceDetails::setStats(long long, long long)</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)

<pre>mongo::NamespaceDetails::getRecordAllocationSize(int)</pre>

#### Used By:

- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<pre>mongo::NamespaceDetails::setUserFlag(int)</pre>

#### Used By:

- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/index\_legacy.cpp](../indexing)

<pre>mongo::NamespaceDetails::findIndexByName(mongo::StringData const&, bool)</pre>

#### Used By:

- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::NamespaceDetails::findIndexByKeyPattern(mongo::BSONObj const&, bool)</pre>

#### Used By:

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

<pre>mongo::NamespaceDetails::orphanDeletedList()</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)

<pre>mongo::NamespaceDetails::writingWithExtra()</pre>

#### Used By:

- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)

<pre>mongo::NamespaceDetails::setPaddingFactor(double)</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<pre>mongo::NamespaceDetails::findIndexByPrefix(mongo::BSONObj const&, bool)</pre>

#### Used By:

- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<pre>mongo::NamespaceDetails::updateTTLIndex(int, mongo::BSONElement const&)</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::NamespaceDetails::setLastExtentSize(int)</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)

<pre>mongo::NamespaceDetails::incrementStats(long long, long long)</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)

<pre>mongo::NamespaceDetails::clearUserFlag(int)</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::NamespaceDetails::setIndexIsMultikey(int, bool)</pre>

#### Used By:

- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)

<pre>mongo::legalClientSystemNS(mongo::StringData const&, bool)</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)
- [src/mongo/db/ops/delete.cpp](../query\_system)

### src/mongo/db/database.cpp

<pre>mongo::Database::clearTmpCollections()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/repl/rs.cpp](../replication)

<pre>mongo::Database::setProfilingLevel(int, std::string&)</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::Database::createCollection(mongo::StringData const&, bool, mongo::BSONObj const*, bool)</pre>

#### Used By:

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

<pre>mongo::Database::renameCollection(mongo::StringData const&, mongo::StringData const&, bool)</pre>

#### Used By:

- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)

<pre>mongo::Database::getOrCreateCollection(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/db/index\_builder.cpp](../indexing)
- [src/mongo/db/repl/sync.cpp](../replication)
- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

<pre>mongo::Database::getCollection(mongo::StringData const&)</pre>

#### Used By:

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

<pre>mongo::Database::duplicateUncasedName(bool, std::string const&, std::string const&, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*)</pre>

#### Used By:

- [src/mongo/db/repl/master\_slave.cpp](../replication)

<pre>mongo::Database::dropCollection(mongo::StringData const&)</pre>

#### Used By:

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

<pre>mongo::Database::_initExtentFreeList()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::Database::Database(char const*, bool&, std::string const&)</pre>

#### Used By:

- [src/mongo/dbtests/basictests.cpp](../unit\_tests)

### src/mongo/db/database\_holder.cpp

<pre>mongo::DatabaseHolder::closeAll(std::string const&, mongo::BSONObjBuilder&, bool)</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::DatabaseHolder::getOrCreate(std::string const&, std::string const&, bool&)</pre>

#### Used By:

- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/storage\_options.cpp

<pre>mongo::getJournalCommitInterval()</pre>

#### Used By:

- [src/mongo/db/commands/parameters.cpp](../database\_commands)

<pre>mongo::setJournalCommitInterval(unsigned int)</pre>

#### Used By:

- [src/mongo/db/commands/parameters.cpp](../database\_commands)

<pre>mongo::storageGlobalParams</pre>

#### Used By:

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

<pre>mongo::isJournalingEnabled()</pre>

#### Used By:

- [src/mongo/db/commands/parameters.cpp](../database\_commands)

### src/mongo/db/structure/btree/btree.cpp

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::bt_insert(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::wouldCreateDup(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::KeyV1 const&, mongo::DiskLoc const&) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::locate(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::wouldCreateDup(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::KeyBson const&, mongo::DiskLoc const&) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::locate(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&, int&, bool&, mongo::DiskLoc const&, int) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::advanceTo(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::customLocate(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyBson const&)</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::unindex(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::bt_insert(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::DiskLoc, mongo::BSONObj const&, bool, bool) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::addBucket(mongo::BtreeInMemoryState*)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::findSingle(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::advance(mongo::DiskLoc const&, int&, int, char const*) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::addBucket(mongo::BtreeInMemoryState*)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::dupKeyError(mongo::IndexDescriptor const*, mongo::KeyV1 const&)</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::advanceTo(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::unindex(mongo::BtreeInMemoryState*, mongo::DiskLoc, mongo::BSONObj const&, mongo::DiskLoc) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::findSingle(mongo::BtreeInMemoryState const*, mongo::DiskLoc const&, mongo::BSONObj const&) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::customLocate(mongo::BtreeInMemoryState const*, mongo::DiskLoc&, int&, mongo::BSONObj const&, int, bool, std::vector<mongo::BSONElement const*, std::allocator<mongo::BSONElement const*> > const&, std::vector<bool, std::allocator<bool> > const&, int, std::pair<mongo::DiskLoc, int>&)</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V0>::advance(mongo::DiskLoc const&, int&, int, char const*) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

<pre>mongo::BtreeBucket<mongo::BtreeData_V1>::fullValidate(mongo::DiskLoc const&, mongo::BSONObj const&, long long*, bool, unsigned int) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)

### src/mongo/db/structure/btree/btreebuilder.cpp

<pre>mongo::BtreeBuilder<mongo::BtreeData_V0>::BtreeBuilder(bool, mongo::BtreeInMemoryState*)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<pre>mongo::BtreeBuilder<mongo::BtreeData_V1>::BtreeBuilder(bool, mongo::BtreeInMemoryState*)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<pre>mongo::BtreeBuilder<mongo::BtreeData_V1>::commit(bool)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<pre>mongo::BtreeBuilder<mongo::BtreeData_V0>::addKey(mongo::BSONObj&, mongo::DiskLoc)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<pre>mongo::BtreeBuilder<mongo::BtreeData_V1>::addKey(mongo::BSONObj&, mongo::DiskLoc)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<pre>mongo::BtreeBuilder<mongo::BtreeData_V0>::commit(bool)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

### src/mongo/db/structure/btree/key.cpp

<pre>mongo::KeyV1::dataSize() const</pre>

#### Used By:

- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<pre>mongo::KeyV1Owned::KeyV1Owned(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/db/index/btree\_interface.cpp](../indexing)
- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<pre>mongo::KeyV1::woCompare(mongo::KeyV1 const&, mongo::Ordering const&) const</pre>

#### Used By:

- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<pre>mongo::KeyV1::woEqual(mongo::KeyV1 const&) const</pre>

#### Used By:

- [src/mongo/dbtests/perftests.cpp](../unit\_tests)
- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<pre>mongo::KeyV1::toBson() const</pre>

#### Used By:

- [src/mongo/db/commands/index\_stats.cpp](../database\_commands)
- [src/mongo/db/index/btree\_interface.cpp](../indexing)
- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<pre>mongo::oldCompare(mongo::BSONObj const&, mongo::BSONObj const&, mongo::Ordering const&)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<pre>mongo::KeyBson::woCompare(mongo::KeyBson const&, mongo::Ordering const&) const</pre>

#### Used By:

- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

### src/mongo/db/structure/btree/state.cpp

<pre>mongo::BtreeInMemoryState::head() const</pre>

#### Used By:

- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)
- [src/mongo/db/index/btree\_index\_cursor.cpp](../indexing)

<pre>mongo::BtreeInMemoryState::setMultikey()</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

<pre>mongo::BtreeInMemoryState::setHead(mongo::DiskLoc)</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

### src/mongo/db/structure/collection.cpp

<pre>mongo::Collection::storageSize(int*, mongo::BSONArrayBuilder*) const</pre>

#### Used By:

- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

<pre>mongo::Collection::docFor(mongo::DiskLoc const&)</pre>

#### Used By:

- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<pre>mongo::Collection::dataSize() const</pre>

#### Used By:

- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Collection::isCapped() const</pre>

#### Used By:

- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/commands/validate.cpp](../database\_commands)

<pre>mongo::Collection::insertDocument(mongo::DocWriter const*, bool)</pre>

#### Used By:

- [src/mongo/db/repl/oplog.cpp](../replication)

<pre>mongo::Collection::getIterator(mongo::DiskLoc const&, bool, mongo::CollectionScanParams::Direction const&) const</pre>

#### Used By:

- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)
- [src/mongo/db/exec/collection\_scan.cpp](../query\_system)
- [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
- [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)

<pre>mongo::Collection::numRecords() const</pre>

#### Used By:

- [src/mongo/db/query/new\_find.cpp](../query\_system)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Collection::insertDocument(mongo::BSONObj const&, bool)</pre>

#### Used By:

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

<pre>mongo::Collection::updateDocument(mongo::DiskLoc const&, mongo::BSONObj const&, bool, mongo::OpDebug*)</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::Collection::deleteDocument(mongo::DiskLoc const&, bool, bool, mongo::BSONObj*)</pre>

#### Used By:

- [src/mongo/dbtests/repltests.cpp](../unit\_tests)
- [src/mongo/db/ops/delete.cpp](../query\_system)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

### src/mongo/db/structure/collection\_info\_cache.cpp

<pre>mongo::CollectionInfoCache::computeIndexKeys()</pre>

#### Used By:

- [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

<pre>mongo::CollectionInfoCache::reset()</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)

<pre>mongo::CollectionInfoCache::getPlanCache() const</pre>

#### Used By:

- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)

### src/mongo/db/structure/record\_store.cpp

<pre>mongo::RecordStore::recordFor(mongo::DiskLoc const&) const</pre>

#### Used By:

- [src/mongo/db/index/btree\_interface.cpp](../indexing)
- [src/mongo/db/index/btree\_access\_method.cpp](../indexing)

### src/mongo/db/cap.cpp

<pre>mongo::NamespaceDetails::cappedTruncateAfter(char const*, mongo::DiskLoc, bool)</pre>

#### Used By:

- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)

<pre>mongo::NamespaceDetails::emptyCappedCollection(char const*)</pre>

#### Used By:

- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)
- [src/mongo/db/repl/rs\_rollback.cpp](../replication)
- [src/mongo/db/commands/test\_commands.cpp](../database\_commands)

### src/mongo/db/catalog/index\_catalog.cpp

<pre>mongo::IndexCatalog::IndexBuildBlock::IndexBuildBlock(mongo::IndexCatalog*, mongo::StringData const&, mongo::DiskLoc const&)</pre>

#### Used By:

- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::IndexCatalog::IndexBuildBlock::~IndexBuildBlock()</pre>

#### Used By:

- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::IndexCatalog::findIndexByName(mongo::StringData const&, bool)</pre>

#### Used By:

- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::IndexCatalog::getDescriptor(int)</pre>

#### Used By:

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

<pre>mongo::IndexCatalog::findIndexByKeyPattern(mongo::BSONObj const&, bool)</pre>

#### Used By:

- [src/mongo/db/exec/s2near.cpp](../query\_system)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)

<pre>mongo::IndexCatalog::numIndexesTotal() const</pre>

#### Used By:

- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/db/commands/mr.cpp](../database\_commands)

<pre>mongo::IndexCatalog::ensureHaveIdIndex()</pre>

#### Used By:

- [src/mongo/db/repl/oplog.cpp](../replication)
- [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
- [src/mongo/dbtests/repltests.cpp](../unit\_tests)

<pre>mongo::IndexCatalog::numIndexesReady() const</pre>

#### Used By:

- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/dbtests/indexcatalogtests.cpp](../unit\_tests)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)

<pre>mongo::IndexCatalog::getIndex(mongo::IndexDescriptor const*)</pre>

#### Used By:

- [src/mongo/db/exec/2dnear.cpp](../query\_system)
- [src/mongo/db/geo/haystack.cpp](../geo\_queries)
- [src/mongo/db/prefetch.cpp](../page\_fault\_utilities)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)
- [src/mongo/db/query/stage\_builder.cpp](../query\_system)
- [src/mongo/db/exec/stagedebug\_cmd.cpp](../query\_system)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/db/exec/2d.cpp](../query\_system)

<pre>mongo::IndexCatalog::dropIndex(int)</pre>

#### Used By:

- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)

<pre>mongo::IndexCatalog::findIdIndex()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
- [src/mongo/db/query/get\_runner.cpp](../query\_system)
- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/commands/dbhash.cpp](../database\_commands)

<pre>mongo::IndexCatalog::prepOneUnfinishedIndex()</pre>

#### Used By:

- [src/mongo/db/index\_rebuilder.cpp](../indexing)

<pre>mongo::IndexCatalog::findIndexByPrefix(mongo::BSONObj const&, bool)</pre>

#### Used By:

- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/d\_split.cpp](../sharding)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::IndexCatalog::blowAwayInProgressIndexEntries()</pre>

#### Used By:

- [src/mongo/db/index\_rebuilder.cpp](../indexing)

<pre>mongo::IndexCatalog::dropAllIndexes(bool)</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/commands/drop\_indexes.cpp](../database\_commands)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::IndexCatalog::ok() const</pre>

#### Used By:

- [src/mongo/db/ops/update.cpp](../query\_system)

<pre>mongo::IndexCatalog::fixIndexKey(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::IndexCatalog::getBtreeBasedIndex(mongo::IndexDescriptor const*)</pre>

#### Used By:

- [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
- [src/mongo/db/query/idhack\_runner.cpp](../query\_system)

<pre>mongo::IndexCatalog::getBtreeIndex(mongo::IndexDescriptor const*)</pre>

#### Used By:

- [src/mongo/db/exec/index\_scan.cpp](../query\_system)

<pre>mongo::IndexCatalog::IndexBuildBlock::success()</pre>

#### Used By:

- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::IndexCatalog::createIndex(mongo::BSONObj, bool)</pre>

#### Used By:

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

<pre>mongo::IndexCatalog::_getAccessMethodName(mongo::BSONObj const&)</pre>

#### Used By:

- [src/mongo/db/index\_legacy.cpp](../indexing)
- [src/mongo/db/exec/index\_scan.cpp](../query\_system)

### src/mongo/db/catalog/ondisk/namespace\_index.cpp

<pre>mongo::NamespaceIndex::getNamespaces(std::list<std::string, std::allocator<std::string> >&, bool) const</pre>

#### Used By:

- [src/mongo/db/commands/dbhash.cpp](../database\_commands)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)

<pre>mongo::NamespaceIndex::details(mongo::StringData const&)</pre>

#### Used By:

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

<pre>mongo::NamespaceIndex::_init()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

-------------

A DiskLoc is simply a file number and offset into the file for a db. You can think of this as an  "address" into our database's storage space.

- src/mongo/db/diskloc.h
- src/mongo/db/diskloc\_test.cpp   ()

## Interface

(not used outside this module)

-------------

A record is simply a "node" in a linked list. It contains "prev" and "next" offsets, as well as  the offset of the extent in the current file.

- src/mongo/db/storage/record.cpp   (mongod, tools)
- src/mongo/db/storage/record.h

## Interface


### src/mongo/db/storage/record.cpp

<pre>mongo::DiskLoc::obj() const</pre>

#### Used By:

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

<pre>mongo::Record::touch(bool) const</pre>

#### Used By:

- [src/mongo/db/pagefault.cpp](../page\_fault\_utilities)
- [src/mongo/db/query/plan\_executor.cpp](../query\_system)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::Record::likelyInPhysicalMemory() const</pre>

#### Used By:

- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::DiskLoc::rec() const</pre>

#### Used By:

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

<pre>mongo::Record::_accessing() const</pre>

#### Used By:

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

<pre>mongo::Record::MemoryTrackingEnabled</pre>

#### Used By:

- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::DiskLoc::drec() const</pre>

#### Used By:

- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/commands/validate.cpp](../database\_commands)

<pre>mongo::Record::likelyInPhysicalMemory(char const*)</pre>

#### Used By:

- [src/mongo/db/exec/fetch.cpp](../query\_system)
- [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
- [src/mongo/db/query/multi\_plan\_runner.cpp](../query\_system)
- [src/mongo/db/query/plan\_executor.cpp](../query\_system)

<pre>mongo::DiskLoc::ext() const</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/exec/oplogstart.cpp](../query\_system)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/commands/rename\_collection.cpp](../database\_commands)
- [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
- [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
- [src/mongo/db/commands/validate.cpp](../database\_commands)
- [src/mongo/tools/dump.cpp](../tools)

<pre>mongo::DeletedRecord::_accessing() const</pre>

#### Used By:

- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
- [src/mongo/db/commands/validate.cpp](../database\_commands)

-------------

An extent is a bucket of records. Extents themselves are in a kind of linked list, except instead  of offsets into a single datafile, their "prev" and "next" members are DiskLocs.

- src/mongo/db/storage/extent.cpp   (mongod, tools)
- src/mongo/db/storage/extent.h

## Interface


### src/mongo/db/storage/extent.cpp

<pre>mongo::Extent::dump()</pre>

#### Used By:

- [src/mongo/db/commands/validate.cpp](../database\_commands)

<pre>mongo::Extent::initialSize(int)</pre>

#### Used By:

- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

<pre>mongo::Extent::followupSize(int, int)</pre>

#### Used By:

- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

<pre>mongo::Extent::markEmpty()</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)

<pre>mongo::Extent::validates(mongo::DiskLoc, mongo::BSONArrayBuilder*)</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/commands/validate.cpp](../database\_commands)

<pre>mongo::Extent::maxSize()</pre>

#### Used By:

- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

-------------

Sits above an extent and has helper functions to manage them as a whole. This is the new way to  iterate extents.

- src/mongo/db/storage/extent\_manager.cpp   (mongod, tools)
- src/mongo/db/storage/extent\_manager.h

## Interface


### src/mongo/db/storage/extent\_manager.cpp

<pre>mongo::ExtentManager::getExtent(mongo::DiskLoc const&, bool) const</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/commands/touch.cpp](../database\_commands)

<pre>mongo::ExtentManager::flushFiles(bool)</pre>

#### Used By:

- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<pre>mongo::ExtentManager::freeExtents(mongo::DiskLoc, mongo::DiskLoc)</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)

<pre>mongo::ExtentManager::quantizeExtentSize(int)</pre>

#### Used By:

- [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)

<pre>mongo::ExtentManager::getFile(int, int, bool)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::ExtentManager::getNextExtent(mongo::Extent*) const</pre>

#### Used By:

- [src/mongo/tools/dump.cpp](../tools)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)
- [src/mongo/db/commands/touch.cpp](../database\_commands)

<pre>mongo::ExtentManager::fileSize() const</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::ExtentManager::getNextRecordInExtent(mongo::DiskLoc const&) const</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/db/commands/storage\_details.cpp](../database\_commands)

-------------

Utilities to clone entire collections and databases

- src/mongo/db/cloner.cpp   (mongod, tools)
- src/mongo/db/cloner.h

## Interface


### src/mongo/db/cloner.cpp

<pre>mongo::Cloner::cloneFrom(mongo::Client::Context&, std::string const&, mongo::CloneOptions const&, std::string&, int*, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*)</pre>

#### Used By:

- [src/mongo/db/repl/master\_slave.cpp](../replication)

<pre>mongo::Cloner::Cloner()</pre>

#### Used By:

- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<pre>mongo::Cloner::copyCollectionFromRemote(std::string const&, std::string const&, std::string&)</pre>

#### Used By:

- [src/mongo/db/repl/rs\_rollback.cpp](../replication)

<pre>mongo::Cloner::go(mongo::Client::Context&, std::string const&, mongo::CloneOptions const&, std::set<std::string, std::less<std::string>, std::allocator<std::string> >*, std::string&, int*)</pre>

#### Used By:

- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

-------------

One of the very hairy, very old parts of the server. Contains code for the DBDirectClient, which  is an implementation of the "DBClientBase" class in the client driver. The DBDirectClient has the  same interface as the client driver, except that instead of connecting over the network it is just  doing operations on the local server behind the scenes.   This also has code for the "BSONElementManipulator which is what allows us to do in place  updates in the old code. It appears now that it is only used in updating the "expireAfterSeconds"  field for a document in a TTL index.   Also have random things like "getDatabaseNames" which just iteratest the db directory getting all  the names of the files there. Also has the version of "inShutdown" and "dbexit" for mongod.   clarify relationship between instance.cpp and the various ops/* (insert/update etc)

- src/mongo/db/instance.cpp   (mongod, tools)
- src/mongo/db/instance.h

## Interface


### src/mongo/db/instance.cpp

<pre>typeinfo for mongo::DBDirectClient</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::exitCleanly(mongo::ExitCode)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::DBDirectClient::query(std::string const&, mongo::Query, int, int, mongo::BSONObj const*, int, int)</pre>

#### Used By:

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

<pre>mongo::createDirectClient()</pre>

#### Used By:

- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<pre>mongo::DBDirectClient::_lookupAvailableOptions()</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::lockFile</pre>

#### Used By:

- [src/mongo/dbtests/framework.cpp](../unit\_tests)

<pre>mongo::_diaglog</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::mongoAbort(char const*)</pre>

#### Used By:

- [src/mongo/db/dur.cpp](../journaling)

<pre>mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>vtable for mongo::DBDirectClient</pre>

#### Used By:

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

<pre>mongo::DBDirectClient::count(std::string const&, mongo::BSONObj const&, int, int, int)</pre>

#### Used By:

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

<pre>mongo::DiagLog::flush()</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::inShutdown()</pre>

#### Used By:

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

<pre>mongo::assembleResponse(mongo::Message&, mongo::DbResponse&, mongo::HostAndPort const&)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::dbexit(mongo::ExitCode, char const*)</pre>

#### Used By:

- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/util/net/message\_server\_port.cpp](../network)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::DiagLog::setLevel(int)</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/mongod\_options.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::DBDirectClient::killCursor(long long)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::dbExecCommand</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<pre>non-virtual thunk to mongo::DBDirectClient::call(mongo::Message&, mongo::Message&, bool, std::string*)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::acquirePathLock(bool)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)

<pre>mongo::BSONElementManipulator::initTimestamp()</pre>

#### Used By:

- [src/mongo/dbtests/jsobjtests.cpp](../unit\_tests)

<pre>mongo::replHasDatabases()</pre>

#### Used By:

- [src/mongo/db/repl/heartbeat.cpp](../replication)

<pre>mongo::killCurrentOp</pre>

#### Used By:

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

<pre>mongo::Database::closeDatabase(std::string const&, std::string const&)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

<pre>mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>non-virtual thunk to mongo::DBDirectClient::say(mongo::Message&, bool, std::string*)</pre>

#### Used By:

- [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/sharding.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
- [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

<pre>mongo::getDatabaseNames(std::vector<std::string, std::allocator<std::string> >&, std::string const&)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/auth/authz\_manager\_external\_state\_d.cpp](../authentication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/index\_rebuilder.cpp](../indexing)
- [src/mongo/db/repl/rs.cpp](../replication)

-------------

This is another really hairy, really old legacy file. At this point it's easier to just write out  all the functions in the interface than describe what it does. I believe "pdfile" is short for  "persistent data file". It contains a bunch of old legacy things to manipulate data files and  data file metadata.   Here are all the functions in pdfile.cpp that are currently used in the project.   mongo::inDBRepair  mongo::allocateSpaceForANewRecord(char const*, mongo::NamespaceDetails*, int, bool)  mongo::dbSize(char const*)  mongo::dropDatabase(std::string const&)  mongo::dbHolderUnchecked()  mongo::addRecordToRecListInExtent(mongo::Record*, mongo::DiskLoc)  mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)  mongo::\_deleteDataFiles(char const*)  mongo::dropAllDatabasesExceptLocal()  mongo::isValidNS(mongo::StringData const&)  mongo::repairDatabase(std::string, std::string&, bool, bool)

- src/mongo/db/pdfile.cpp   (mongod, tools)
- src/mongo/db/pdfile.h
- src/mongo/db/pdfile\_private.h
- src/mongo/db/pdfile\_version.h

## Interface


### src/mongo/db/pdfile.cpp

<pre>mongo::inDBRepair</pre>

#### Used By:

- [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)

<pre>mongo::allocateSpaceForANewRecord(char const*, mongo::NamespaceDetails*, int, bool)</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::dbSize(char const*)</pre>

#### Used By:

- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::dropDatabase(std::string const&)</pre>

#### Used By:

- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)

<pre>mongo::dbHolderUnchecked()</pre>

#### Used By:

- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/introspect.cpp](../client\_and\_operation\_tracking)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
- [src/mongo/db/restapi.cpp](../database\_web\_accesss)

<pre>mongo::addRecordToRecListInExtent(mongo::Record*, mongo::DiskLoc)</pre>

#### Used By:

- [src/mongo/db/compact.cpp](../database\_commands)
- [src/mongo/dbtests/indexupdatetests.cpp](../unit\_tests)

<pre>mongo::userCreateNS(char const*, mongo::BSONObj, std::string&, bool, bool*)</pre>

#### Used By:

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

<pre>mongo::_deleteDataFiles(char const*)</pre>

#### Used By:

- [src/mongo/db/durop.cpp](../journaling)

<pre>mongo::dropAllDatabasesExceptLocal()</pre>

#### Used By:

- [src/mongo/db/repl/rs\_initialsync.cpp](../replication)

<pre>mongo::isValidNS(mongo::StringData const&)</pre>

#### Used By:

- [src/mongo/dbtests/basictests.cpp](../unit\_tests)

<pre>mongo::repairDatabase(std::string, std::string&, bool, bool)</pre>

#### Used By:

- [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
- [src/mongo/db/dbcommands.cpp](../database\_commands)
