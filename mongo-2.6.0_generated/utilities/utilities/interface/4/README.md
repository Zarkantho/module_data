
# Interface for Elapsed Time
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/util/elapsed\_tracker.cpp

<div></div>

    mongo::ElapsedTracker::intervalHasElapsed()

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/plan\_executor.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ElapsedTracker::ElapsedTracker(int, int)

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/plan\_executor.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::ElapsedTracker::resetLastTime()

- Used By:

    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/plan\_executor.cpp](../../../../core\_query\_system/query\_execution)
