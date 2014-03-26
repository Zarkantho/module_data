
# Interface for Collection Cursor Cache
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/catalog/collection\_cursor\_cache.cpp

<div></div>

    mongo::CollectionCursorCache::registerRunner(mongo::Runner*)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/internal\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)

<div></div>

    mongo::CollectionCursorCache::invalidateDocument(mongo::DiskLoc const&, mongo::InvalidationType)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../../queries/core\_query\_system)

<div></div>

    mongo::CollectionCursorCache::deregisterCursor(mongo::ClientCursor*)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::CollectionCursorCache::find(long long)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::CollectionCursorCache::getCursorIds(std::set<long long, std::less<long long>, std::allocator<long long> >*)

- Used By:

    - [src/mongo/db/range\_deleter\_db\_env.cpp](../../../../sharding/sharding)

<div></div>

    mongo::CollectionCursorCache::numCursors()

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CollectionCursorCache::deregisterRunner(mongo::Runner*)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/get\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/db/query/internal\_runner.cpp](../../../../queries/core\_query\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/sharding)

<div></div>

    mongo::CollectionCursorCache::registerCursor(mongo::ClientCursor*)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)

<div></div>

    mongo::CollectionCursorCache::eraseCursorGlobal(long long)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CollectionCursorCache::invalidateAll(bool)

- Used By:

    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::CollectionCursorCache::timeoutCursorsGlobal(unsigned int)

- Used By:

    - [src/mongo/db/clientcursor.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
