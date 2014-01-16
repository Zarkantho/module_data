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

    mongo::RangeDeleter::deleteNow(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, std::string*)

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

    mongo::RangeDeleter::startWorkers()

- Used By:

    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/db/range\_deleter\_service.cpp

    mongo::getDeleter()

- Used By:

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

    mongo::CollectionMetadata::getNextChunk(mongo::BSONObj const&, mongo::ChunkType*) const

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

    mongo::CollectionMetadata::getMinKey() const

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

    mongo::CollectionMetadata::getNextOrphanRange(mongo::BSONObj const&, mongo::KeyRange*) const

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

    mongo::CollectionMetadata::keyBelongsToMe(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/exec/shard\_filter.cpp](../query\_system)

    mongo::CollectionMetadata::keyIsPending(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

    mongo::CollectionMetadata::isValidKey(mongo::BSONObj const&) const

- Used By:

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

    mongo::checkAndUpgradeConfigVersion(mongo::ConnectionString const&, bool, mongo::VersionType*, mongo::VersionType*, std::string*)

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::getConfigVersion(mongo::ConnectionString const&, mongo::VersionType*)

- Used By:

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

    mongo::ScopedDistributedLock::ScopedDistributedLock(mongo::ConnectionString const&, std::string const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

    mongo::DistributedLock::DistributedLock(mongo::ConnectionString const&, std::string const&, unsigned long long, bool)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::DistributedLock::unlock(mongo::BSONObj*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::DistributedLock::lock_try(std::string const&, bool, mongo::BSONObj*, double)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::setLockPingerEnabled(bool)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::ScopedDistributedLock::acquire(long long, std::string*)

- Used By:

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

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::Date_t> const&, mongo::Date_t*, std::string*)

- Used By:

    - [src/mongo/s/type\_mongos.cpp](../sharding)

    mongo::FieldParser::extractID(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../new\_wire\_protocol\_write\_commands)

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/write\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_upsert\_detail.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/wc\_error\_detail.cpp](../new\_wire\_protocol\_write\_commands)

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::OpTime> const&, mongo::OpTime*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONArray> const&, mongo::BSONArray*, std::string*)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<std::string> const&, std::string*, std::string*)

- Used By:

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

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::BSONObj> const&, mongo::BSONObj*, std::string*)

- Used By:

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

    mongo::FieldParser::extractNumber(mongo::BSONObj, mongo::BSONField<int> const&, int*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_delete\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/config\_coordinator.cpp](../new\_wire\_protocol\_write\_commands)

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<bool> const&, bool*, std::string*)

- Used By:

    - [src/mongo/db/query/type\_explain.cpp](../query\_system)
    - [src/mongo/s/write\_ops/batched\_update\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/auth/privilege\_parser.cpp](../authentication)
    - [src/mongo/s/write\_ops/batched\_insert\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/type\_mongos.cpp](../sharding)
    - [src/mongo/s/write\_ops/batched\_update\_document.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_delete\_request.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<long long> const&, long long*, std::string*)

- Used By:

    - [src/mongo/s/write\_ops/batched\_request\_metadata.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/s/write\_ops/batched\_command\_response.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/query/type\_explain.cpp](../query\_system)

    mongo::FieldParser::extract(mongo::BSONObj, mongo::BSONField<mongo::OID> const&, mongo::OID*, std::string*)

- Used By:

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

    mongo::ChangelogType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

### src/mongo/s/type\_chunk.cpp

    mongo::ChunkType::min

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

    mongo::ChunkType::ConfigNS

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ChunkType::max

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

    mongo::ChunkType::toBSON() const

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

    mongo::ChunkType::DEPRECATED_lastmod

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::ChunkType::~ChunkType()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

    mongo::ChunkType::ns

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

    mongo::ChunkType::ChunkType()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

    mongo::ChunkType::shard

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

### src/mongo/s/type\_collection.cpp

    mongo::CollectionType::toBSON() const

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

    mongo::CollectionType::~CollectionType()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

    mongo::CollectionType::ns

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

    mongo::CollectionType::ConfigNS

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::CollectionType::isValid(std::string*) const

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

    mongo::CollectionType::CollectionType()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

### src/mongo/s/type\_config\_version.cpp

    mongo::VersionType::VersionType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::VersionType::clear()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

    mongo::VersionType::~VersionType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::VersionType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

    mongo::VersionType::toBSON() const

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

### src/mongo/s/type\_database.cpp

    mongo::DatabaseType::~DatabaseType()

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

    mongo::DatabaseType::DatabaseType()

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

    mongo::DatabaseType::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

    mongo::DatabaseType::ConfigNS

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::DatabaseType::isValid(std::string*) const

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

    mongo::DatabaseType::primary

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::DatabaseType::name

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

### src/mongo/s/type\_settings.cpp

    mongo::SettingsType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

    mongo::SettingsType::key

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

    mongo::SettingsType::balancerStopped

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

### src/mongo/s/type\_shard.cpp

    mongo::ShardType::name

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ShardType::~ShardType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

    mongo::ShardType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/tools/stat.cpp](../tools)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../unit\_tests)

    mongo::ShardType::ShardType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

    mongo::ShardType::draining

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ShardType::maxSize

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ShardType::toBSON() const

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

-------------

# Group Description
Bizarre legacy sharding code.   From writeback\_listener.h  "The writeback listener takes back write attempts that were made against a wrong shard.  (Wrong here in the sense that the target chunk moved before this mongos had a chance to  learn so.) It is responsible for reapplying these writes to the correct shard."   So basically, the mongos sends an operation to the mongod, and the writeback listener (running on  the mongos) says to the mongod every now and again, "yo, have I screwed up recently?". The mongod  is then like "yeah bro, you screwed up, you wrote all these things to the wrong place and the  writeback listener is like "thanks man" and tries to write them to the correct shard. Meanwhile  the user is like "I'm so glad my data was written". This should go away because of the new write  commands.   rofl

# Files
- src/mongo/s/writeback\_listener.cpp   (mongos)
- src/mongo/s/writeback\_listener.h

# Interface

### src/mongo/s/writeback\_listener.cpp

    mongo::WriteBackListener::waitFor(mongo::WriteBackListener::ConnectionIdent const&, mongo::OID const&)

- Used By:

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

    mongo::balancer

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/chunk.cpp

    mongo::ChunkManager::loadExistingRanges(std::string const&)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

    mongo::Chunk::MaxChunkSize

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::Chunk::multiSplit(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, mongo::BSONObj&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ChunkManager::hasShardKey(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::ChunkManager::createFirstChunks(std::string const&, mongo::Shard const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const*, std::vector<mongo::Shard, std::allocator<mongo::Shard> > const*)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

    mongo::Chunk::moveAndCommit(mongo::Shard const&, long long, bool, bool, int, mongo::BSONObj&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ChunkManager::ChunkManager(std::string const&, mongo::ShardKeyPattern const&, bool)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

    mongo::ChunkManager::compatibleWith(mongo::ChunkManager const&, mongo::Shard const&) const

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::Chunk::ShouldAutoSplit

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)

    mongo::ChunkManager::getShardsForQuery(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::ChunkManager::drop(boost::shared_ptr<mongo::ChunkManager const>) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::ChunkManager::findChunkForDoc(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ChunkManager::findIntersectingChunk(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ChunkManager::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Chunk::splitIfShould(long) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::ChunkRangeManager::reloadAll(std::map<mongo::BSONObj, boost::shared_ptr<mongo::Chunk const>, mongo::BSONObjCmp, std::allocator<std::pair<mongo::BSONObj const, boost::shared_ptr<mongo::Chunk const> > > > const&)

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

    mongo::ChunkManager::_printChunks() const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ChunkManager::ChunkManager(boost::shared_ptr<mongo::ChunkManager const>)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

    mongo::ChunkManager::ChunkManager()

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

    mongo::Chunk::Chunk(mongo::ChunkManager const*, mongo::BSONObj const&, mongo::BSONObj const&, mongo::Shard const&, mongo::ChunkVersion)

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

    mongo::Chunk::singleSplit(bool, mongo::BSONObj&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ChunkManager::getShardsForRange(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Chunk::setMaxChunkSizeSizeMB(int)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../mongos\_and\_mongod\_mains)

    mongo::Chunk::genID(std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

    mongo::Chunk::containsPoint(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ChunkManager::getVersion() const

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/cluster\_client\_internal.cpp

    mongo::checkClusterMongoVersions(mongo::ConnectionString const&, std::string const&)

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../unit\_tests)

### src/mongo/s/cluster\_write.cpp

    mongo::ClusterWriterStats::hasShardStats() const

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

    mongo::ClusterWriter::write(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

    mongo::ClusterWriter::ClusterWriter(bool, int)

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

    mongo::ClusterWriter::getStats()

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

    mongo::ClusterWriterStats::getShardStats() const

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../new\_wire\_protocol\_write\_commands)

### src/mongo/s/config.cpp

    mongo::ConfigServer::init(std::vector<std::string, std::allocator<std::string> >)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::configServer

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)

    mongo::DBConfig::getChunkManager(std::string const&, bool, bool)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::serverID

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::ConfigServer::reloadSettings()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::DBConfig::getShard(std::string const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::DBConfig::dropDatabase(std::string&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::DBConfig::getChunkManagerIfExists(std::string const&, bool, bool)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::ConfigServer::logChange(std::string const&, std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::DBConfig::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::DBConfig::getAllShardedCollections(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::DBConfig::setPrimary(std::string const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::DBConfig::enableSharding(bool)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::DBConfig::removeSharding(std::string const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::DBConfig::shardCollection(std::string const&, mongo::ShardKeyPattern, bool, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >*, std::vector<mongo::Shard, std::allocator<mongo::Shard> >*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::DBConfig::isSharded(std::string const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::ConfigServer::ok(bool)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::ConfigServer::replicaSetChange(mongo::ReplicaSetMonitor const*)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::DBConfig::getChunkManagerOrPrimary(std::string const&, boost::shared_ptr<mongo::ChunkManager const>&, boost::shared_ptr<mongo::Shard>&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::DBConfig::load()

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::ConfigServer::allUp(std::string&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::DBConfig::reload()

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/config\_server\_checker\_service.cpp

    mongo::startConfigServerChecker()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/cursors.cpp

    mongo::cursorCache

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::CursorCache::storeRef(std::string const&, long long, std::string const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::CursorCache::startTimeoutThread()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/d\_logic.cpp

    mongo::_handlePossibleShardedMessage(mongo::Message&, mongo::DbResponse*)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/s/d\_merge.cpp

    mongo::mergeChunks(mongo::NamespaceString const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::OID const&, bool, std::string*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)

### src/mongo/s/d\_migrate.cpp

    mongo::aboutToDeleteForSharding(mongo::StringData const&, mongo::Database const*, mongo::NamespaceDetails const*, mongo::DiskLoc const&)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

    mongo::logOpForSharding(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj const*, bool)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)

### src/mongo/s/d\_state.cpp

    mongo::ShardingState::needCollectionMetadata(std::string const&) const

- Used By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../update\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../query\_system)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)

    mongo::ShardedConnectionInfo::addHook()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)

    mongo::ShardingState::gotShardName(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)

    mongo::shardingState

- Used By:

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

    mongo::ShardingState::resetMetadata(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)

    mongo::ShardingState::getCollectionMetadata(std::string const&)

- Used By:

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

    mongo::ShardingState::initialize(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../database\_commands)

    mongo::ShardingState::refreshMetadataIfNeeded(std::string const&, mongo::ChunkVersion const&, mongo::ChunkVersion*)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

    mongo::ShardingState::setShardName(std::string const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

    mongo::ShardingState::getVersion(std::string const&) const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/db/query/new\_find.cpp](../query\_system)

    mongo::ShardedConnectionInfo::get(bool)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::ShardingState::refreshMetadataNow(std::string const&, mongo::ChunkVersion*)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../database\_commands)

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

    mongo::shardVersionOk(std::string const&, std::string&, mongo::ChunkVersion&, mongo::ChunkVersion&)

- Used By:

    - [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)

    mongo::ShardingState::resetShardingState()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs.cpp](../replication)

### src/mongo/s/default\_version.cpp

    mongo::versionManager

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::VersionManager::isVersionableCB(mongo::DBClientBase*)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/grid.cpp

    mongo::Grid::removeDBIfExists(mongo::DBConfig const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Grid::getDBConfig(mongo::StringData const&, bool, std::string const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::Grid::addShard(std::string*, mongo::ConnectionString const&, long long, std::string&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::Grid::setAllowLocalHost(bool)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::Grid::knowAboutShard(std::string const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::Grid::flushConfig()

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::grid

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../authentication)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::Grid::allowLocalHost() const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/mongos\_persistence\_stubs.cpp

    mongo::isJournalingEnabled()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

    mongo::getJournalCommitInterval()

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

    mongo::setJournalCommitInterval(unsigned int)

- Used By:

    - [src/mongo/db/commands/parameters.cpp](../database\_commands)

### src/mongo/s/request.cpp

    mongo::Request::process(int)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::Request::init()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::Request::Request(mongo::Message&, mongo::AbstractMessagingPort*)

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

### src/mongo/s/shard.cpp

    mongo::Shard::setAddress(mongo::ConnectionString const&)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

    mongo::Shard::reloadShardInfo()

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::Shard::runCommand(std::string const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::Shard::removeShard(std::string const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    vtable for mongo::ShardingConnectionHook

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::Shard::reset(std::string const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::Shard::_setAddr(std::string const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)

    mongo::Shard::getAllShards(std::vector<mongo::Shard, std::allocator<mongo::Shard> >&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

### src/mongo/s/shard\_key\_pattern.cpp

    mongo::isUniqueIndexCompatible(mongo::BSONObj, mongo::BSONObj)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)

### src/mongo/s/shardconnection.cpp

    mongo::ShardConnection::~ShardConnection()

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::ShardConnection::releaseMyConnections()

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::ShardConnection::_finishInit()

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::ShardConnection::kill()

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::ShardConnection::sync()

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ShardConnection::ShardConnection(std::string const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::ShardConnection::releaseConnectionsAfterResponse

- Used By:

    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::ShardConnection::forgetNS(std::string const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)

    mongo::shardConnectionPool

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/s/server.cpp](../mongos\_and\_mongod\_mains)

    mongo::ShardConnection::ShardConnection(mongo::Shard const&, std::string const&, boost::shared_ptr<mongo::ChunkManager const>)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::ShardConnection::done()

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/client\_info.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

### src/mongo/s/shardkey.cpp

    mongo::ShardKeyPattern::isUniqueIndexCompatible(mongo::KeyPattern const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

    mongo::ShardKeyPattern::ShardKeyPattern(mongo::BSONObj)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/dbtests/sharding.cpp](../unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../unit\_tests)

### src/mongo/s/strategy\_shard.cpp

    mongo::SHARDED

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::Strategy::useClusterWriteCommands

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)

### src/mongo/s/version\_manager.cpp

    mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/s/commands\_public.cpp](../database\_commands)

    mongo::versionManager

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

    mongo::VersionManager::isVersionableCB(mongo::DBClientBase*)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
