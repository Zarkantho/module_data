
# Interface for Shard Configuration
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/shard.cpp

<div></div>

    mongo::Shard::findIfExists(std::string const&)

- Used By:

    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../../../../sharding/routing)

<div></div>

    mongo::Shard::pick(mongo::Shard const&)

- Used By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    vtable for mongo::ShardingConnectionHook

- Used By:

    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::Shard::reset(std::string const&)

- Used By:

    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::Shard::getAllShards(std::vector<mongo::Shard, std::allocator<mongo::Shard> >&)

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::Shard::removeShard(std::string const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::Shard::lookupRSName(std::string const&)

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::Shard::runCommand(std::string const&, mongo::BSONObj const&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::Shard::_setAddr(std::string const&)

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/chunktests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Shard::getStatus() const

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::Shard::setAddress(mongo::ConnectionString const&)

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Shard::reloadShardInfo()

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)

<div></div>

    mongo::Shard::isAShardNode(std::string const&)

- Used By:

    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)
