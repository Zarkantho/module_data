
# Interface for Elapsed Time
This interface information represents symbols thatare defined in this group but used in other modules.  Does not includesymbols defined in this group that are used inside this module.

### src/mongo/util/elapsed\_tracker.cpp

<div></div>

    mongo::ElapsedTracker::resetLastTime()

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../../../queries/core\_query\_system)

<div></div>

    mongo::ElapsedTracker::intervalHasElapsed()

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../../../queries/core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)

<div></div>

    mongo::ElapsedTracker::ElapsedTracker(int, int)

- Used By:

    - [src/mongo/db/ops/update.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/catalog/index\_create.cpp](../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../queries/core\_query\_system)
    - [src/mongo/db/query/plan\_executor.cpp](../../../queries/core\_query\_system)
    - [src/mongo/s/d\_migrate.cpp](../../../sharding/sharding)
