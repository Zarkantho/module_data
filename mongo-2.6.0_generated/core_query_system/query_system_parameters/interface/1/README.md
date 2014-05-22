
# Interface for Query Knobs
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/query\_knobs.cpp

<div></div>

    mongo::internalQueryEnumerationMaxOrSolutions

- Used By:

    - [src/mongo/db/query/query\_planner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryCacheSize

- Used By:

    - [src/mongo/db/query/plan\_cache.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryPlanEvaluationMaxResults

- Used By:

    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::internalQueryPlanEvaluationCollFraction

- Used By:

    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::internalQueryCacheFeedbacksStored

- Used By:

    - [src/mongo/db/query/plan\_cache.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryForceIntersectionPlans

- Used By:

    - [src/mongo/db/query/plan\_ranker.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::internalQueryPlanEvaluationWorks

- Used By:

    - [src/mongo/db/query/plan\_ranker.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::internalQueryEnumerationMaxIntersectPerAnd

- Used By:

    - [src/mongo/db/query/query\_planner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryPlannerEnableIndexIntersection

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryCacheStdDeviations

- Used By:

    - [src/mongo/db/query/plan\_cache.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryPlanOrChildrenIndependently

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryCacheWriteOpsBetweenFlush

- Used By:

    - [src/mongo/db/query/plan\_cache.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryPlannerMaxIndexedSolutions

- Used By:

    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
