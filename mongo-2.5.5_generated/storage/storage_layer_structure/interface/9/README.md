
# Interface

### src/mongo/db/catalog/collection\_cursor\_cache.cpp

<div></div>

    mongo::CollectionCursorCache::registerRunner(mongo::Runner*)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/internal\_runner.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::CollectionCursorCache::invalidateDocument(mongo::DiskLoc const&, mongo::InvalidationType)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)

<div></div>

    mongo::CollectionCursorCache::deregisterCursor(mongo::ClientCursor*)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::CollectionCursorCache::find(long long)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::CollectionCursorCache::getCursorIds(std::set<long long, std::less<long long>, std::allocator<long long> >*)

- Used By:

    - [src/mongo/db/range\_deleter\_db\_env.cpp](../sharding)

<div></div>

    mongo::CollectionCursorCache::numCursors()

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::CollectionCursorCache::deregisterRunner(mongo::Runner*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../core\_query\_system)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../core\_query\_system)
    - [src/mongo/db/query/internal\_runner.cpp](../core\_query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

<div></div>

    mongo::CollectionCursorCache::registerCursor(mongo::ClientCursor*)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::CollectionCursorCache::eraseCursorGlobal(long long)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)

<div></div>

    mongo::CollectionCursorCache::invalidateAll(bool)

- Used By:

    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::CollectionCursorCache::timeoutCursorsGlobal(unsigned int)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
