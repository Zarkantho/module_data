
# Interface

### src/mongo/db/write\_concern\_options.cpp

<div></div>

    mongo::WriteConcernOptions::Default

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../sharding)

<div></div>

    mongo::WriteConcernOptions::AllConfigs

- Used By:

    - [src/mongo/s/config.cpp](../../../sharding)
    - [src/mongo/s/grid.cpp](../../../sharding)
    - [src/mongo/s/balance.cpp](../../../sharding)
    - [src/mongo/s/commands\_admin.cpp](../../../sharding)
    - [src/mongo/s/chunk.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp](../../../sharding)
    - [src/mongo/s/cluster\_client\_internal.cpp](../../../sharding)
    - [src/mongo/s/config\_upgrade\_helpers.cpp](../../../sharding)

<div></div>

    mongo::WriteConcernOptions::parse(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/get\_last\_error.cpp](../../../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../new\_wire\_protocol\_write\_commands)

<div></div>

    mongo::WriteConcernOptions::Unacknowledged

- Used By:

    - [src/mongo/s/balance.cpp](../../../sharding)
