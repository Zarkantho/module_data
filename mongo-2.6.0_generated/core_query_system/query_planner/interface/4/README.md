
# Interface for Query Explain Plan
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/explain\_plan.cpp

<div></div>

    mongo::statsToBSON(mongo::PlanStageStats const&, mongo::BSONObjBuilder*)

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)

<div></div>

    mongo::getPlanSummary(mongo::QuerySolution const&)

- Used By:

    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::getPlanInfo(mongo::QuerySolution const&, mongo::PlanInfo**)

- Used By:

    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/single\_solution\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::explainPlan(mongo::PlanStageStats const&, mongo::TypeExplain**, bool)

- Used By:

    - [src/mongo/db/query/single\_solution\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/internal\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::explainMultiPlan(mongo::PlanStageStats const&, std::vector<mongo::PlanStageStats*, std::allocator<mongo::PlanStageStats*> > const&, mongo::QuerySolution*, mongo::TypeExplain**)

- Used By:

    - [src/mongo/db/query/multi\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/cached\_plan\_runner.cpp](../../../../core\_query\_system/query\_execution)
