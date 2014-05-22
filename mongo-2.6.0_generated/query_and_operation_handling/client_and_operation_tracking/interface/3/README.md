
# Interface for Kill Current Operation
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/kill\_current\_op.cpp

<div></div>

    mongo::KillCurrentOp::checkForInterruptNoAssert()

- Used By:

    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::killAll()

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KillCurrentOp::reset()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Used By:

    - [src/mongo/db/write\_concern.cpp](../../../../replication/write\_concern)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repair\_database.cpp](../../../../storage/repair\_database)
    - [src/mongo/db/cloner.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/commands/touch.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dur\_recover.cpp](../../../../storage/journaling)
    - [src/mongo/db/structure/btree/btree.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/db/extsort.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/commands/storage\_details.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::KillCurrentOp::kill(mongo::AtomicUInt)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
