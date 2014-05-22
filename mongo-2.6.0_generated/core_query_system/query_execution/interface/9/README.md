
# Interface for Cache Aware Query Runners
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/cached\_plan\_runner.cpp

<div></div>

    mongo::CachedPlanRunner::setBackupPlan(mongo::QuerySolution*, mongo::PlanStage*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::CachedPlanRunner::CachedPlanRunner(mongo::Collection const*, mongo::CanonicalQuery*, mongo::QuerySolution*, mongo::PlanStage*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

### src/mongo/db/query/multi\_plan\_runner.cpp

<div></div>

    mongo::MultiPlanRunner::getNext(mongo::BSONObj*, mongo::DiskLoc*)

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MultiPlanRunner::pickBestPlan(unsigned long*, mongo::BSONObj*)

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MultiPlanRunner::~MultiPlanRunner()

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MultiPlanRunner::addPlan(mongo::QuerySolution*, mongo::PlanStage*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MultiPlanRunner::hasBackupPlan() const

- Used By:

    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MultiPlanRunner::cacheBestPlan()

- Used By:

    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MultiPlanRunner::MultiPlanRunner(mongo::Collection const*, mongo::CanonicalQuery*)

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
