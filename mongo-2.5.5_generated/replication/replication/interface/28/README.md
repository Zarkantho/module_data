
# Interface

### src/mongo/db/repl/write\_concern.cpp

<div></div>

    mongo::updateSlaveLocation(mongo::CurOp&, char const*, mongo::OpTime)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::opReplicatedEnough(mongo::OpTime, int)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::waitForReplication(mongo::OpTime, int, int)

- Used By:

    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::opReplicatedEnough(mongo::OpTime, mongo::BSONElement)

- Used By:

    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)
