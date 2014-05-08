
# Interface for Get Query Runner
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/get\_runner.cpp

<div></div>

    mongo::getRunner(mongo::Collection*, mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Used By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::getRunner(mongo::Collection*, std::string const&, mongo::BSONObj const&, mongo::Runner**, mongo::CanonicalQuery**, unsigned long)

- Used By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::ScopedRunnerRegistration::ScopedRunnerRegistration(mongo::Runner*)

- Used By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/ops/count.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::getRunner(mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../core\_query\_system/full\_text\_search\_module)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::getRunnerCount(mongo::Collection*, mongo::BSONObj const&, mongo::BSONObj const&, mongo::Runner**)

- Used By:

    - [src/mongo/db/ops/count.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::ScopedRunnerRegistration::~ScopedRunnerRegistration()

- Used By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/ops/count.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::getRunnerAlwaysPlan(mongo::Collection*, mongo::CanonicalQuery*, mongo::QueryPlannerParams const&, mongo::Runner**)

- Used By:

    - [src/mongo/db/query/subplan\_runner.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::fillOutPlannerParams(mongo::Collection*, mongo::CanonicalQuery*, mongo::QueryPlannerParams*)

- Used By:

    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::getRunnerDistinct(mongo::Collection*, mongo::BSONObj const&, std::string const&, mongo::Runner**)

- Used By:

    - [src/mongo/db/commands/distinct.cpp](../../../../query\_and\_operation\_handling/database\_commands)
