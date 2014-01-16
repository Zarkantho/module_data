# query\_system

# Module Groups

-------------

# Group Description
Matcher expressions. The point of all of this is to take a query string and turn it into a  structured set of classes. If this were a compiler this would be the parse tree for the compiler.

# Files
- src/mongo/db/matcher/expression.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression.h
- src/mongo/db/matcher/expression\_array.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_array.h
- src/mongo/db/matcher/expression\_array\_test.cpp   ()
- src/mongo/db/matcher/expression\_geo.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_geo.h
- src/mongo/db/matcher/expression\_geo\_test.cpp   ()
- src/mongo/db/matcher/expression\_leaf.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_leaf.h
- src/mongo/db/matcher/expression\_leaf\_test.cpp   ()
- src/mongo/db/matcher/expression\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_parser.h
- src/mongo/db/matcher/expression\_parser\_array\_test.cpp   ()
- src/mongo/db/matcher/expression\_parser\_geo.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_parser\_geo\_test.cpp   ()
- src/mongo/db/matcher/expression\_parser\_leaf\_test.cpp   ()
- src/mongo/db/matcher/expression\_parser\_test.cpp   ()
- src/mongo/db/matcher/expression\_parser\_text.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_parser\_text\_test.cpp   ()
- src/mongo/db/matcher/expression\_parser\_tree.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_parser\_tree\_test.cpp   ()
- src/mongo/db/matcher/expression\_test.cpp   ()
- src/mongo/db/matcher/expression\_text.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_text.h
- src/mongo/db/matcher/expression\_tree.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_tree.h
- src/mongo/db/matcher/expression\_tree\_test.cpp   ()
- src/mongo/db/matcher/expression\_where.cpp   (mongod, tools, mongos)

# Interface

### src/mongo/db/matcher/expression\_parser.cpp

<div></div>

    mongo::MatchExpressionParser::_parse(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - src/mongo/db/modules/subscription/src/audit/audit\_manager\_global.cpp
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/db/auth/authz\_manager\_external\_state\_mock.cpp](../authentication)
    - [src/mongo/db/ops/modifier\_pull.cpp](../update\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

-------------

# Group Description
This is the code to say "does this document match the expression"? This is built on the  expressions above.  Helper classes for managing document matching. Related to the expressions above.

# Files
- src/mongo/db/matcher/matchable.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/matchable.h
- src/mongo/db/matcher/path.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/path.h
- src/mongo/db/matcher/path\_internal.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/path\_internal.h
- src/mongo/db/matcher/path\_test.cpp   ()

# Interface

### src/mongo/db/matcher/path.cpp

<div></div>

    mongo::BSONElementIterator::BSONElementIterator()

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authentication.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_indexes\_collections\_databases.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_replset.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_shutdown.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_application\_message.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_sharding.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::BSONElementIterator::~BSONElementIterator()

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_authentication.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_indexes\_collections\_databases.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_user\_management.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_replset.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_shutdown.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_application\_message.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_authz\_check.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_sharding.cpp
    - src/mongo/db/modules/subscription/src/audit/audit\_role\_management.cpp

<div></div>

    mongo::BSONElementIterator::BSONElementIterator(mongo::ElementPath const*, mongo::BSONObj const&)

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp

<div></div>

    mongo::BSONElementIterator::reset(mongo::ElementPath const*, mongo::BSONObj const&)

- Used By:

    - src/mongo/db/modules/subscription/src/audit/audit\_event.cpp

-------------

# Group Description
Interface to actually test if a document matches.

# Files
- src/mongo/db/matcher/matcher.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/matcher.h
- src/mongo/db/matcher.h

# Interface

### src/mongo/db/matcher/matcher.cpp

<div></div>

    mongo::Matcher2::matches(mongo::BSONObj const&, mongo::MatchDetails*) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

<div></div>

    mongo::Matcher2::Matcher2(mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/db/pipeline/document\_source\_match.cpp](../aggregation\_framework)
    - [src/mongo/db/curop.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)
    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)
    - [src/mongo/tools/restore.cpp](../tools)
    - [src/mongo/tools/tool.cpp](../tools)
    - [src/mongo/db/commands/apply\_ops.cpp](../database\_commands)

-------------

# Group Description
Helper for requesting more details about what matched our query from the matcher system.

# Files
- src/mongo/db/matcher/match\_details.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/match\_details.h

# Interface

### src/mongo/db/matcher/match\_details.cpp

<div></div>

    mongo::MatchDetails::elemMatchKey() const

- Used By:

    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)

<div></div>

    mongo::MatchDetails::MatchDetails()

- Used By:

    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)

<div></div>

    mongo::MatchDetails::hasElemMatchKey() const

- Used By:

    - [src/mongo/dbtests/matchertests.cpp](../unit\_tests)

-------------

# Group Description
Planning/parsing/optimization for new query framework   not execution as well? (what are all these *runner.cpp files?)

# Files
- src/mongo/db/query/cached\_plan\_runner.cpp   (mongod, tools)
- src/mongo/db/query/cached\_plan\_runner.h
- src/mongo/db/query/canonical\_query.cpp   (mongod, tools, mongos)
- src/mongo/db/query/canonical\_query.h
- src/mongo/db/query/eof\_runner.cpp   (mongod, tools)
- src/mongo/db/query/eof\_runner.h
- src/mongo/db/query/explain\_plan.cpp   (mongod, tools)
- src/mongo/db/query/explain\_plan.h
- src/mongo/db/query/find\_constants.h
- src/mongo/db/query/get\_runner.cpp   (mongod, tools)
- src/mongo/db/query/get\_runner.h
- src/mongo/db/query/idhack\_runner.cpp   (mongod, tools)
- src/mongo/db/query/idhack\_runner.h
- src/mongo/db/query/index\_bounds.cpp   (mongod, tools, mongos)
- src/mongo/db/query/index\_bounds.h
- src/mongo/db/query/index\_bounds\_builder.cpp   (mongod, tools, mongos)
- src/mongo/db/query/index\_bounds\_builder.h
- src/mongo/db/query/index\_bounds\_builder\_test.cpp   ()
- src/mongo/db/query/index\_bounds\_test.cpp   ()
- src/mongo/db/query/index\_entry.h
- src/mongo/db/query/index\_tag.cpp   (mongod, tools, mongos)
- src/mongo/db/query/index\_tag.h
- src/mongo/db/query/indexability.h
- src/mongo/db/query/internal\_plans.h
- src/mongo/db/query/internal\_runner.cpp   (mongod, tools)
- src/mongo/db/query/internal\_runner.h
- src/mongo/db/query/interval.cpp   (mongod, tools, mongos)
- src/mongo/db/query/interval.h
- src/mongo/db/query/interval\_test.cpp   ()
- src/mongo/db/query/lite\_parsed\_query.cpp   (mongod, tools, mongos)
- src/mongo/db/query/lite\_parsed\_query.h
- src/mongo/db/query/lite\_parsed\_query\_test.cpp   ()
- src/mongo/db/query/multi\_plan\_runner.cpp   (mongod, tools)
- src/mongo/db/query/multi\_plan\_runner.h
- src/mongo/db/query/new\_find.cpp   (mongod, tools)
- src/mongo/db/query/new\_find.h
- src/mongo/db/query/parsed\_projection.cpp   (mongod, tools, mongos)
- src/mongo/db/query/parsed\_projection.h
- src/mongo/db/query/parsed\_projection\_test.cpp   ()
- src/mongo/db/query/plan\_cache.cpp   (mongod, tools, mongos)
- src/mongo/db/query/plan\_cache.h
- src/mongo/db/query/plan\_cache\_test.cpp   ()
- src/mongo/db/query/plan\_enumerator.cpp   (mongod, tools, mongos)
- src/mongo/db/query/plan\_enumerator.h
- src/mongo/db/query/plan\_executor.cpp   (mongod, tools)
- src/mongo/db/query/plan\_executor.h
- src/mongo/db/query/plan\_ranker.cpp   (mongod, tools)
- src/mongo/db/query/plan\_ranker.h
- src/mongo/db/query/planner\_access.cpp   (mongod, tools, mongos)
- src/mongo/db/query/planner\_access.h
- src/mongo/db/query/planner\_analysis.cpp   (mongod, tools, mongos)
- src/mongo/db/query/planner\_analysis.h
- src/mongo/db/query/planner\_ixselect.cpp   (mongod, tools, mongos)
- src/mongo/db/query/planner\_ixselect.h
- src/mongo/db/query/planner\_ixselect\_test.cpp   ()
- src/mongo/db/query/qlog.cpp   (mongod, tools, mongos)
- src/mongo/db/query/qlog.h
- src/mongo/db/query/query\_planner.cpp   (mongod, tools, mongos)
- src/mongo/db/query/query\_planner.h
- src/mongo/db/query/query\_planner\_common.h
- src/mongo/db/query/query\_planner\_params.h
- src/mongo/db/query/query\_planner\_test.cpp   ()
- src/mongo/db/query/query\_solution.cpp   (mongod, tools, mongos)
- src/mongo/db/query/query\_solution.h
- src/mongo/db/query/runner.h
- src/mongo/db/query/runner\_yield\_policy.h
- src/mongo/db/query/single\_solution\_runner.cpp   (mongod, tools)
- src/mongo/db/query/single\_solution\_runner.h
- src/mongo/db/query/stage\_builder.cpp   (mongod, tools)
- src/mongo/db/query/stage\_builder.h
- src/mongo/db/query/stage\_types.h
- src/mongo/db/query/type\_explain.cpp   (mongod, tools)
- src/mongo/db/query/type\_explain.h

# Interface

### src/mongo/db/query/canonical\_query.cpp

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::BSONObj const&, mongo::BSONObj const&, long long, long long, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)

<div></div>

    mongo::CanonicalQuery::canonicalize(std::string const&, mongo::BSONObj const&, mongo::CanonicalQuery**)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/ops/update\_driver.cpp](../update\_system)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/commands/group.cpp](../database\_commands)

### src/mongo/db/query/eof\_runner.cpp

<div></div>

    mongo::EOFRunner::EOFRunner(mongo::CanonicalQuery*, std::string const&)

- Used By:

    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)

### src/mongo/db/query/get\_runner.cpp

<div></div>

    mongo::getRunner(mongo::CanonicalQuery*, mongo::Runner**, unsigned long)

- Used By:

    - [src/mongo/dbtests/documentsourcetests.cpp](../unit\_tests)
    - [src/mongo/db/pipeline/pipeline\_d.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/db/commands/group.cpp](../database\_commands)

<div></div>

    mongo::DeregisterEvenIfUnderlyingCodeThrows::~DeregisterEvenIfUnderlyingCodeThrows()

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/commands/mr.cpp](../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/commands/group.cpp](../database\_commands)

### src/mongo/db/query/internal\_runner.cpp

<div></div>

    mongo::InternalRunner::InternalRunner(std::string const&, mongo::PlanStage*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/s/d\_split.cpp](../sharding)
    - [src/mongo/db/repl/replication\_server\_status.cpp](../replication)
    - [src/mongo/db/commands/dbhash.cpp](../database\_commands)
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
    - [src/mongo/db/index/haystack\_access\_method.cpp](../indexing)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/s/d\_migrate.cpp](../sharding)

### src/mongo/db/query/lite\_parsed\_query.cpp

<div></div>

    mongo::LiteParsedQuery::isTextScoreMeta(mongo::BSONElement)

- Used By:

    - [src/mongo/client/parallel.cpp](../cpp\_client\_driver)

<div></div>

    mongo::LiteParsedQuery::parseMaxTimeMSQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/strategy\_shard.cpp](../sharding)

<div></div>

    mongo::LiteParsedQuery::cmdOptionMaxTimeMS

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/s/chunk.cpp](../sharding)
    - [src/mongo/db/pipeline/pipeline.cpp](../aggregation\_framework)

<div></div>

    mongo::LiteParsedQuery::metaGeoNearPoint

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../database\_commands)

<div></div>

    mongo::LiteParsedQuery::metaGeoNearDistance

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../database\_commands)

<div></div>

    mongo::LiteParsedQuery::parseMaxTimeMSCommand(mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_admin.cpp](../database\_commands)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)

<div></div>

    mongo::LiteParsedQuery::metaTextScore

- Used By:

    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

### src/mongo/db/query/multi\_plan\_runner.cpp

<div></div>

    mongo::MultiPlanRunner::getNext(mongo::BSONObj*, mongo::DiskLoc*)

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)

<div></div>

    mongo::MultiPlanRunner::MultiPlanRunner(mongo::CanonicalQuery*)

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)

<div></div>

    mongo::MultiPlanRunner::~MultiPlanRunner()

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)

<div></div>

    mongo::MultiPlanRunner::pickBestPlan(unsigned long*)

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)

<div></div>

    mongo::MultiPlanRunner::addPlan(mongo::QuerySolution*, mongo::PlanStage*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)

### src/mongo/db/query/new\_find.cpp

<div></div>

    mongo::MaxBytesToReturnToClientAtOnce

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/pipeline\_command.cpp](../database\_commands)

<div></div>

    mongo::newGetMore(char const*, int, long long, mongo::CurOp&, int, bool&, bool*)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::newRunQuery(mongo::Message&, mongo::QueryMessage&, mongo::CurOp&, mongo::Message&)

- Used By:

    - [src/mongo/dbtests/querytests.cpp](../unit\_tests)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/db/query/plan\_cache.cpp

<div></div>

    mongo::PlanCache::clear()

- Used By:

    - [src/mongo/db/structure/collection\_info\_cache.cpp](../storage\_layer\_structure)

<div></div>

    mongo::PlanCache::~PlanCache()

- Used By:

    - [src/mongo/db/structure/collection.cpp](../storage\_layer\_structure)

### src/mongo/db/query/plan\_executor.cpp

<div></div>

    mongo::PlanExecutor::PlanExecutor(mongo::WorkingSet*, mongo::PlanStage*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)

<div></div>

    mongo::PlanExecutor::getNext(mongo::BSONObj*, mongo::DiskLoc*)

- Used By:

    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)

<div></div>

    mongo::PlanExecutor::~PlanExecutor()

- Used By:

    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)

### src/mongo/db/query/single\_solution\_runner.cpp

<div></div>

    mongo::SingleSolutionRunner::SingleSolutionRunner(mongo::CanonicalQuery*, mongo::QuerySolution*, mongo::PlanStage*, mongo::WorkingSet*)

- Used By:

    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)

### src/mongo/db/query/type\_explain.cpp

<div></div>

    mongo::TypeExplain::getScanAndOrder() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::scanAndOrder

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::getAllPlansAt(unsigned long) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::clauses

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::sizeAllPlans() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::sizeClauses() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::isMultiKey

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::isIndexBoundsSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::isIsMultiKeySet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::getCursor() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)

<div></div>

    mongo::TypeExplain::getNScannedObjects() const

- Used By:

    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)
    - [src/mongo/db/commands/geonear.cpp](../database\_commands)

<div></div>

    mongo::TypeExplain::isAllPlansSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::getNScanned() const

- Used By:

    - [src/mongo/db/commands/geonear.cpp](../database\_commands)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)
    - [src/mongo/db/fts/fts\_command\_mongod.cpp](../full\_text\_search\_module)

<div></div>

    mongo::TypeExplain::indexBounds

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::isCursorSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)
    - [src/mongo/db/commands/distinct.cpp](../database\_commands)

<div></div>

    mongo::TypeExplain::isScanAndOrderSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::isClausesSet() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::getN() const

- Used By:

    - [src/mongo/db/commands/distinct.cpp](../database\_commands)

<div></div>

    mongo::TypeExplain::getClausesAt(unsigned long) const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::getIndexBounds() const

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::allPlans

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

<div></div>

    mongo::TypeExplain::cursor

- Used By:

    - [src/mongo/db/pipeline/document\_source\_cursor.cpp](../aggregation\_framework)

-------------

# Group Description
Executor for new query framework   oh. what is the relationship between 'runners' and e.g. 'index\_scan'   here?

# Files
- src/mongo/db/exec/2d.cpp   (mongod, tools)
- src/mongo/db/exec/2d.h
- src/mongo/db/exec/2dcommon.cpp   (mongod, tools)
- src/mongo/db/exec/2dcommon.h
- src/mongo/db/exec/2dnear.cpp   (mongod, tools)
- src/mongo/db/exec/2dnear.h
- src/mongo/db/exec/and\_common-inl.h
- src/mongo/db/exec/and\_hash.cpp   (mongod, tools)
- src/mongo/db/exec/and\_hash.h
- src/mongo/db/exec/and\_sorted.cpp   (mongod, tools)
- src/mongo/db/exec/and\_sorted.h
- src/mongo/db/exec/collection\_scan.cpp   (mongod, tools)
- src/mongo/db/exec/collection\_scan.h
- src/mongo/db/exec/collection\_scan\_common.h
- src/mongo/db/exec/fetch.cpp   (mongod, tools)
- src/mongo/db/exec/fetch.h
- src/mongo/db/exec/filter.h
- src/mongo/db/exec/index\_scan.cpp   (mongod, tools)
- src/mongo/db/exec/index\_scan.h
- src/mongo/db/exec/limit.cpp   (mongod, tools)
- src/mongo/db/exec/limit.h
- src/mongo/db/exec/merge\_sort.cpp   (mongod, tools)
- src/mongo/db/exec/merge\_sort.h
- src/mongo/db/exec/mock\_stage.cpp   ()
- src/mongo/db/exec/mock\_stage.h
- src/mongo/db/exec/oplogstart.cpp   (mongod, tools)
- src/mongo/db/exec/oplogstart.h
- src/mongo/db/exec/or.cpp   (mongod, tools)
- src/mongo/db/exec/or.h
- src/mongo/db/exec/plan\_stage.h
- src/mongo/db/exec/plan\_stats.h
- src/mongo/db/exec/projection.cpp   (mongod, tools)
- src/mongo/db/exec/projection.h
- src/mongo/db/exec/projection\_exec.cpp   (mongod, tools)
- src/mongo/db/exec/projection\_exec.h
- src/mongo/db/exec/projection\_exec\_test.cpp   ()
- src/mongo/db/exec/s2near.cpp   (mongod, tools)
- src/mongo/db/exec/s2near.h
- src/mongo/db/exec/shard\_filter.cpp   (mongod, tools)
- src/mongo/db/exec/shard\_filter.h
- src/mongo/db/exec/skip.cpp   (mongod, tools)
- src/mongo/db/exec/skip.h
- src/mongo/db/exec/sort.cpp   (mongod, tools)
- src/mongo/db/exec/sort.h
- src/mongo/db/exec/sort\_test.cpp   ()
- src/mongo/db/exec/stagedebug\_cmd.cpp   (mongod, tools)
- src/mongo/db/exec/text.cpp   (mongod, tools)
- src/mongo/db/exec/text.h
- src/mongo/db/exec/working\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/exec/working\_set.h
- src/mongo/db/exec/working\_set\_common.cpp   (mongod, tools)
- src/mongo/db/exec/working\_set\_common.h
- src/mongo/db/exec/working\_set\_computed\_data.h
- src/mongo/db/exec/working\_set\_test.cpp   ()

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
    - [src/mongo/db/commands/test\_commands.cpp](../database\_commands)
    - [src/mongo/dbtests/namespacetests.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/db/catalog/index\_create.cpp](../storage\_layer\_structure)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/validate.cpp](../database\_commands)
    - [src/mongo/dbtests/query\_stage\_collscan.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/collection\_to\_capped.cpp](../database\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/db.cpp](../mongos\_and\_mongod\_mains)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
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

    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/runner\_registry.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_and.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_fetch.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_single\_solution\_runner.cpp](../unit\_tests)
    - [src/mongo/dbtests/query\_stage\_merge\_sort.cpp](../unit\_tests)
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
    - [src/mongo/dbtests/query\_multi\_plan\_runner.cpp](../unit\_tests)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/dbtests/query\_stage\_tests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/dbtests/oplogstarttests.cpp](../unit\_tests)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
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
    - [src/mongo/db/index/btree\_based\_builder.cpp](../indexing)
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

-------------

# Group Description
Legacy utilities for managing queries. Has utilities like range intersection and application of  skip and limit. These are allllmost dead. The functionality should be replaced by the new  matcher, expressions, and query system.

# Files
- src/mongo/db/queryutil-inl.h
- src/mongo/db/queryutil.cpp   (mongod, tools, mongos)
- src/mongo/db/queryutil.h

# Interface

### src/mongo/db/queryutil.cpp

<div></div>

    mongo::FieldRangeVectorIterator::FieldIntervalMatcher::FieldIntervalMatcher(mongo::FieldInterval const&, mongo::BSONElement const&, bool)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRange::operator|=(mongo::FieldRange const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::OrRangeGenerator::popOrClauseSingleKey()

- Used By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::FieldRangeSet::toString() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeVectorIterator::prepDive()

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeVector::FieldRangeVector(mongo::FieldRangeSet const&, mongo::BSONObj, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRange::operator-=(mongo::FieldRange const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldInterval::toString() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeVector::startKey() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeVector::endKey() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeVector::startKeyInclusive() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeVectorIterator::FieldIntervalMatcher::upperCmp() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSet::subset(mongo::BSONObj const&) const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::isSimpleIdQuery(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

<div></div>

    mongo::FieldRangeVectorIterator::advance(mongo::BSONObj const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSetPair::frsForIndex(mongo::NamespaceDetails const*, int) const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRange::isPointIntervalSet() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeVectorIterator::FieldIntervalMatcher::lowerCmp() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSet::universalRange() const

- Used By:

    - [src/mongo/db/keypattern.cpp](../indexing)
    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::FieldRange::universal() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)
    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::FieldRangeVectorIterator::CompoundRangeCounter::CompoundRangeCounter(int, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSetPair::operator&=(mongo::FieldRangeSetPair const&)

- Used By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::FieldRangeSetPair::operator-=(mongo::FieldRangeSet const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeVector::isSingleInterval() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRange::toString() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSetPair::assertValidIndex(mongo::NamespaceDetails const*, int) const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSetPair::noNonUniversalRanges() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRange::FieldRange(mongo::BSONElement const&, bool, bool)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRange::intersect(mongo::FieldRange const&, bool)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeVectorIterator::FieldRangeVectorIterator(mongo::FieldRangeVector const&, int)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSet::operator&=(mongo::FieldRangeSet const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSet::FieldRangeSet(char const*, mongo::BSONObj const&, bool, bool)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSet::getSpecial() const

- Used By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::FieldRangeVector::toString() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSet::numNonUniversalRanges() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeVector::endKeyInclusive() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::applySkipLimit(long long, mongo::BSONObj const&)

- Used By:

    - [src/mongo/s/commands\_public.cpp](../database\_commands)

<div></div>

    mongo::FieldRangeSet::operator-=(mongo::FieldRangeSet const&)

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::FieldRangeSetPair::toString() const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

<div></div>

    mongo::OrRangeGenerator::OrRangeGenerator(char const*, mongo::BSONObj const&, bool)

- Used By:

    - [src/mongo/s/chunk.cpp](../sharding)

<div></div>

    mongo::FieldRangeSet::prefixed(std::string const&) const

- Used By:

    - [src/mongo/dbtests/queryutiltests.cpp](../unit\_tests)

-------------

# Group Description
Old way of doing document projections. Given a doc and a projection, transforms the document.   what calls it, and where are projections done now?

# Files
- src/mongo/db/projection.cpp   (mongod, tools, mongos)
- src/mongo/db/projection.h

# Interface

### src/mongo/db/projection.cpp

<div></div>

    mongo::Projection::init(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

<div></div>

    mongo::Projection::transform(mongo::BSONObj const&, mongo::MatchDetails const*) const

- Used By:

    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)

-------------

# Group Description
Entry point for various database operations   locks: we should clarify locking, e.g. everything in update.cpp happens   in the context of a db write lock   should clarify the relationship between these and db/instance.cpp (not built in anywhere)

# Files
- src/mongo/db/ops/count.cpp   (mongod, tools)
- src/mongo/db/ops/count.h
- src/mongo/db/ops/delete.cpp   (mongod, tools)
- src/mongo/db/ops/delete.h
- src/mongo/db/ops/insert.cpp   (mongod, tools)
- src/mongo/db/ops/insert.h
- src/mongo/db/ops/update.cpp   (mongod, tools)
- src/mongo/db/ops/update.h

# Interface

### src/mongo/db/ops/count.cpp

<div></div>

    mongo::runCount(char const*, mongo::BSONObj const&, std::string&, int&)

- Used By:

    - [src/mongo/dbtests/counttests.cpp](../unit\_tests)
    - [src/mongo/db/dbcommands.cpp](../database\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

### src/mongo/db/ops/delete.cpp

<div></div>

    mongo::deleteObjects(mongo::StringData const&, mongo::BSONObj, bool, bool, bool)

- Used By:

    - [src/mongo/db/ttl.cpp](../indexing)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/database.cpp](../storage\_layer\_structure)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/catalog/index\_catalog.cpp](../storage\_layer\_structure)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

### src/mongo/db/ops/insert.cpp

<div></div>

    mongo::fixDocumentForInsert(mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/dbtests/pdfiletests.cpp](../unit\_tests)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::userAllowedWriteNS(mongo::StringData const&)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::userAllowedWriteNS(mongo::NamespaceString const&)

- Used By:

    - [src/mongo/db/commands/write\_commands/write\_commands.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)

<div></div>

    mongo::userAllowedWriteNS(mongo::StringData const&, mongo::StringData const&)

- Used By:

    - [src/mongo/db/dbcommands.cpp](../database\_commands)

### src/mongo/db/ops/update.cpp

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*)

- Used By:

    - [src/mongo/db/repl/oplog.cpp](../replication)
    - [src/mongo/db/repl/rs\_rollback.cpp](../replication)
    - [src/mongo/db/commands/find\_and\_modify.cpp](../database\_commands)
    - [src/mongo/db/commands/write\_commands/batch\_executor.cpp](../new\_wire\_protocol\_write\_commands)
    - [src/mongo/db/repl/master\_slave.cpp](../replication)
    - [src/mongo/db/dbhelpers.cpp](../client\_and\_operation\_tracking)

<div></div>

    mongo::applyUpdateOperators(mongo::BSONObj const&, mongo::BSONObj const&)

- Used By:

    - [src/mongo/db/namespace\_details.cpp](../storage\_layer\_structure)

<div></div>

    mongo::update(mongo::UpdateRequest const&, mongo::OpDebug*, mongo::UpdateDriver*)

- Used By:

    - [src/mongo/db/instance.cpp](../storage\_layer\_structure)
