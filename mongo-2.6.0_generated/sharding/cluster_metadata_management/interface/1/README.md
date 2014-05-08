
# Interface for Database And Collection Configuration
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/config.cpp

<div></div>

    mongo::ConfigServer::init(std::vector<std::string, std::allocator<std::string> >)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::Shard::EMPTY

- Used By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::configServer

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/dbclient\_shard\_resolver.cpp](../../../../sharding/routing)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::DBConfig::getChunkManager(std::string const&, bool, bool)

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::serverID

- Used By:

    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/writeback\_listener.cpp](../../../../sharding/writeback\_listener)

<div></div>

    mongo::ConfigServer::reloadSettings()

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::DBConfig::getShard(std::string const&)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConfig::dropDatabase(std::string&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConfig::getChunkManagerIfExists(std::string const&, bool, bool)

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::DBConfig::getChunkManagerOrPrimary(std::string const&, boost::shared_ptr<mongo::ChunkManager const>&, boost::shared_ptr<mongo::Shard>&)

- Used By:

    - [src/mongo/s/cluster\_write.cpp](../../../../sharding/routing)
    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::ConfigServer::logChange(std::string const&, std::string const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::DBConfig::getAllShards(std::set<mongo::Shard, std::less<mongo::Shard>, std::allocator<mongo::Shard> >&) const

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConfig::getAllShardedCollections(std::set<std::string, std::less<std::string>, std::allocator<std::string> >&) const

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConfig::setPrimary(std::string const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ConfigServer::init(std::string const&)

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::DBConfig::enableSharding(bool)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConfig::removeSharding(std::string const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConfig::shardCollection(std::string const&, mongo::ShardKeyPattern, bool, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> >*, std::vector<mongo::Shard, std::allocator<mongo::Shard> >*)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConfig::isSharded(std::string const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ConfigServer::ok(bool)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::DBConfig::load()

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::ConfigServer::allUp()

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ConfigServer::allUp(std::string&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DBConfig::reload()

- Used By:

    - [src/mongo/s/chunk\_manager\_targeter.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/version\_manager.cpp](../../../../sharding/metadata\_versioning)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ConfigServer::replicaSetChange(std::string const&, std::string const&)

- Used By:

    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
