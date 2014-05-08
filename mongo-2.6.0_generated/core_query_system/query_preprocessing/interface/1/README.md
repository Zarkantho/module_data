
# Interface for Lite Parsed Query
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/lite\_parsed\_query.cpp

<div></div>

    mongo::LiteParsedQuery::isTextScoreMeta(mongo::BSONElement)

- Used By:

    - [src/mongo/db/exec/sort.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::LiteParsedQuery::parseMaxTimeMSQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::LiteParsedQuery::metaDiskLoc

- Used By:

    - [src/mongo/db/exec/projection\_exec.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::LiteParsedQuery::normalizeSortOrder(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/query/query\_solution.cpp](../../../../core\_query\_system/query\_planner)
    - [src/mongo/db/query/query\_planner.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::LiteParsedQuery::isQueryIsolated(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/ops/delete\_executor.cpp](../../../../core\_query\_system/delete\_operations)
    - [src/mongo/db/ops/update.cpp](../../../../core\_query\_system/update\_system)

<div></div>

    mongo::LiteParsedQuery::cmdOptionMaxTimeMS

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)
    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../core\_query\_system/aggregation\_framework)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)

<div></div>

    mongo::LiteParsedQuery::metaGeoNearPoint

- Used By:

    - [src/mongo/db/exec/projection\_exec.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::LiteParsedQuery::metaGeoNearDistance

- Used By:

    - [src/mongo/db/exec/projection\_exec.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/commands/geonear.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::LiteParsedQuery::metaIndexKey

- Used By:

    - [src/mongo/db/exec/projection\_exec.cpp](../../../../core\_query\_system/query\_execution)

<div></div>

    mongo::LiteParsedQuery::parseMaxTimeMSCommand(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../query\_and\_operation\_handling/database\_commands)

<div></div>

    mongo::LiteParsedQuery::metaTextScore

- Used By:

    - [src/mongo/db/exec/projection\_exec.cpp](../../../../core\_query\_system/query\_execution)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../core\_query\_system/full\_text\_search\_module)
