
# Interface for Mongod Migration Commands
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/s/d\_migrate.cpp

<div></div>

    mongo::ShardingState::inCriticalMigrateSection()

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::ShardingState::waitTillNotInCriticalSection(int)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::logOpForSharding(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, mongo::BSONObj const*, bool)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../../../../replication/data\_sync)
