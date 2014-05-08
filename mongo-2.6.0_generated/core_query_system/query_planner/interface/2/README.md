
# Interface for Query Plan Cache
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/plan\_cache.cpp

<div></div>

    mongo::PlanCache::notifyOfWriteOp()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::PlanCache::shouldCacheQuery(mongo::CanonicalQuery const&)

- Used By:

    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::PlanCache::add(mongo::CanonicalQuery const&, std::vector<mongo::QuerySolution*, std::allocator<mongo::QuerySolution*> > const&, mongo::PlanRankingDecision*)

- Used By:

    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::PlanCache::remove(mongo::CanonicalQuery const&)

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::SolutionCacheData::toString() const

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::PlanCache::contains(mongo::CanonicalQuery const&) const

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::PlanCache::feedback(mongo::CanonicalQuery const&, mongo::PlanCacheEntryFeedback*)

- Used By:

    - [src/mongo/db/query/cached\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::PlanCacheIndexTree::clone() const

- Used By:

    - [src/mongo/db/query/subplan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::PlanCache::~PlanCache()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::PlanCache::clear()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::PlanCache::getEntry(mongo::CanonicalQuery const&, mongo::PlanCacheEntry**) const

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::PlanCache::PlanCache(std::string const&)

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::PlanCache::getAllEntries() const

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::PlanCacheEntry::~PlanCacheEntry()

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
