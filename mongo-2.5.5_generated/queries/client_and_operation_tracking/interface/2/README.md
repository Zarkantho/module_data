
# Interface for Current Operation
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/curop.cpp

<div></div>

    mongo::CurOp::ensureStarted()

- Used By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/clientlistplugin.cpp](../../../../network/web\_server)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::CurOp::enter(mongo::Client::Context*)

- Used By:

    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CurOp::reset()

- Used By:

    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/indexupdatetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_sync.cpp](../../../../replication/data\_sync)

<div></div>

    mongo::CurOp::info()

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/dbtests/counttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::CurOp::getRemainingMaxTimeMicros() const

- Used By:

    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/query/new\_find.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::OpDebug::recordStats()

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::CurOp::kill(bool*)

- Used By:

    - [src/mongo/dbtests/extsorttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CurOp::reset(mongo::HostAndPort const&, int)

- Used By:

    - [src/mongo/db/index\_builder.cpp](../../../../queries/indexing)
    - [src/mongo/dbtests/replsettests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::CurOp::getOp(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/index\_builder.cpp](../../../../queries/indexing)

<div></div>

    mongo::CurOp::~CurOp()

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::CurOp::setMessage(char const*, std::string, unsigned long long, int)

- Used By:

    - [src/mongo/db/structure/collection\_compact.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/index/btree\_based\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/get\_last\_error.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/touch.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::CurOp::setMaxTimeMicros(unsigned long long)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::CurOp::setNS(mongo::StringData const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)

<div></div>

    mongo::CurOp::CurOp(mongo::Client*, mongo::CurOp*)

- Used By:

    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../../../../network/write\_commands)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
