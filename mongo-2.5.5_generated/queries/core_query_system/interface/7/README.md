
# Interface

### src/mongo/db/exec/and\_hash.cpp

<div></div>

    mongo::AndHashStage::AndHashStage(mongo::WorkingSet*, mongo::MatchExpression const*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)

<div></div>

    mongo::AndHashStage::addChild(mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)

### src/mongo/db/exec/and\_sorted.cpp

<div></div>

    mongo::AndSortedStage::AndSortedStage(mongo::WorkingSet*, mongo::MatchExpression const*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)

<div></div>

    mongo::AndSortedStage::addChild(mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)

### src/mongo/db/exec/collection\_scan.cpp

<div></div>

    mongo::CollectionScan::CollectionScan(mongo::CollectionScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

### src/mongo/db/exec/fetch.cpp

<div></div>

    mongo::FetchStage::FetchStage(mongo::WorkingSet*, mongo::PlanStage*, mongo::MatchExpression const*)

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

### src/mongo/db/exec/index\_scan.cpp

<div></div>

    mongo::IndexScan::IndexScan(mongo::IndexScanParams const&, mongo::WorkingSet*, mongo::MatchExpression const*)

- Used By:

    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

### src/mongo/db/exec/limit.cpp

<div></div>

    mongo::LimitStage::LimitStage(int, mongo::WorkingSet*, mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)

### src/mongo/db/exec/merge\_sort.cpp

<div></div>

    mongo::MergeSortStage::addChild(mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)

<div></div>

    mongo::MergeSortStage::MergeSortStage(mongo::MergeSortStageParams const&, mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)

### src/mongo/db/exec/mock\_stage.cpp

<div></div>

    mongo::MockStage::pushBack(mongo::WorkingSetMember const&)

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)

<div></div>

    mongo::MockStage::MockStage(mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)

<div></div>

    mongo::MockStage::pushBack(mongo::PlanStage::StageState)

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)

### src/mongo/db/exec/oplogstart.cpp

<div></div>

    mongo::OplogStart::_backwardsScanTime

- Used By:

    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)

<div></div>

    mongo::OplogStart::OplogStart(std::string const&, mongo::MatchExpression*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)

### src/mongo/db/exec/skip.cpp

<div></div>

    mongo::SkipStage::SkipStage(int, mongo::WorkingSet*, mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)

### src/mongo/db/exec/sort.cpp

<div></div>

    mongo::SortStage::SortStage(mongo::SortStageParams const&, mongo::WorkingSet*, mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)

### src/mongo/db/exec/working\_set.cpp

<div></div>

    mongo::WorkingSetMember::WorkingSetMember()

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)

<div></div>

    mongo::WorkingSetMember::~WorkingSetMember()

- Used By:

    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)

<div></div>

    mongo::WorkingSet::~WorkingSet()

- Used By:

    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)

<div></div>

    mongo::WorkingSet::WorkingSet()

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/catalog/database.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/s/d\_migrate.cpp](../sharding)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/dbtests/query\_stage\_limit\_skip.cpp](../unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

<div></div>

    mongo::WorkingSetMember::hasObj() const

- Used By:

    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)

<div></div>

    mongo::WorkingSetMember::getFieldDotted(std::string const&, mongo::BSONElement*) const

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)

<div></div>

    mongo::WorkingSet::getFlagged() const

- Used By:

    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)

<div></div>

    mongo::WorkingSetMember::hasLoc() const

- Used By:

    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
