
# Interface for TODO: Name this group
This interface information represents symbols that are defined in this group but used in other modules.  Does not include symbols defined in this group that are used inside this module.

### src/mongo/db/query/canonical\_query.cpp

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, long long, long long, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/ops/update\_driver.cpp](../../../../queries/update\_system)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/group.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::CanonicalQuery::isSimpleIdQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/query/eof\_runner.cpp

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)

### src/mongo/db/query/explain\_plan.cpp

<div></div>

    mongo::statsToBSON(mongo::PlanStageStats const&, mongo::BSONObjBuilder*)

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)

### src/mongo/db/query/get\_runner.cpp

<div></div>

    mongo::ScopedRunnerRegistration::ScopedRunnerRegistration(mongo::Runner*)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/group.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::getRunner(mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../queries/full\_text\_search\_module)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/group.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::ScopedRunnerRegistration::~ScopedRunnerRegistration()

- Used By:

    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/mr.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/group.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::getRunnerDistinct(mongo::Collection*, mongo::BSONObj const&, std::string const&, mongo::Runner**)

- Used By:

    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)

### src/mongo/db/query/internal\_runner.cpp

<div></div>

    mongo::InternalRunner::InternalRunner(mongo::Collection const*, mongo::PlanStage*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/db/repl/replication\_server\_status.cpp](../../../../replication/replica\_set\_state)
    - [src/mongo/db/commands/dbhash.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/test\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/dbtests/namespacetests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/db.cpp](../../../../process\_management/mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../../../../replication/data\_sync)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../../../../replication/master\_slave)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../../../../queries/client\_and\_operation\_tracking)
    - [src/mongo/db/commands/validate.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../../../../queries/indexing)
    - [src/mongo/s/d\_split.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/s/d\_migrate.cpp](../../../../sharding/chunk\_management)

### src/mongo/db/query/lite\_parsed\_query.cpp

<div></div>

    mongo::LiteParsedQuery::isTextScoreMeta(mongo::BSONElement)

- Used By:

    - [src/mongo/client/parallel.cpp](../../../../sharding/routing)

<div></div>

    mongo::LiteParsedQuery::parseMaxTimeMSQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/strategy.cpp](../../../../network/network\_core)

<div></div>

    mongo::LiteParsedQuery::cmdOptionMaxTimeMS

- Used By:

    - [src/mongo/s/commands\_public.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)
    - [src/mongo/s/chunk.cpp](../../../../sharding/chunk\_management)
    - [src/mongo/db/pipeline/pipeline.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::LiteParsedQuery::metaGeoNearPoint

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::LiteParsedQuery::metaGeoNearDistance

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::LiteParsedQuery::parseMaxTimeMSCommand(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../../../../sharding/mongos\_commands)
    - [src/mongo/db/dbcommands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::LiteParsedQuery::metaTextScore

- Used By:

    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../queries/full\_text\_search\_module)

### src/mongo/db/query/multi\_plan\_runner.cpp

<div></div>

    mongo::MultiPlanRunner::getNext(mongo::BSONObj*, mongo::DiskLoc*)

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MultiPlanRunner::MultiPlanRunner(mongo::Collection const*, mongo::CanonicalQuery*)

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MultiPlanRunner::~MultiPlanRunner()

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MultiPlanRunner::pickBestPlan(unsigned long*)

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::MultiPlanRunner::addPlan(mongo::QuerySolution*, mongo::PlanStage*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../../../../tests/unit\_tests)

### src/mongo/db/query/new\_find.cpp

<div></div>

    mongo::MaxBytesToReturnToClientAtOnce

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/pipeline\_command.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::newGetMore(char const*, int, long long, mongo::CurOp&, int, bool&, bool*)

- Used By:

    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::newRunQuery(mongo::Message&, mongo::QueryMessage&, mongo::CurOp&, mongo::Message&)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/db/instance.cpp](../../../../storage/storage\_layer\_structure)

### src/mongo/db/query/plan\_cache.cpp

<div></div>

    mongo::PlanCache::notifyOfWriteOp()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::PlanCache::remove(mongo::CanonicalQuery const&)

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::SolutionCacheData::toString() const

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::PlanCache::~PlanCache()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::PlanCache::clear()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)
    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::PlanCache::getEntry(mongo::CanonicalQuery const&, mongo::PlanCacheEntry**) const

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::PlanCache::PlanCache(std::string const&)

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::PlanCache::getAllEntries() const

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::PlanCacheEntry::~PlanCacheEntry()

- Used By:

    - [src/mongo/db/commands/plan\_cache\_commands.cpp](../../../../queries/database\_commands)

### src/mongo/db/query/plan\_executor.cpp

<div></div>

    mongo::PlanExecutor::PlanExecutor(mongo::WorkingSet*, mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::PlanExecutor::getNext(mongo::BSONObj*, mongo::DiskLoc*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)

<div></div>

    mongo::PlanExecutor::~PlanExecutor()

- Used By:

    - [src/mongo/dbtests/query\_stage\_tests.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../../../../tests/unit\_tests)

### src/mongo/db/query/query\_settings.cpp

<div></div>

    mongo::QuerySettings::clearAllowedIndices()

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::AllowedIndexEntry::~AllowedIndexEntry()

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::QuerySettings::setAllowedIndices(mongo::CanonicalQuery const&, std::vector<mongo::BSONObj, std::allocator<mongo::BSONObj> > const&)

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::QuerySettings::QuerySettings()

- Used By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::QuerySettings::~QuerySettings()

- Used By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::QuerySettings::removeAllowedIndices(mongo::CanonicalQuery const&)

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::QuerySettings::getAllAllowedIndices() const

- Used By:

    - [src/mongo/db/commands/index\_filter\_commands.cpp](../../../../queries/database\_commands)

### src/mongo/db/query/single\_solution\_runner.cpp

<div></div>

    mongo::SingleSolutionRunner::SingleSolutionRunner(mongo::Collection const*, mongo::CanonicalQuery*, mongo::QuerySolution*, mongo::PlanStage*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../../../../tests/unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../../../../tests/unit\_tests)

### src/mongo/db/query/type\_explain.cpp

<div></div>

    mongo::TypeExplain::scanAndOrder

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::getAllPlansAt(unsigned long) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::clauses

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::sizeAllPlans() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::isIndexBoundsSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::sizeClauses() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::isMultiKey

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::getCursor() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::TypeExplain::getScanAndOrder() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::getNScannedObjects() const

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../queries/full\_text\_search\_module)

<div></div>

    mongo::TypeExplain::isAllPlansSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::getNScanned() const

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../../../../queries/full\_text\_search\_module)

<div></div>

    mongo::TypeExplain::isIsMultiKeySet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::indexBounds

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::isScanAndOrderSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::isClausesSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::getN() const

- Used By:

    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::TypeExplain::getIsMultiKey() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::getClausesAt(unsigned long) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::isCursorSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)
    - [src/mongo/db/commands/distinct.cpp](../../../../queries/database\_commands)

<div></div>

    mongo::TypeExplain::getIndexBounds() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::allPlans

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)

<div></div>

    mongo::TypeExplain::cursor

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../../../../queries/aggregation\_framework)
