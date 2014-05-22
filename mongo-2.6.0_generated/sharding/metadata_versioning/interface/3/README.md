
# Interface for Shard Version Manager
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/version\_manager.cpp

<div></div>

    mongo::versionManager

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::VersionManager::resetShardVersionCB(mongo::DBClientBase*)

- Used By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::VersionManager::checkShardVersionCB(mongo::DBClientBase*, std::string const&, bool, int)

- Used By:

    - [src/mongo/s/write\_ops/dbclient\_safe\_writer.cpp](../../../../network/write\_commands)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::VersionManager::isVersionableCB(mongo::DBClientBase*)

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::VersionManager::initShardVersionCB(mongo::DBClientBase*, mongo::BSONObj&)

- Used By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::VersionManager::checkShardVersionCB(mongo::ShardConnection*, bool, int)

- Used By:

    - [src/mongo/s/shardconnection.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::VersionManager::forceRemoteCheckShardVersionCB(std::string const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)
    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)
