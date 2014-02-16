
# Interface

### src/mongo/db/kill\_current\_op.cpp

<div></div>

    mongo::KillCurrentOp::reset()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)

<div></div>

    mongo::KillCurrentOp::checkForInterruptNoAssert()

- Used By:

    - [src/mongo/db/db.cpp](../../../mongos\_and\_mongod\_mains)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::checkForInterrupt(bool)

- Used By:

    - [src/mongo/db/commands/storage\_details.cpp](../../../database\_commands)
    - [src/mongo/db/commands/index\_stats.cpp](../../../database\_commands)
    - [src/mongo/db/structure/collection\_compact.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../indexing)
    - [src/mongo/db/extsort.cpp](../../../aggregation\_framework)
    - [src/mongo/db/structure/btree/btreebuilder.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/dur\_recover.cpp](../../../journaling)
    - [src/mongo/db/pdfile.cpp](../../../storage\_layer\_structure)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding)
    - [src/mongo/db/query/new\_find.cpp](../../../core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/test\_commands.cpp](../../../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../database\_commands)
    - [src/mongo/db/structure/btree/btree.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/cloner.cpp](../../../storage\_layer\_structure)
    - [src/mongo/db/commands/validate.cpp](../../../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../database\_commands)
    - [src/mongo/db/commands/touch.cpp](../../../database\_commands)
    - [src/mongo/db/write\_concern.cpp](../../../replication)

<div></div>

    mongo::KillCurrentOp::notifyAllWaiters()

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../unit\_tests)

<div></div>

    mongo::KillCurrentOp::killAll()

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../unit\_tests)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../unit\_tests)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)

<div></div>

    mongo::KillCurrentOp::kill(mongo::AtomicUInt)

- Used By:

    - [src/mongo/db/index\_builder.cpp](../../../indexing)
    - [src/mongo/db/instance.cpp](../../../storage\_layer\_structure)
