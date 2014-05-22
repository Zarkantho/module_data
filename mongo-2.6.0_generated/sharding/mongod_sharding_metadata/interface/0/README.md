
# Interface for Global Sharding State
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/d\_state.cpp

<div></div>

    mongo::ShardingState::initialize(std::string const&)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardedConnectionInfo::addHook()

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)

<div></div>

    mongo::shardVersionOk(std::string const&, std::string&, mongo::ChunkVersion&, mongo::ChunkVersion&)

- Used By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)

<div></div>

    mongo::ShardingState::resetShardingState()

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardedConnectionInfo::get(bool)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_logic.cpp](../../../../sharding/writeback\_listener)
    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardingState::needCollectionMetadata(std::string const&) const

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::ShardingState::getCollectionMetadata(std::string const&)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/query/stage\_builder.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ShardingState::forgetPending(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::OID const&, std::string*)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardingState::splitChunk(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, mongo::ChunkVersion)

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::shardingState

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/stage\_builder.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::ShardingState::donateChunk(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::ChunkVersion)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::haveLocalShardingInfo(std::string const&)

- Used By:

    - [src/mongo/scripting/v8\_db.cpp](../../../../javascript/javascript\_libraries)

<div></div>

    mongo::usingAShardConnection(std::string const&)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ShardingState::resetMetadata(std::string const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardingState::mergeChunks(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::ChunkVersion)

- Used By:

    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardingState::refreshMetadataIfNeeded(std::string const&, mongo::ChunkVersion const&, mongo::ChunkVersion*)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ShardingState::getVersion(std::string const&) const

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardingState::gotShardName(std::string const&)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardingState::setShardName(std::string const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ShardingState::undoDonateChunk(std::string const&, boost::shared_ptr<mongo::CollectionMetadata const>)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardingState::refreshMetadataNow(std::string const&, mongo::ChunkVersion*)

- Used By:

    - [src/mongo/db/commands/cleanup\_orphaned\_cmd.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ShardingState::notePending(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::OID const&, std::string*)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
