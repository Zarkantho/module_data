
# Interface for Write Concern Replication Checks
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/write\_concern.cpp

<div></div>

    mongo::updateSlaveLocation(mongo::CurOp&, char const*, mongo::OpTime)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::opReplicatedEnough(mongo::OpTime, int)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::resetSlaveCache()

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::waitForReplication(mongo::OpTime, int, int)

- Used By:

    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::opReplicatedEnough(mongo::OpTime, mongo::BSONElement)

- Used By:

    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::updateSlaveLocations(mongo::BSONArray)

- Used By:

    - [src/mongo/db/repl/replset\_commands.cpp](../../../../replication/replication\_commands)
