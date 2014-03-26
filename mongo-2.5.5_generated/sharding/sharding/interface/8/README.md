
# Interface for Config Server Schema
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/s/type\_changelog.cpp

<div></div>

    mongo::ChangelogType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

### src/mongo/s/type\_chunk.cpp

<div></div>

    mongo::ChunkType::min

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ChunkType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ChunkType::max

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ChunkType::DEPRECATED_lastmod

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ChunkType::ns

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ChunkType::shard

- Used By:

    - [src/mongo/dbtests/sharding.cpp](../../../tests/unit\_tests)

### src/mongo/s/type\_collection.cpp

<div></div>

    mongo::CollectionType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

### src/mongo/s/type\_config\_version.cpp

<div></div>

    mongo::VersionType::VersionType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/s/server.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::VersionType::clear()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::VersionType::~VersionType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/s/server.cpp](../../../process\_management/mongos\_and\_mongod\_mains)

<div></div>

    mongo::VersionType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::VersionType::toBSON() const

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

### src/mongo/s/type\_database.cpp

<div></div>

    mongo::DatabaseType::~DatabaseType()

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../security/authorization)

<div></div>

    mongo::DatabaseType::DatabaseType()

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../security/authorization)

<div></div>

    mongo::DatabaseType::parseBSON(mongo::BSONObj const&, std::string*)

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../security/authorization)

<div></div>

    mongo::DatabaseType::ConfigNS

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../security/authorization)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::DatabaseType::isValid(std::string*) const

- Used By:

    - [src/mongo/db/auth/authz\_manager\_external\_state\_s.cpp](../../../security/authorization)

### src/mongo/s/type\_mongos.cpp

<div></div>

    mongo::MongosType::toBSON() const

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::MongosType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::MongosType::~MongosType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::MongosType::MongosType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

### src/mongo/s/type\_settings.cpp

<div></div>

    mongo::SettingsType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::SettingsType::key

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::SettingsType::balancerStopped

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

### src/mongo/s/type\_shard.cpp

<div></div>

    mongo::ShardType::~ShardType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ShardType::ConfigNS

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
    - [src/mongo/tools/stat.cpp](../../../tools/tools)
    - [src/mongo/dbtests/config\_server\_fixture.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ShardType::ShardType()

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ShardType::toBSON() const

- Used By:

    - [src/mongo/dbtests/config\_upgrade\_tests.cpp](../../../tests/unit\_tests)
