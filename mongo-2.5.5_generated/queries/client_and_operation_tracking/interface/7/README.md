
# Interface for Client Cursor
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/clientcursor.cpp

<div></div>

    mongo::ClientCursorPin::ClientCursorPin(mongo::Collection const*, long long)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ClientCursor::setIdleTime(unsigned int)

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::ClientCursorPin::deleteUnderlying()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::ClientCursor::~ClientCursor()

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../queries/aggregation\_framework)

<div></div>

    mongo::ClientCursorPin::c() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::ClientCursor::ClientCursor(mongo::Collection const*, mongo::Runner*, int, mongo::BSONObj)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/parallel\_collection\_scan.cpp](../../../queries/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ClientCursor::staticYield(int, mongo::StringData const&, mongo::Record const*)

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::ClientCursor::suggestYieldMicros()

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::ClientCursor::updateSlaveLocation(mongo::CurOp&)

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)

<div></div>

    vtable for mongo::ClientCursorMonitor

- Used By:

    - [src/mongo/db/d\_globals.cpp](../../../dead\_code/legacy\_code)

<div></div>

    mongo::ClientCursor::kill()

- Used By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ClientCursorPin::~ClientCursorPin()

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/query/new\_find.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../queries/aggregation\_framework)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../tests/unit\_tests)

<div></div>

    mongo::ClientCursor::shouldTimeout(unsigned int)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../tests/unit\_tests)
    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../storage/storage\_layer\_structure)

<div></div>

    mongo::ClientCursor::ClientCursor(mongo::Collection const*)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../queries/database\_commands)

<div></div>

    mongo::ClientCursor::totalOpen()

- Used By:

    - [src/mongo/db/restapi.cpp](../../../network/web\_server)
