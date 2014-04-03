
# Interface for Oplog
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/repl/oplog.cpp

<div></div>

    mongo::createOplog()

- Used By:

    - [src/mongo/db/repl/rs\_initiate.cpp](../../../../replication/replica\_set\_configuration)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)

<div></div>

    mongo::newRepl()

- Used By:

    - [src/mongo/db/repl/repl\_start.cpp](../../../../replication/replication\_initialization)

<div></div>

    mongo::oplogCheckCloseDatabase(mongo::Database*)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::logOp(char const*, char const*, mongo::BSONObj const&, mongo::BSONObj*, bool*, bool, mongo::BSONObj const*)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/ops/delete.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/ops/update.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/create\_indexes.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::newReplUp()

- Used By:

    - [src/mongo/db/repl/rs.cpp](../../../../replication/replica\_set\_state)

<div></div>

    mongo::oldRepl()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/repltests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::applyOperation_inlock(mongo::BSONObj const&, bool, bool)

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/apply\_ops.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::logOpInitiate(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/repl/rs\_config.cpp](../../../../replication/replica\_set\_configuration)

<div></div>

    mongo::logKeepalive()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)

<div></div>

    mongo::logOpComment(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/oplog\_note.cpp](../../../../queries/database\_commands)
