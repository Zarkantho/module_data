
# Interface for Config Server Schema
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/type\_changelog.cpp

<div></div>

    mongo::ChangelogType::server

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ChangelogType::time

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ChangelogType::changeID

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ChangelogType::~ChangelogType()

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::ChangelogType::ConfigNS

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ChangelogType::ChangelogType()

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::ChangelogType::toBSON() const

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::ChangelogType::details

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ChangelogType::clientAddr

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ChangelogType::ns

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::ChangelogType::what

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

### src/mongo/s/type\_chunk.cpp

<div></div>

    mongo::ChunkType::jumbo

- Used By:

    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)
    - [src/mongo/s/balancer\_policy.cpp](../../../../sharding/balancer)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::name

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::min

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/balancer\_policy.cpp](../../../../sharding/balancer)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::ConfigNS

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::max

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/balancer\_policy.cpp](../../../../sharding/balancer)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/balancer\_policy\_tests.cpp](../../../../sharding/balancer)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::toBSON() const

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::DEPRECATED_lastmod

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::isValid(std::string*) const

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::ChunkType::~ChunkType()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::ChunkType::ns

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::ChunkType()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::shard

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/dbtests/sharding.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ChunkType::cloneTo(mongo::ChunkType*) const

- Used By:

    - [src/mongo/s/d\_merge.cpp](../../../../sharding/chunk\_management)

### src/mongo/s/type\_collection.cpp

<div></div>

    mongo::CollectionType::DEPRECATED_lastmodEpoch

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::CollectionType::toBSON() const

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::CollectionType::noBalance

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::CollectionType::CollectionType()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::CollectionType::keyPattern

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::CollectionType::unique

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::CollectionType::DEPRECATED_lastmod

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::CollectionType::~CollectionType()

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::CollectionType::ns

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::CollectionType::primary

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::CollectionType::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::CollectionType::dropped

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::CollectionType::ConfigNS

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CollectionType::isValid(std::string*) const

- Used By:

    - [src/mongo/dbtests/merge\_chunk\_tests.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/metadata\_loader.cpp](../../../../sharding/mongod\_sharding\_metadata)

### src/mongo/s/type\_config\_version.cpp

<div></div>

    mongo::VersionType::VersionType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::version_DEPRECATED

- Used By:

    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::upgradeId

- Used By:

    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::clear()

- Used By:

    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::VersionType::~VersionType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/server.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::minCompatibleVersion

- Used By:

    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::currentVersion

- Used By:

    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::isValid(std::string*) const

- Used By:

    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::excludingMongoVersions

- Used By:

    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::toBSON() const

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::cloneTo(mongo::VersionType*) const

- Used By:

    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::VersionType::upgradeState

- Used By:

    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)

### src/mongo/s/type\_database.cpp

<div></div>

    mongo::DatabaseType::~DatabaseType()

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)

<div></div>

    mongo::DatabaseType::DatabaseType()

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)

<div></div>

    mongo::DatabaseType::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)

<div></div>

    mongo::DatabaseType::DEPRECATED_partitioned

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::DatabaseType::ConfigNS

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::DatabaseType::DEPRECATED_sharded

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::DatabaseType::isValid(std::string*) const

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../../security/authorization)

<div></div>

    mongo::DatabaseType::primary

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::DatabaseType::name

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

### src/mongo/s/type\_lockpings.cpp

<div></div>

    mongo::LockpingsType::ping

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::LockpingsType::ConfigNS

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::LockpingsType::process

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

### src/mongo/s/type\_locks.cpp

<div></div>

    mongo::LocksType::process

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::LocksType::state

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::LocksType::name

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::LocksType::lockID

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::LocksType::ConfigNS

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::LocksType::who

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

<div></div>

    mongo::LocksType::why

- Used By:

    - [src/mongo/s/distlock.cpp](../../../../sharding/cluster\_locking)

### src/mongo/s/type\_mongos.cpp

<div></div>

    mongo::MongosType::name

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::MongosType::mongoVersion

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::MongosType::toBSON() const

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MongosType::ConfigNS

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MongosType::up

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::MongosType::~MongosType()

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MongosType::ping

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::MongosType::MongosType()

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MongosType::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::MongosType::waiting

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

### src/mongo/s/type\_settings.cpp

<div></div>

    mongo::SettingsType::ConfigNS

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::SettingsType::shortBalancerSleep

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::SettingsType::key

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::SettingsType::secondaryThrottle

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::SettingsType::balancerActiveWindow

- Used By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)

<div></div>

    mongo::SettingsType::balancerStopped

- Used By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::SettingsType::chunksize

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

### src/mongo/s/type\_shard.cpp

<div></div>

    mongo::ShardType::host

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ShardType::name

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ShardType::~ShardType()

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ShardType::ConfigNS

- Used By:

    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/tools/stat.cpp](../../../../tools/tools)
    - [src/mongo/s/config\_upgrade.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ShardType::ShardType()

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ShardType::tags

- Used By:

    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ShardType::draining

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ShardType::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::ShardType::maxSize

- Used By:

    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/shard.cpp](../../../../sharding/shard\_abstraction)

<div></div>

    mongo::ShardType::toBSON() const

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ShardType::isValid(std::string*) const

- Used By:

    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

### src/mongo/s/type\_tags.cpp

<div></div>

    mongo::TagsType::min

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::TagsType::ConfigNS

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::TagsType::tag

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::TagsType::ns

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)

<div></div>

    mongo::TagsType::max

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
