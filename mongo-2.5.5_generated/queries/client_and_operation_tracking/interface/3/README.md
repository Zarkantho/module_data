
# Interface for Kill Current Operation
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/kill\_current\_op.cpp

<div></div>

    mongo::KillCurrentOp::reset()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KillCurrentOp::checkForInterruptNoAssert()

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/extsort.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/pdfile.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)
    - [src/mongo/db/query/new\_find.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/write\_concern.cpp](../../../../replication/replication)

<div></div>

    mongo::KillCurrentOp::notifyAllWaiters()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KillCurrentOp::killAll()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::kill(mongo::AtomicUInt)

- Used By:

    - [src/mongo/db/index\_builder.cpp](../../../../queries/indexing)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
