# sharding

# Module Groups

-------------

# Group Description
Helper classes to delete a range of documents. This is used for example in chunk migrations  when we are cleaning up an old chunk.

# Files
- src/mongo/db/range\_deleter.cpp   (mongod, tools)
- src/mongo/db/range\_deleter.h
- src/mongo/db/range\_deleter\_db\_env.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_db\_env.h
- src/mongo/db/range\_deleter\_mock\_env.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_mock\_env.h
- src/mongo/db/range\_deleter\_service.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_service.h
- src/mongo/db/range\_deleter\_stat\_test.cpp   ()
- src/mongo/db/range\_deleter\_stats.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_stats.h
- src/mongo/db/range\_deleter\_test.cpp   ()
- src/mongo/db/range\_preserver.h

# Interface

### src/mongo/db/range\_deleter.cpp

- <pre>mongo::RangeDeleter::deleteNow(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, std::string*)</pre>
Used By:
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

- <pre>mongo::RangeDeleter::startWorkers()</pre>
Used By:
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/range\_deleter\_service.cpp

- <pre>mongo::getDeleter()</pre>
Used By:
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

-------------

# Group Description
Utilities for comparing ranges. Useful because our sharding is range based.   okay, but why in s/ ? only used by sharding? seems weird that something   general like range arith is only in s/ but the more specific delete-range   isn't.

# Files
- src/mongo/s/range\_arithmetic.cpp   (mongod, tools, mongos)
- src/mongo/s/range\_arithmetic.h
- src/mongo/s/range\_arithmetic\_test.cpp   ()

# Interface
(not used outside this module)

-------------

# Group Description
Contains metadata about a collection, particularly for sharding. The MetadataLoader populates new  CollectionMetadata objects from config server data.

# Files
- src/mongo/s/collection\_metadata.cpp   (mongod, tools)
- src/mongo/s/collection\_metadata.h
- src/mongo/s/collection\_metadata\_test.cpp   ()
- src/mongo/s/metadata\_loader.cpp   (mongod, tools)
- src/mongo/s/metadata\_loader.h
- src/mongo/s/metadata\_loader\_test.cpp   ()

# Interface

### src/mongo/s/collection\_metadata.cpp

- <pre>mongo::CollectionMetadata::getNextChunk(mongo::BSONObj const&, mongo::ChunkType*) const</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

- <pre>mongo::CollectionMetadata::getMinKey() const</pre>
Used By:
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

- <pre>mongo::CollectionMetadata::getNextOrphanRange(mongo::BSONObj const&, mongo::KeyRange*) const</pre>
Used By:
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

- <pre>mongo::CollectionMetadata::keyBelongsToMe(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/exec/shard\_filter.cpp](../query\_system)

- <pre>mongo::CollectionMetadata::keyIsPending(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

- <pre>mongo::CollectionMetadata::isValidKey(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

-------------

# Group Description
Code to upgrade config server metadata

# Files
- src/mongo/s/config\_upgrade.cpp   (mongos)
- src/mongo/s/config\_upgrade.h
- src/mongo/s/config\_upgrade\_helpers.cpp   (mongos)
- src/mongo/s/config\_upgrade\_helpers.h
- src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp   (mongos)
- src/mongo/s/config\_upgrade\_v4\_to\_v5.cpp   (mongos)

# Interface

### src/mongo/s/config\_upgrade.cpp

- <pre>mongo::checkAndUpgradeConfigVersion(mongo::ConnectionString const&, bool, mongo::VersionType*, mongo::VersionType*, std::string*)</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::getConfigVersion(mongo::ConnectionString const&, mongo::VersionType*)</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

-------------

# Group Description
Distributed lock (lock on the config servers from mongos, i.e. "balancer lock")

# Files
- src/mongo/client/distlock.cpp   (mongod, tools, mongos)
- src/mongo/client/distlock.h
- src/mongo/client/distlock\_test.cpp   (mongod, tools)

# Interface

### src/mongo/client/distlock.cpp

- <pre>mongo::ScopedDistributedLock::ScopedDistributedLock(mongo::ConnectionString const&, std::string const&)</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

- <pre>mongo::DistributedLock::DistributedLock(mongo::ConnectionString const&, std::string const&, unsigned long long, bool)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::DistributedLock::unlock(mongo::BSONObj*)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::DistributedLock::lock_try(std::string const&, bool, mongo::BSONObj*, double)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::setLockPingerEnabled(bool)</pre>
Used By:
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

- <pre>mongo::ScopedDistributedLock::acquire(long long, std::string*)</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

-------------

# Group Description
Parser for fields in a BSON object. Meant to help enforce a schema on a BSON object.

# Files
- src/mongo/db/field\_parser-inl.h
- src/mongo/db/field\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/field\_parser.h
- src/mongo/db/field\_parser\_test.cpp   ()

# Interface

### src/mongo/db/field\_parser.cpp

- <pre>mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::Date_t> const&, mongo::Date_t*, std::string*)</pre>
Used By:
    - [src/mongo/s/type\_mongos.cpp](../sharding)

- <pre>mongo::FieldParser::extractID(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)</pre>
Used By:
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)</pre>
Used By:
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::OpTime> const&, mongo::OpTime*, std::string*)</pre>
Used By:
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONArray> const&, mongo::BSONArray*, std::string*)</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)</pre>
Used By:
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/type\_explain.cpp](../query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)</pre>
Used By:
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/type\_explain.cpp](../query\_system)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

- <pre>mongo::FieldParser::extractNumber(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)</pre>
Used By:
    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<bool> const&, bool*, std::string*)</pre>
Used By:
    - [src/mongo/db/query/type\_explain.cpp](../query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

- <pre>mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<long long> const&, long long*, std::string*)</pre>
Used By:
    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

- <pre>mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::OID> const&, mongo::OID*, std::string*)</pre>
Used By:
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)

-------------

# Group Description
"Schema" for config server metadata. These classes contain structural class definitions for what  we expect to find on the config server. They use the field parser above to convert BSON fields  into C++ members.

# Files
- src/mongo/s/type\_changelog.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_changelog.h
- src/mongo/s/type\_changelog\_test.cpp   ()
- src/mongo/s/type\_chunk.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_chunk.h
- src/mongo/s/type\_chunk\_test.cpp   ()
- src/mongo/s/type\_collection.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_collection.h
- src/mongo/s/type\_collection\_test.cpp   ()
- src/mongo/s/type\_config\_version.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_config\_version.h
- src/mongo/s/type\_config\_version\_test.cpp   ()
- src/mongo/s/type\_database.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_database.h
- src/mongo/s/type\_database\_test.cpp   ()
- src/mongo/s/type\_lockpings.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_lockpings.h
- src/mongo/s/type\_lockpings\_test.cpp   ()
- src/mongo/s/type\_locks.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_locks.h
- src/mongo/s/type\_locks\_test.cpp   ()
- src/mongo/s/type\_mongos.cpp   (mongos)
- src/mongo/s/type\_mongos.h
- src/mongo/s/type\_mongos\_test.cpp   ()
- src/mongo/s/type\_settings.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_settings.h
- src/mongo/s/type\_settings\_test.cpp   ()
- src/mongo/s/type\_shard.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_shard.h
- src/mongo/s/type\_shard\_test.cpp   ()
- src/mongo/s/type\_tags.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_tags.h
- src/mongo/s/type\_tags\_test.cpp   ()

# Interface

### src/mongo/s/type\_changelog.cpp

- <pre>mongo::ChangelogType::ConfigNS</pre>
Used By:
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

### src/mongo/s/type\_chunk.cpp

- <pre>mongo::ChunkType::min</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

- <pre>mongo::ChunkType::ConfigNS</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ChunkType::max</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

- <pre>mongo::ChunkType::toBSON() const</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

- <pre>mongo::ChunkType::DEPRECATED_lastmod</pre>
Used By:
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

- <pre>mongo::ChunkType::~ChunkType()</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

- <pre>mongo::ChunkType::ns</pre>
Used By:
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

- <pre>mongo::ChunkType::ChunkType()</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

- <pre>mongo::ChunkType::shard</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

### src/mongo/s/type\_collection.cpp

- <pre>mongo::CollectionType::toBSON() const</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

- <pre>mongo::CollectionType::~CollectionType()</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

- <pre>mongo::CollectionType::ns</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

- <pre>mongo::CollectionType::ConfigNS</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

- <pre>mongo::CollectionType::isValid(std::string*) const</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

- <pre>mongo::CollectionType::CollectionType()</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

### src/mongo/s/type\_config\_version.cpp

- <pre>mongo::VersionType::VersionType()</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::VersionType::clear()</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

- <pre>mongo::VersionType::~VersionType()</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::VersionType::ConfigNS</pre>
Used By:
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

- <pre>mongo::VersionType::toBSON() const</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

### src/mongo/s/type\_database.cpp

- <pre>mongo::DatabaseType::~DatabaseType()</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

- <pre>mongo::DatabaseType::DatabaseType()</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

- <pre>mongo::DatabaseType::parseBSON(mongo::BSONObj const&, std::string*)</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

- <pre>mongo::DatabaseType::ConfigNS</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

- <pre>mongo::DatabaseType::isValid(std::string*) const</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

- <pre>mongo::DatabaseType::primary</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::DatabaseType::name</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

### src/mongo/s/type\_settings.cpp

- <pre>mongo::SettingsType::ConfigNS</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

- <pre>mongo::SettingsType::key</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

- <pre>mongo::SettingsType::balancerStopped</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

### src/mongo/s/type\_shard.cpp

- <pre>mongo::ShardType::name</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ShardType::~ShardType()</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

- <pre>mongo::ShardType::ConfigNS</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

- <pre>mongo::ShardType::ShardType()</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

- <pre>mongo::ShardType::draining</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ShardType::maxSize</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ShardType::toBSON() const</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

-------------

# Group Description
Bizarre legacy sharding code.   From writeback\_listener.h  "The writeback listener takes back write attempts that were made against a wrong shard.  (Wrong here in the sense that the target chunk moved before this mongos had a chance to  learn so.) It is responsible for reapplying these writes to the correct shard."   So basically, the mongos sends an operation to the mongod, and the writeback listener (running on  the mongos) says to the mongod every now and again, "yo, have I screwed up recently?". The mongod  is then like "yeah bro, you screwed up, you wrote all these things to the wrong place and the  writeback listener is like "thanks man" and tries to write them to the correct shard. Meanwhile  the user is like "I'm so glad my data was written". This should go away because of the new write  commands.   rofl

# Files
- src/mongo/s/writeback\_listener.cpp   (mongos)
- src/mongo/s/writeback\_listener.h

# Interface

### src/mongo/s/writeback\_listener.cpp

- <pre>mongo::WriteBackListener::waitFor(mongo::WriteBackListener::ConnectionIdent const&, mongo::OID const&)</pre>
Used By:
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)

-------------

# Group Description
mongod component of writeback listener

# Files
- src/mongo/s/d\_writeback.cpp   (mongod, tools)
- src/mongo/s/d\_writeback.h

# Interface
(not used outside this module)

-------------

# Group Description
Sharding code? TODO: verify that this is all sharding related and document the architecture.

# Files
- src/mongo/s/balance.cpp   (mongos)
- src/mongo/s/balance.h
- src/mongo/s/balancer\_policy.cpp   (mongos)
- src/mongo/s/balancer\_policy.h
- src/mongo/s/balancer\_policy\_tests.cpp   ()
- src/mongo/s/bson\_serializable.h
- src/mongo/s/chunk.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk.h
- src/mongo/s/chunk\_diff-inl.cpp
- src/mongo/s/chunk\_diff.h
- src/mongo/s/chunk\_diff\_test.cpp   ()
- src/mongo/s/chunk\_manager\_targeter.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk\_manager\_targeter.h
- src/mongo/s/chunk\_version.h
- src/mongo/s/chunk\_version\_test.cpp   ()
- src/mongo/s/cluster\_client\_internal.cpp   (mongos)
- src/mongo/s/cluster\_client\_internal.h
- src/mongo/s/cluster\_write.cpp   (mongod, tools, mongos)
- src/mongo/s/cluster\_write.h
- src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp   (mongos)
- src/mongo/s/config.cpp   (mongod, tools, mongos)
- src/mongo/s/config.h
- src/mongo/s/config\_server\_checker\_service.cpp   (mongod, tools, mongos)
- src/mongo/s/config\_server\_checker\_service.h
- src/mongo/s/config\_server\_tests.cpp   ()
- src/mongo/s/cursors.cpp   (mongos)
- src/mongo/s/cursors.h
- src/mongo/s/d\_logic.cpp   (mongod, tools)
- src/mongo/s/d\_logic.h
- src/mongo/s/d\_merge.cpp   (mongod, tools)
- src/mongo/s/d\_merge.h
- src/mongo/s/d\_migrate.cpp   (mongod, tools)
- src/mongo/s/d\_split.cpp   (mongod, tools)
- src/mongo/s/d\_state.cpp   (mongod, tools)
- src/mongo/s/dbclient\_multi\_command.cpp   (mongod, tools, mongos)
- src/mongo/s/dbclient\_multi\_command.h
- src/mongo/s/dbclient\_shard\_resolver.cpp   (mongod, tools, mongos)
- src/mongo/s/dbclient\_shard\_resolver.h
- src/mongo/s/default\_version.cpp   (mongod, tools)
- src/mongo/s/grid.cpp   (mongod, tools, mongos)
- src/mongo/s/grid.h
- src/mongo/s/mock\_multi\_command.h
- src/mongo/s/mock\_ns\_targeter.h
- src/mongo/s/mock\_shard\_resolver.h
- src/mongo/s/mongo\_version\_range.cpp   (mongod, tools, mongos)
- src/mongo/s/mongo\_version\_range.h
- src/mongo/s/mongo\_version\_range\_test.cpp   ()
- src/mongo/s/mongos\_persistence\_stubs.cpp   (mongos)
- src/mongo/s/multi\_command\_dispatch.h
- src/mongo/s/ns\_targeter.h
- src/mongo/s/request.cpp   (mongos)
- src/mongo/s/request.h
- src/mongo/s/shard.cpp   (mongod, tools, mongos)
- src/mongo/s/shard.h
- src/mongo/s/shard\_conn\_test.cpp   ()
- src/mongo/s/shard\_key\_pattern.cpp   (mongod, tools, mongos)
- src/mongo/s/shard\_key\_pattern.h
- src/mongo/s/shard\_resolver.h
- src/mongo/s/shard\_test.cpp   ()
- src/mongo/s/shardconnection.cpp   (mongod, tools, mongos)
- src/mongo/s/shardkey.cpp   (mongod, tools, mongos)
- src/mongo/s/shardkey.h
- src/mongo/s/stale\_exception.h
- src/mongo/s/strategy.cpp   (mongos)
- src/mongo/s/strategy.h
- src/mongo/s/strategy\_shard.cpp   (mongos)
- src/mongo/s/strategy\_single.cpp   (mongos)
- src/mongo/s/version\_manager.cpp   (mongos)
- src/mongo/s/version\_manager.h
- src/mongo/s/version\_mongos.cpp   (mongos)
- src/mongo/s/version\_mongos.h

# Interface

### src/mongo/s/balance.cpp

- <pre>mongo::balancer</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/chunk.cpp

- <pre>mongo::ChunkManager::loadExistingRanges(std::string const&)</pre>
Used By:
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

- <pre>mongo::Chunk::MaxChunkSize</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::Chunk::multiSplit(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, mongo::BSONObj&) const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ChunkManager::hasShardKey(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::ChunkManager::createFirstChunks(std::string const&, mongo::Shard const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const*, std::vector<mongo::Shard, std::allocator<mongo::Shard> > const*)</pre>
Used By:
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

- <pre>mongo::Chunk::moveAndCommit(mongo::Shard const&, long long, bool, bool, int, mongo::BSONObj&) const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ChunkManager::ChunkManager(std::string const&, mongo::ShardKeyPattern const&, bool)</pre>
Used By:
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

- <pre>mongo::ChunkManager::compatibleWith(mongo::ChunkManager const&, mongo::Shard const&) const</pre>
Used By:
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::Chunk::ShouldAutoSplit</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::ChunkManager::getShardsForQuery(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::ChunkManager::drop(boost::shared_ptr<mongo::ChunkManager const>) const</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::ChunkManager::findChunkForDoc(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ChunkManager::findIntersectingChunk(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ChunkManager::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::Chunk::splitIfShould(long) const</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::ChunkRangeManager::reloadAll(std::map<mongo::BSONObj, boost::shared_ptr<mongo::Chunk const>, mongo::BSONObjCmp, std::allocator<std::pair<mongo::BSONObj const, boost::shared_ptr<mongo::Chunk const> > > > const&)</pre>
Used By:
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

- <pre>mongo::ChunkManager::_printChunks() const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ChunkManager::ChunkManager(boost::shared_ptr<mongo::ChunkManager const>)</pre>
Used By:
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

- <pre>mongo::ChunkManager::ChunkManager()</pre>
Used By:
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

- <pre>mongo::Chunk::Chunk(mongo::ChunkManager const*, mongo::BSONObj const&, mongo::BSONObj const&, mongo::Shard const&, mongo::ChunkVersion)</pre>
Used By:
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

- <pre>mongo::Chunk::singleSplit(bool, mongo::BSONObj&) const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ChunkManager::getShardsForRange(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&, mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::Chunk::setMaxChunkSizeSizeMB(int)</pre>
Used By:
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::Chunk::genID(std::string const&, mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

- <pre>mongo::Chunk::containsPoint(mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ChunkManager::getVersion() const</pre>
Used By:
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/cluster\_client\_internal.cpp

- <pre>mongo::checkClusterMongoVersions(mongo::ConnectionString const&, std::string const&)</pre>
Used By:
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

### src/mongo/s/cluster\_write.cpp

- <pre>mongo::ClusterWriterStats::hasShardStats() const</pre>
Used By:
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::ClusterWriter::write(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)</pre>
Used By:
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::ClusterWriter::ClusterWriter(bool, int)</pre>
Used By:
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::ClusterWriter::getStats()</pre>
Used By:
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::ClusterWriterStats::getShardStats() const</pre>
Used By:
    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

### src/mongo/s/config.cpp

- <pre>mongo::ConfigServer::init(std::vector<std::string, std::allocator<std::string> >)</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::configServer</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

- <pre>mongo::DBConfig::getChunkManager(std::string const&, bool, bool)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

- <pre>mongo::serverID</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::ConfigServer::reloadSettings()</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::DBConfig::getShard(std::string const&)</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::DBConfig::dropDatabase(std::string&)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::DBConfig::getChunkManagerIfExists(std::string const&, bool, bool)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::ConfigServer::logChange(std::string const&, std::string const&, mongo::BSONObj const&)</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::DBConfig::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::DBConfig::getAllShardedCollections(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::DBConfig::setPrimary(std::string const&)</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::DBConfig::enableSharding(bool)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::DBConfig::removeSharding(std::string const&)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::DBConfig::shardCollection(std::string const&, mongo::ShardKeyPattern, bool, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >*, std::vector<mongo::Shard, std::allocator<mongo::Shard> >*)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::DBConfig::isSharded(std::string const&)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

- <pre>mongo::ConfigServer::ok(bool)</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::ConfigServer::replicaSetChange(mongo::ReplicaSetMonitor const*)</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::DBConfig::getChunkManagerOrPrimary(std::string const&, boost::shared_ptr<mongo::ChunkManager const>&, boost::shared_ptr<mongo::Shard>&)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::DBConfig::load()</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::ConfigServer::allUp(std::string&)</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::DBConfig::reload()</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/config\_server\_checker\_service.cpp

- <pre>mongo::startConfigServerChecker()</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/cursors.cpp

- <pre>mongo::cursorCache</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::CursorCache::storeRef(std::string const&, long long, std::string const&)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::CursorCache::startTimeoutThread()</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/d\_logic.cpp

- <pre>mongo::_handlePossibleShardedMessage(mongo::Message&, mongo::DbResponse*)</pre>
Used By:
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/s/d\_merge.cpp

- <pre>mongo::mergeChunks(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::OID const&, bool, std::string*)</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)

### src/mongo/s/d\_migrate.cpp

- <pre>mongo::aboutToDeleteForSharding(mongo::StringData const&, mongo::Database const*, mongo::NamespaceDetails const*, mongo::DiskLoc const&)</pre>
Used By:
    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

- <pre>mongo::logOpForSharding(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj const*, bool)</pre>
Used By:
    - [src/mongo/db/repl/oplog.cpp](../replication)

### src/mongo/s/d\_state.cpp

- <pre>mongo::ShardingState::needCollectionMetadata(std::string const&) const</pre>
Used By:
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)

- <pre>mongo::ShardedConnectionInfo::addHook()</pre>
Used By:
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)

- <pre>mongo::ShardingState::gotShardName(std::string const&)</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)

- <pre>mongo::shardingState</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/rs.cpp](../replication)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

- <pre>mongo::ShardingState::resetMetadata(std::string const&)</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

- <pre>mongo::ShardingState::getCollectionMetadata(std::string const&)</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../query\_system)
    - [src/mongo/db/query/stage\_builder.cpp](../query\_system)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)

- <pre>mongo::ShardingState::initialize(std::string const&)</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)

- <pre>mongo::ShardingState::refreshMetadataIfNeeded(std::string const&, mongo::ChunkVersion const&, mongo::ChunkVersion*)</pre>
Used By:
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::ShardingState::setShardName(std::string const&)</pre>
Used By:
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

- <pre>mongo::ShardingState::getVersion(std::string const&) const</pre>
Used By:
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)

- <pre>mongo::ShardedConnectionInfo::get(bool)</pre>
Used By:
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

- <pre>mongo::ShardingState::refreshMetadataNow(std::string const&, mongo::ChunkVersion*)</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

- <pre>mongo::haveLocalShardingInfo(std::string const&)</pre>
Used By:
    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

- <pre>mongo::shardVersionOk(std::string const&, std::string&, mongo::ChunkVersion&, mongo::ChunkVersion&)</pre>
Used By:
    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

- <pre>mongo::ShardingState::resetShardingState()</pre>
Used By:
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)

### src/mongo/s/default\_version.cpp

- <pre>mongo::versionManager</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::VersionManager::isVersionableCB(mongo::DBClientBase*)</pre>
Used By:
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)</pre>
Used By:
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)</pre>
Used By:
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/grid.cpp

- <pre>mongo::Grid::removeDBIfExists(mongo::DBConfig const&)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::Grid::addShard(std::string*, mongo::ConnectionString const&, long long, std::string&)</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::Grid::setAllowLocalHost(bool)</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::Grid::knowAboutShard(std::string const&) const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::Grid::flushConfig()</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::grid</pre>
Used By:
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::Grid::allowLocalHost() const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/mongos\_persistence\_stubs.cpp

- <pre>mongo::isJournalingEnabled()</pre>
Used By:
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

- <pre>mongo::getJournalCommitInterval()</pre>
Used By:
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

- <pre>mongo::setJournalCommitInterval(unsigned int)</pre>
Used By:
    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

### src/mongo/s/request.cpp

- <pre>mongo::Request::process(int)</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::Request::init()</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::Request::Request(mongo::Message&, mongo::AbstractMessagingPort*)</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/shard.cpp

- <pre>mongo::Shard::setAddress(mongo::ConnectionString const&)</pre>
Used By:
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

- <pre>mongo::Shard::reloadShardInfo()</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::Shard::runCommand(std::string const&, mongo::BSONObj const&) const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::Shard::removeShard(std::string const&)</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>vtable for mongo::ShardingConnectionHook</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::Shard::reset(std::string const&)</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::Shard::_setAddr(std::string const&)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

- <pre>mongo::Shard::getAllShards(std::vector<mongo::Shard, std::allocator<mongo::Shard> >&)</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

### src/mongo/s/shard\_key\_pattern.cpp

- <pre>mongo::isUniqueIndexCompatible(mongo::BSONObj, mongo::BSONObj)</pre>
Used By:
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

### src/mongo/s/shardconnection.cpp

- <pre>mongo::ShardConnection::~ShardConnection()</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::ShardConnection::releaseMyConnections()</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::ShardConnection::_finishInit()</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::ShardConnection::kill()</pre>
Used By:
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::ShardConnection::sync()</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ShardConnection::ShardConnection(std::string const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::ShardConnection::releaseConnectionsAfterResponse</pre>
Used By:
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::ShardConnection::forgetNS(std::string const&)</pre>
Used By:
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

- <pre>mongo::shardConnectionPool</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

- <pre>mongo::ShardConnection::ShardConnection(mongo::Shard const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::ShardConnection::done()</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/shardkey.cpp

- <pre>mongo::ShardKeyPattern::isUniqueIndexCompatible(mongo::KeyPattern const&) const</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

- <pre>mongo::ShardKeyPattern::ShardKeyPattern(mongo::BSONObj)</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

### src/mongo/s/strategy\_shard.cpp

- <pre>mongo::SHARDED</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::Strategy::useClusterWriteCommands</pre>
Used By:
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

### src/mongo/s/version\_manager.cpp

- <pre>mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)</pre>
Used By:
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

- <pre>mongo::versionManager</pre>
Used By:
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)</pre>
Used By:
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

- <pre>mongo::VersionManager::isVersionableCB(mongo::DBClientBase*)</pre>
Used By:
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
