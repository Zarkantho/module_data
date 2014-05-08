
# Interface for Query Plan
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/plan\_ranker.cpp

<div></div>

    mongo::PlanRanker::pickBestPlan(std::vector<mongo::CandidatePlan, std::allocator<mongo::CandidatePlan> > const&, mongo::PlanRankingDecision*)

- Used By:

    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::PlanRanker::scoreTree(mongo::PlanStageStats const*)

- Used By:

    - [src/mongo/db/query/cached\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
