
# Interface for Collection Info Cache
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/db/catalog/collection\_info\_cache.cpp

<div></div>

    mongo::CollectionInfoCache::computeIndexKeys()

- Used By:

    - [src/mongo/db/ops/update\_lifecycle\_impl.cpp](../../../queries/update\_system)

<div></div>

    mongo::CollectionInfoCache::getQuerySettings() const

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../queries/database\_commands)

<div></div>

    mongo::CollectionInfoCache::getPlanCache() const

- Used By:

    - [src/mongo/db/query/cached\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../queries/database\_commands)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../queries/database\_commands)
