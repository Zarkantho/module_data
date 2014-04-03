
# Interface for Chunk Management
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/chunk.cpp

<div></div>

    mongo::ChunkManager::loadExistingRanges(std::string const&)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Chunk::MaxChunkSize

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::Chunk::multiSplit(std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&, mongo::BSONObj&) const

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::Chunk::markAsJumbo() const

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::ChunkManager::createFirstChunks(std::string const&, mongo::Shard const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const*, std::vector<mongo::Shard, std::allocator<mongo::Shard> > const*)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Chunk::toString() const

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::Chunk::moveAndCommit(mongo::Shard const&, long long, bool, bool, int, mongo::BSONObj&) const

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::ChunkManager::ChunkManager(std::string const&, mongo::ShardKeyPattern const&, bool)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ChunkManager::compatibleWith(mongo::ChunkManager const&, mongo::Shard const&) const

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Chunk::ShouldAutoSplit

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::ChunkManager::getShardsForQuery(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)

<div></div>

    mongo::Chunk::MaxObjectPerChunk

- Used By:

    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)

<div></div>

    mongo::ChunkManager::findChunkForDoc(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/mongod\_commands)

<div></div>

    mongo::ChunkManager::findIntersectingChunk(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/request.cpp](../../../../network/network\_core)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::ChunkManager::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::ChunkRangeManager::reloadAll(std::map<mongo::BSONObj, boost::shared_ptr<mongo::Chunk const>, mongo::BSONObjCmp, std::allocator<std::pair<mongo::BSONObj const, boost::shared_ptr<mongo::Chunk const> > > > const&)

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ChunkManager::ChunkManager(boost::shared_ptr<mongo::ChunkManager const>)

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ChunkManager::ChunkManager()

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Chunk::Chunk(mongo::ChunkManager const*, mongo::BSONObj const&, mongo::BSONObj const&, mongo::Shard const&, mongo::ChunkVersion)

- Used By:

    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Chunk::singleSplit(bool, mongo::BSONObj&) const

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::Chunk::refreshChunkSize()

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::Chunk::setMaxChunkSizeSizeMB(int)

- Used By:

    - [src/mongo/s/mongos\_options.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::Chunk::genID(std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/mongod\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/mongod\_commands)

<div></div>

    mongo::ChunkManager::getVersion() const

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../network/cpp\_client\_driver)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
