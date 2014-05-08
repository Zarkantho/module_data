
# Interface for Query Planner
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/planner\_access.cpp

<div></div>

    mongo::QueryPlannerAccess::buildIndexedDataAccess(mongo::CanonicalQuery const&, mongo::MatchExpression*, bool, std::vector<mongo::IndexEntry, std::allocator<mongo::IndexEntry> > const&)

- Used By:

    - [src/mongo/db/query/subplan\_runner.cpp](../../../../core\_query\_system/query\_execution)

### src/mongo/db/query/planner\_analysis.cpp

<div></div>

    mongo::QueryPlannerAnalysis::analyzeDataAccess(mongo::CanonicalQuery const&, mongo::QueryPlannerParams const&, mongo::QuerySolutionNode*)

- Used By:

    - [src/mongo/db/query/subplan\_runner.cpp](../../../../core\_query\_system/query\_execution)

### src/mongo/db/query/query\_planner.cpp

<div></div>

    mongo::QueryPlanner::tagAccordingToCache(mongo::MatchExpression*, mongo::PlanCacheIndexTree const*, std::map<mongo::BSONObj, unsigned long, std::less<mongo::BSONObj>, std::allocator<std::pair<mongo::BSONObj const, unsigned long> > > const&)

- Used By:

    - [src/mongo/db/query/subplan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::QueryPlanner::plan(mongo::CanonicalQuery const&, mongo::QueryPlannerParams const&, std::vector<mongo::QuerySolution*, std::allocator<mongo::QuerySolution*> >*)

- Used By:

    - [src/mongo/db/query/subplan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)

### src/mongo/db/query/query\_planner\_test\_lib.cpp

<div></div>

    mongo::QueryPlannerTestLib::solutionMatches(mongo::BSONObj const&, mongo::QuerySolutionNode const*)

- Used By:

    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
