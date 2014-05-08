
# Interface for Write Concern Object Parser
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/write\_concern\_options.cpp

<div></div>

    mongo::WriteConcernOptions::Default

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)

<div></div>

    mongo::WriteConcernOptions::Acknowledged

- Used By:

    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/write\_ops/batch\_upconvert.cpp](../../../../network/write\_commands)

<div></div>

    mongo::WriteConcernOptions::AllConfigs

- Used By:

    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/grid.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/config.cpp](../../../../sharding/cluster\_metadata\_management)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../../sharding/config\_metadata\_upgrade)
    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../../sharding/config\_metadata\_upgrade)

<div></div>

    mongo::WriteConcernOptions::parse(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::WriteConcernOptions::Unacknowledged

- Used By:

    - [src/mongo/s/balance.cpp](../../../../sharding/balancer)
    - [src/mongo/s/write\_ops/batch\_downconvert.cpp](../../../../network/write\_commands)
