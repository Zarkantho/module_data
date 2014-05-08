
# Interface for Master Slave
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/master\_slave.cpp

<div></div>

    mongo::replAllDead

- Used By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/ttl.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/repl/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)
    - [src/mongo/db/repl/repl\_reads\_ok.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_state.cpp](../../../../sharding/mongod\_sharding\_metadata)

<div></div>

    mongo::relinquishSyncingSome

- Used By:

    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::startMasterSlave()

- Used By:

    - [src/mongo/db/repl/repl\_start.cpp](../../../../replication/replication\_initialization)

<div></div>

    mongo::DatabaseIgnorer::ignoreAt(std::string const&, mongo::OpTime const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::syncing

- Used By:

    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::replInfo

- Used By:

    - [src/mongo/db/restapi.cpp](../../../../network/web\_server)

<div></div>

    mongo::DatabaseIgnorer::doIgnoreUntilAfter(std::string const&, mongo::OpTime const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ReplSource::ReplSource(mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ReplSource::applyOperation(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::ReplSource::forceResyncDead(char const*)

- Used By:

    - [src/mongo/db/repl/resync.cpp](../../../../replication/data\_sync)
