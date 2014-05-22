
# Interface for Cluster Write
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/cluster\_write.cpp

<div></div>

    mongo::clusterInsert(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ClusterWriterStats::hasShardStats() const

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ClusterWriter::write(mongo::BatchedCommandRequest const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)

<div></div>

    mongo::clusterCreateIndex(std::string const&, mongo::BSONObj, bool, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::clusterDelete(std::string const&, mongo::BSONObj const&, int, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ClusterWriterStats::getShardStats() const

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ClusterWriter::ClusterWriter(bool, int)

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)

<div></div>

    mongo::ClusterWriter::getStats()

- Used By:

    - [src/mongo/s/commands/cluster\_write\_cmd.cpp](../../../../network/write\_commands)

<div></div>

    mongo::clusterUpdate(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, bool, bool, mongo::BSONObj const&, mongo::BatchedCommandResponse*)

- Used By:

    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../../sharding/config\_metadata\_upgrade)
