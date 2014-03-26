# Core Query System


-------------

## Query Expression Parser
Matcher expressions. The point of all of this is to take a query string and turn it into a structured set of classes.

#### Files
- src/mongo/db/matcher/expression.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression.h   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_array.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_array.h   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_array\_test.cpp   ()
- src/mongo/db/matcher/expression\_geo.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_geo.h   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_geo\_test.cpp   ()
- src/mongo/db/matcher/expression\_leaf.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_leaf.h   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_leaf\_test.cpp   ()
- src/mongo/db/matcher/expression\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_parser.h   (mongod, tools, mongos)
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
- src/mongo/db/matcher/expression\_text.h   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_tree.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_tree.h   (mongod, tools, mongos)
- src/mongo/db/matcher/expression\_tree\_test.cpp   ()
- src/mongo/db/matcher/expression\_where.cpp   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Matchable Document
Class that holds a BSONObj and provides an interface that the parsed expressions use when determining whether a BSONObj matches.

#### Files
- src/mongo/db/matcher/matchable.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/matchable.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Document Iterators
This contains code to help with iterating arrays and nested documents

#### Files
- src/mongo/db/matcher/path.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/path.h   (mongod, tools, mongos)
- src/mongo/db/matcher/path\_internal.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/path\_internal.h   (mongod, tools, mongos)
- src/mongo/db/matcher/path\_test.cpp   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Document Matcher
Interface to actually test if a document matches.  Wraps a match expression generated from the expression parsing system.

#### Files
- src/mongo/db/matcher/matcher.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/matcher.h   (mongod, tools, mongos)
- src/mongo/db/matcher.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Match Details
Helper for requesting more details about what matched our query from the matcher system.

#### Files
- src/mongo/db/matcher/match\_details.cpp   (mongod, tools, mongos)
- src/mongo/db/matcher/match\_details.h   (mongod, tools, mongos)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## TODO: Name this group
Planning/parsing/optimization for new query framework   not execution as well? (what are all these *runner.cpp files?)

#### Files
- src/mongo/db/query/cached\_plan\_runner.cpp   (mongod, tools)
- src/mongo/db/query/cached\_plan\_runner.h   (mongod, tools)
- src/mongo/db/query/canonical\_query.cpp   (mongod, tools, mongos)
- src/mongo/db/query/canonical\_query.h   (mongod, tools, mongos)
- src/mongo/db/query/canonical\_query\_test.cpp   ()
- src/mongo/db/query/eof\_runner.cpp   (mongod, tools)
- src/mongo/db/query/eof\_runner.h   (mongod, tools)
- src/mongo/db/query/explain\_plan.cpp   (mongod, tools)
- src/mongo/db/query/explain\_plan.h   (mongod, tools)
- src/mongo/db/query/find\_constants.h   (mongod, tools)
- src/mongo/db/query/get\_runner.cpp   (mongod, tools)
- src/mongo/db/query/get\_runner.h   (mongod, tools)
- src/mongo/db/query/get\_runner\_test.cpp   ()
- src/mongo/db/query/idhack\_runner.cpp   (mongod, tools)
- src/mongo/db/query/idhack\_runner.h   (mongod, tools)
- src/mongo/db/query/index\_bounds.cpp   (mongod, tools, mongos)
- src/mongo/db/query/index\_bounds.h   (mongod, tools, mongos)
- src/mongo/db/query/index\_bounds\_builder.cpp   (mongod, tools, mongos)
- src/mongo/db/query/index\_bounds\_builder.h   (mongod, tools, mongos)
- src/mongo/db/query/index\_bounds\_builder\_test.cpp   ()
- src/mongo/db/query/index\_bounds\_test.cpp   ()
- src/mongo/db/query/index\_entry.h   (mongod, tools, mongos)
- src/mongo/db/query/index\_tag.cpp   (mongod, tools, mongos)
- src/mongo/db/query/index\_tag.h   (mongod, tools, mongos)
- src/mongo/db/query/indexability.h   (mongod, tools, mongos)
- src/mongo/db/query/internal\_plans.h   (mongod, tools)
- src/mongo/db/query/internal\_runner.cpp   (mongod, tools)
- src/mongo/db/query/internal\_runner.h   (mongod, tools)
- src/mongo/db/query/interval.cpp   (mongod, tools, mongos)
- src/mongo/db/query/interval.h   (mongod, tools, mongos)
- src/mongo/db/query/interval\_test.cpp   ()
- src/mongo/db/query/lite\_parsed\_query.cpp   (mongod, tools, mongos)
- src/mongo/db/query/lite\_parsed\_query.h   (mongod, tools, mongos)
- src/mongo/db/query/lite\_parsed\_query\_test.cpp   ()
- src/mongo/db/query/multi\_plan\_runner.cpp   (mongod, tools)
- src/mongo/db/query/multi\_plan\_runner.h   (mongod, tools)
- src/mongo/db/query/new\_find.cpp   (mongod, tools)
- src/mongo/db/query/new\_find.h   (mongod, tools)
- src/mongo/db/query/parsed\_projection.cpp   (mongod, tools, mongos)
- src/mongo/db/query/parsed\_projection.h   (mongod, tools, mongos)
- src/mongo/db/query/parsed\_projection\_test.cpp   ()
- src/mongo/db/query/plan\_cache.cpp   (mongod, tools, mongos)
- src/mongo/db/query/plan\_cache.h   (mongod, tools, mongos)
- src/mongo/db/query/plan\_cache\_test.cpp   ()
- src/mongo/db/query/plan\_enumerator.cpp   (mongod, tools, mongos)
- src/mongo/db/query/plan\_enumerator.h   (mongod, tools, mongos)
- src/mongo/db/query/plan\_executor.cpp   (mongod, tools)
- src/mongo/db/query/plan\_executor.h   (mongod, tools)
- src/mongo/db/query/plan\_ranker.cpp   (mongod, tools)
- src/mongo/db/query/plan\_ranker.h   (mongod, tools, mongos)
- src/mongo/db/query/planner\_access.cpp   (mongod, tools, mongos)
- src/mongo/db/query/planner\_access.h   (mongod, tools, mongos)
- src/mongo/db/query/planner\_analysis.cpp   (mongod, tools, mongos)
- src/mongo/db/query/planner\_analysis.h   (mongod, tools, mongos)
- src/mongo/db/query/planner\_ixselect.cpp   (mongod, tools, mongos)
- src/mongo/db/query/planner\_ixselect.h   (mongod, tools, mongos)
- src/mongo/db/query/planner\_ixselect\_test.cpp   ()
- src/mongo/db/query/qlog.cpp   (mongod, tools, mongos)
- src/mongo/db/query/qlog.h   (mongod, tools, mongos)
- src/mongo/db/query/query\_planner.cpp   (mongod, tools, mongos)
- src/mongo/db/query/query\_planner.h   (mongod, tools, mongos)
- src/mongo/db/query/query\_planner\_common.h   (mongod, tools, mongos)
- src/mongo/db/query/query\_planner\_params.h   (mongod, tools, mongos)
- src/mongo/db/query/query\_planner\_test.cpp   ()
- src/mongo/db/query/query\_planner\_test\_lib.cpp   ()
- src/mongo/db/query/query\_planner\_test\_lib.h   ()
- src/mongo/db/query/query\_settings.cpp   (mongod, tools, mongos)
- src/mongo/db/query/query\_settings.h   (mongod, tools, mongos)
- src/mongo/db/query/query\_solution.cpp   (mongod, tools, mongos)
- src/mongo/db/query/query\_solution.h   (mongod, tools, mongos)
- src/mongo/db/query/runner.h   (mongod, tools, mongos)
- src/mongo/db/query/runner\_yield\_policy.h   (mongod, tools)
- src/mongo/db/query/single\_solution\_runner.cpp   (mongod, tools)
- src/mongo/db/query/single\_solution\_runner.h   (mongod, tools)
- src/mongo/db/query/stage\_builder.cpp   (mongod, tools)
- src/mongo/db/query/stage\_builder.h   (mongod, tools)
- src/mongo/db/query/stage\_types.h   (mongod, tools, mongos)
- src/mongo/db/query/type\_explain.cpp   (mongod, tools)
- src/mongo/db/query/type\_explain.h   (mongod, tools)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## LRU Key Value Cache
Key value store utility class with limited size and an LRU replacement policy.

#### Files
- src/mongo/db/query/lru\_key\_value.h   (mongod, tools, mongos)
- src/mongo/db/query/lru\_key\_value\_test.cpp   ()

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## TODO: Name this group
Executor for new query framework   oh. what is the relationship between 'runners' and e.g. 'index\_scan'   here?

#### Files
- src/mongo/db/exec/2d.cpp   (mongod, tools)
- src/mongo/db/exec/2d.h   (mongod, tools)
- src/mongo/db/exec/2dcommon.cpp   (mongod, tools)
- src/mongo/db/exec/2dcommon.h   (mongod, tools)
- src/mongo/db/exec/2dnear.cpp   (mongod, tools)
- src/mongo/db/exec/2dnear.h   (mongod, tools)
- src/mongo/db/exec/and\_common-inl.h   (mongod, tools)
- src/mongo/db/exec/and\_hash.cpp   (mongod, tools)
- src/mongo/db/exec/and\_hash.h   (mongod, tools)
- src/mongo/db/exec/and\_sorted.cpp   (mongod, tools)
- src/mongo/db/exec/and\_sorted.h   (mongod, tools)
- src/mongo/db/exec/collection\_scan.cpp   (mongod, tools)
- src/mongo/db/exec/collection\_scan.h   (mongod, tools)
- src/mongo/db/exec/collection\_scan\_common.h   (mongod, tools, mongos)
- src/mongo/db/exec/count.cpp   (mongod, tools)
- src/mongo/db/exec/count.h   (mongod, tools)
- src/mongo/db/exec/distinct\_scan.cpp   (mongod, tools)
- src/mongo/db/exec/distinct\_scan.h   (mongod, tools)
- src/mongo/db/exec/fetch.cpp   (mongod, tools)
- src/mongo/db/exec/fetch.h   (mongod, tools)
- src/mongo/db/exec/filter.h   (mongod, tools)
- src/mongo/db/exec/index\_scan.cpp   (mongod, tools)
- src/mongo/db/exec/index\_scan.h   (mongod, tools)
- src/mongo/db/exec/keep\_mutations.cpp   (mongod, tools)
- src/mongo/db/exec/keep\_mutations.h   (mongod, tools)
- src/mongo/db/exec/limit.cpp   (mongod, tools)
- src/mongo/db/exec/limit.h   (mongod, tools)
- src/mongo/db/exec/merge\_sort.cpp   (mongod, tools)
- src/mongo/db/exec/merge\_sort.h   (mongod, tools)
- src/mongo/db/exec/mock\_stage.cpp   ()
- src/mongo/db/exec/mock\_stage.h   ()
- src/mongo/db/exec/oplogstart.cpp   (mongod, tools)
- src/mongo/db/exec/oplogstart.h   (mongod, tools)
- src/mongo/db/exec/or.cpp   (mongod, tools)
- src/mongo/db/exec/or.h   (mongod, tools)
- src/mongo/db/exec/plan\_stage.h   (mongod, tools, mongos)
- src/mongo/db/exec/plan\_stats.h   (mongod, tools, mongos)
- src/mongo/db/exec/projection.cpp   (mongod, tools)
- src/mongo/db/exec/projection.h   (mongod, tools)
- src/mongo/db/exec/projection\_exec.cpp   (mongod, tools)
- src/mongo/db/exec/projection\_exec.h   (mongod, tools)
- src/mongo/db/exec/projection\_exec\_test.cpp   ()
- src/mongo/db/exec/s2near.cpp   (mongod, tools)
- src/mongo/db/exec/s2near.h   (mongod, tools)
- src/mongo/db/exec/shard\_filter.cpp   (mongod, tools)
- src/mongo/db/exec/shard\_filter.h   (mongod, tools)
- src/mongo/db/exec/skip.cpp   (mongod, tools)
- src/mongo/db/exec/skip.h   (mongod, tools)
- src/mongo/db/exec/sort.cpp   (mongod, tools)
- src/mongo/db/exec/sort.h   (mongod, tools)
- src/mongo/db/exec/sort\_test.cpp   ()
- src/mongo/db/exec/stagedebug\_cmd.cpp   (mongod, tools)
- src/mongo/db/exec/text.cpp   (mongod, tools)
- src/mongo/db/exec/text.h   (mongod, tools)
- src/mongo/db/exec/working\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/exec/working\_set.h   (mongod, tools, mongos)
- src/mongo/db/exec/working\_set\_common.cpp   (mongod, tools)
- src/mongo/db/exec/working\_set\_common.h   (mongod, tools)
- src/mongo/db/exec/working\_set\_computed\_data.h   (mongod, tools)
- src/mongo/db/exec/working\_set\_test.cpp   ()
- src/mongo/dbtests/query\_stage\_distinct.cpp   ()
- src/mongo/dbtests/query\_stage\_keep.cpp   ()

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## TODO: Name this group
Legacy utilities for managing queries. Has utilities like range intersection and application of  skip and limit. These are allllmost dead. The functionality should be replaced by the new  matcher, expressions, and query system.

#### Files
- src/mongo/db/queryutil-inl.h   (mongod, tools, mongos)
- src/mongo/db/queryutil.cpp   (mongod, tools, mongos)
- src/mongo/db/queryutil.h   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## TODO: Name this group
Old way of doing document projections. Given a doc and a projection, transforms the document.   what calls it, and where are projections done now?

#### Files
- src/mongo/db/projection.cpp   (mongod, tools, mongos)
- src/mongo/db/projection.h   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## TODO: Name this group
Entry point for various database operations   locks: we should clarify locking, e.g. everything in update.cpp happens   in the context of a db write lock   should clarify the relationship between these and db/instance.cpp (not built in anywhere)

#### Files
- src/mongo/db/ops/count.cpp   (mongod, tools)
- src/mongo/db/ops/count.h   (mongod, tools)
- src/mongo/db/ops/delete.cpp   (mongod, tools)
- src/mongo/db/ops/delete.h   (mongod, tools)
- src/mongo/db/ops/insert.cpp   (mongod, tools)
- src/mongo/db/ops/insert.h   (mongod, tools)
- src/mongo/db/ops/update.cpp   (mongod, tools)
- src/mongo/db/ops/update.h   (mongod, tools)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)
