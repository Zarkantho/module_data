
# Interface for Cache Aware Query Runners
This dependency information represents symbols that are used in this group but defined in other modules.  Does not include symbols used in this group that are defined inside this module.

### src/mongo/db/query/cached\_plan\_runner.cpp

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::uasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::CollectionInfoCache::getPlanCache() const

- Provided By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::PlanCache::feedback(mongo::CanonicalQuery const&, mongo::PlanCacheEntryFeedback*)

- Provided By:

    - [src/mongo/db/query/plan\_cache.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::explainMultiPlan(mongo::PlanStageStats const&, std::vector<mongo::PlanStageStats*, std::allocator<mongo::PlanStageStats*> > const&, mongo::QuerySolution*, mongo::TypeExplain**)

- Provided By:

    - [src/mongo/db/query/explain\_plan.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::uasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::verboseQueryLogging

- Provided By:

    - [src/mongo/db/query/qlog.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::msgasserted(int, std::string const&)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::PlanRanker::scoreTree(mongo::PlanStageStats const*)

- Provided By:

    - [src/mongo/db/query/plan\_ranker.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::Status::toString() const

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::getPlanInfo(mongo::QuerySolution const&, mongo::PlanInfo**)

- Provided By:

    - [src/mongo/db/query/explain\_plan.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    std::string mongo::integerToHex<int>(int)

- Provided By:

    - [src/mongo/util/hex.cpp](../../../../utilities/utilities)

### src/mongo/db/query/multi\_plan\_runner.cpp

<div></div>

    mongo::ElapsedTracker::ElapsedTracker(int, int)

- Provided By:

    - [src/mongo/util/elapsed\_tracker.cpp](../../../../utilities/utilities)

<div></div>

    mongo::currentClient

- Provided By:

    - [src/mongo/db/client.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
    - [src/mongo/s/s\_only.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    boost::system::system_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::Record::likelyInPhysicalMemory(char const*)

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::getThreadName()

- Provided By:

    - [src/mongo/util/concurrency/thread\_name.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Collection::numRecords() const

- Provided By:

    - [src/mongo/db/catalog/collection.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::PlanCache::shouldCacheQuery(mongo::CanonicalQuery const&)

- Provided By:

    - [src/mongo/db/query/plan\_cache.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryPlanEvaluationMaxResults

- Provided By:

    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)

<div></div>

    boost::system::generic_category()

- Provided By:

    - [src/third\_party/boost/libs/system/src/error\_code.cpp](../../../../third\_party/boost\_system)

<div></div>

    mongo::msgasserted(int, char const*)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::ElapsedTracker::intervalHasElapsed()

- Provided By:

    - [src/mongo/util/elapsed\_tracker.cpp](../../../../utilities/utilities)

<div></div>

    mongo::Status::Status(mongo::ErrorCodes::Error, char const*, int)

- Provided By:

    - [src/mongo/base/status.cpp](../../../../utilities/base\_utilites)

<div></div>

    mongo::PlanRanker::pickBestPlan(std::vector<mongo::CandidatePlan, std::allocator<mongo::CandidatePlan> > const&, mongo::PlanRankingDecision*)

- Provided By:

    - [src/mongo/db/query/plan\_ranker.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::PlanCache::add(mongo::CanonicalQuery const&, std::vector<mongo::QuerySolution*, std::allocator<mongo::QuerySolution*> > const&, mongo::PlanRankingDecision*)

- Provided By:

    - [src/mongo/db/query/plan\_cache.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::logger::LogstreamBuilder::makeStream()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::explainMultiPlan(mongo::PlanStageStats const&, std::vector<mongo::PlanStageStats*, std::allocator<mongo::PlanStageStats*> > const&, mongo::QuerySolution*, mongo::TypeExplain**)

- Provided By:

    - [src/mongo/db/query/explain\_plan.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryPlanEvaluationCollFraction

- Provided By:

    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)

<div></div>

    mongo::verifyFailed(char const*, char const*, unsigned int)

- Provided By:

    - [src/mongo/util/assert\_util.cpp](../../../../utilities/utilities)

<div></div>

    mongo::logger::globalLogManager()

- Provided By:

    - [src/mongo/logger/logger.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::PlanCache::remove(mongo::CanonicalQuery const&)

- Provided By:

    - [src/mongo/db/query/plan\_cache.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::Database::getCollection(mongo::StringData const&)

- Provided By:

    - [src/mongo/db/catalog/database.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::Record::touch(bool) const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::logger::LogstreamBuilder::LogstreamBuilder(mongo::logger::LogDomain<mongo::logger::MessageEventEphemeral>*, std::string const&, mongo::logger::LogSeverity)

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::logger::LogstreamBuilder::~LogstreamBuilder()

- Provided By:

    - [src/mongo/logger/logstream\_builder.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::CollectionCursorCache::deregisterRunner(mongo::Runner*)

- Provided By:

    - [src/mongo/db/catalog/collection\_cursor\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::CollectionInfoCache::getPlanCache() const

- Provided By:

    - [src/mongo/db/catalog/collection\_info\_cache.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::getPlanSummary(mongo::QuerySolution const&)

- Provided By:

    - [src/mongo/db/query/explain\_plan.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::ElapsedTracker::resetLastTime()

- Provided By:

    - [src/mongo/util/elapsed\_tracker.cpp](../../../../utilities/utilities)

<div></div>

    mongo::DiskLoc::rec() const

- Provided By:

    - [src/mongo/db/storage/record.cpp](../../../../storage/storage\_layer\_structure)

<div></div>

    mongo::verboseQueryLogging

- Provided By:

    - [src/mongo/db/query/qlog.cpp](../../../../process\_management/logging\_system)

<div></div>

    mongo::ClientCursor::staticYield(int, mongo::StringData const&, mongo::Record const*)

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)

<div></div>

    mongo::getPlanInfo(mongo::QuerySolution const&, mongo::PlanInfo**)

- Provided By:

    - [src/mongo/db/query/explain\_plan.cpp](../../../../core\_query\_system/query\_planner)

<div></div>

    mongo::internalQueryPlanEvaluationWorks

- Provided By:

    - [src/mongo/db/query/query\_knobs.cpp](../../../../core\_query\_system/query\_system\_parameters)

<div></div>

    mongo::ClientCursor::suggestYieldMicros()

- Provided By:

    - [src/mongo/db/clientcursor.cpp](../../../../query\_and\_operation\_handling/client\_and\_operation\_tracking)
