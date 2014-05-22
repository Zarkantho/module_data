
# Interface for Query Plan Stage Implementations
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/exec/and\_hash.cpp

<div></div>

    mongo::AndHashStage::getMemUsage() const

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::AndHashStage::AndHashStage(mongo::WorkingSet*, mongo::MatchExpression const*, unsigned long)

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::AndHashStage::addChild(mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::AndHashStage::AndHashStage(mongo::WorkingSet*, mongo::MatchExpression const*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)

### src/mongo/db/exec/and\_sorted.cpp

<div></div>

    mongo::AndSortedStage::AndSortedStage(mongo::WorkingSet*, mongo::MatchExpression const*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::AndSortedStage::addChild(mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)

### src/mongo/db/exec/collection\_scan.cpp

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)

### src/mongo/db/exec/count.cpp

<div></div>

    mongo::Count::recoverFromYield()

- Used By:

    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Count::work(unsigned long*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Count::prepareToYield()

- Used By:

    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::Count::Count(mongo::CountParams const&, mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)

<div></div>

    vtable for mongo::Count

- Used By:

    - [src/mongo/dbtests/query\_stage\_count.cpp](../../../../tests/unit\_tests)

### src/mongo/db/exec/distinct\_scan.cpp

<div></div>

    mongo::DistinctScan::DistinctScan(mongo::DistinctParams const&, mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_distinct.cpp](../../../../tests/unit\_tests)

### src/mongo/db/exec/fetch.cpp

<div></div>

    mongo::FetchStage::FetchStage(mongo::WorkingSet*, mongo::PlanStage*, mongo::MatchExpression const*)

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

### src/mongo/db/exec/index\_scan.cpp

<div></div>

    mongo::IndexScan::IndexScan(mongo::IndexScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/dbhash.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../query\_and\_operation\_handling/indexing)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

### src/mongo/db/exec/keep\_mutations.cpp

<div></div>

    mongo::KeepMutationsStage::KeepMutationsStage(mongo::MatchExpression const*, mongo::WorkingSet*, mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_keep.cpp](../../../../tests/unit\_tests)

### src/mongo/db/exec/limit.cpp

<div></div>

    mongo::LimitStage::LimitStage(int, mongo::WorkingSet*, mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../../../../tests/unit\_tests)

### src/mongo/db/exec/merge\_sort.cpp

<div></div>

    mongo::MergeSortStage::addChild(mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MergeSortStage::MergeSortStage(mongo::MergeSortStageParams const&, mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)

### src/mongo/db/exec/mock\_stage.cpp

<div></div>

    mongo::MockStage::pushBack(mongo::WorkingSetMember const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MockStage::MockStage(mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MockStage::pushBack(mongo::PlanStage::StageState)

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../../../../tests/unit\_tests)

### src/mongo/db/exec/oplogstart.cpp

<div></div>

    mongo::OplogStart::_backwardsScanTime

- Used By:

    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::OplogStart::OplogStart(std::string const&, mongo::MatchExpression*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

### src/mongo/db/exec/skip.cpp

<div></div>

    mongo::SkipStage::SkipStage(int, mongo::WorkingSet*, mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../../../../tests/unit\_tests)

### src/mongo/db/exec/sort.cpp

<div></div>

    mongo::SortStage::SortStage(mongo::SortStageParams const&, mongo::WorkingSet*, mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
