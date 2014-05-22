
# Interface for Canonical Query
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/canonical\_query.cpp

<div></div>

    mongo::CanonicalQuery::getPlanCacheKey() const

- Used By:

    - [src/mongo/db/query/query\_settings.cpp](../../../../core\_query\_system/query\_system\_parameters)
    - [src/mongo/db/query/plan\_cache.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::CanonicalQuery::isSimpleIdQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/ops/update\_executor.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/query/idhack\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../core\_query\_system/query\_system\_commands)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, long long, long long, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../core\_query\_system/full\_text\_search\_module)

<div></div>

    mongo::CanonicalQuery::toStringShort() const

- Used By:

    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/db/ops/update\_driver.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/dbtests/plan\_ranking.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ops/update\_executor.cpp](../../../../core\_query\_system/update\_system)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/commands/group.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::CanonicalQuery::countNodes(mongo::MatchExpression const*, mongo::MatchExpression::MatchType)

- Used By:

    - [src/mongo/db/query/plan\_enumerator.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::CanonicalQuery::toString() const

- Used By:

    - [src/mongo/db/query/subplan\_runner.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)
    - [src/mongo/db/query/query\_planner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/query/get\_runner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::CanonicalQuery::canonicalize(mongo::QueryMessage const&, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/db/query/new\_find.cpp](../../../../core\_query\_system/query\_system\_entry\_points)

<div></div>

    mongo::CanonicalQuery::sortTree(mongo::MatchExpression*)

- Used By:

    - [src/mongo/db/query/query\_planner.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/query/query\_planner\_test\_lib.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::CanonicalQuery::canonicalize(mongo::CanonicalQuery const&, mongo::MatchExpression*, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/db/query/subplan\_runner.cpp](../../../../core\_query\_system/query\_execution)
