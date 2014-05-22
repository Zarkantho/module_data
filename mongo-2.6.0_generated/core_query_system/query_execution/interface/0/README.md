
# Interface for Query Plan Executor
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/plan\_executor.cpp

<div></div>

    mongo::PlanExecutor::~PlanExecutor()

- Used By:

    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::PlanExecutor::getNext(mongo::BSONObj*, mongo::DiskLoc*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::PlanExecutor::PlanExecutor(mongo::WorkingSet*, mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
