# Query Execution
This handles the actual execution of a query.  This is what interacts with the indexes and the storage layer to actually fetch the stream of results.


-------------

## Query Plan Executor
Class built on top of a Plan Stage tree that knows how to turn the crank on query execution.

#### Files
- src/mongo/db/query/plan\_executor.cpp   (mongod, tools)
- src/mongo/db/query/plan\_executor.h   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Query Plan Stage Interface
A plan stage is the basic building block of a query execution plan. The plan stage also keeps track of the state of the execution of the stage.

#### Files
- src/mongo/db/exec/plan\_stage.h   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Query Plan Stage Builder
Converts a query solution to an actual execution plan, using specific information about the current state of the database, such as what indexes are available.

#### Files
- src/mongo/db/query/stage\_builder.cpp   (mongod, tools)
- src/mongo/db/query/stage\_builder.h   (mongod, tools)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Query Plan Stage Types
Enum of all the supported plan stage types.

#### Files
- src/mongo/db/query/stage\_types.h   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Query Plan Stage Implementations
Implementations for all the types of plan stages that can comprise a query.

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
- src/mongo/db/exec/collection\_scan.h   (mongod, tools, mongos)
- src/mongo/db/exec/collection\_scan\_common.h   (mongod, tools, mongos)
- src/mongo/db/exec/count.cpp   (mongod, tools)
- src/mongo/db/exec/count.h   (mongod, tools)
- src/mongo/db/exec/distinct\_scan.cpp   (mongod, tools)
- src/mongo/db/exec/distinct\_scan.h   (mongod, tools)
- src/mongo/db/exec/fetch.cpp   (mongod, tools)
- src/mongo/db/exec/fetch.h   (mongod, tools, mongos)
- src/mongo/db/exec/filter.h   (mongod, tools)
- src/mongo/db/exec/index\_scan.cpp   (mongod, tools)
- src/mongo/db/exec/index\_scan.h   (mongod, tools, mongos)
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
- src/mongo/db/exec/text.cpp   (mongod, tools)
- src/mongo/db/exec/text.h   (mongod, tools)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Query Stage Test Command
TODO: Document what these are for and how they fit into the system.

#### Files
- src/mongo/db/exec/stagedebug\_cmd.cpp   (mongod, tools)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Query Plan Stats
TODO: Document what these are for and how they fit into the system.

#### Files
- src/mongo/db/exec/plan\_stats.h   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Working Set
All data in use by a query operation.

#### Files
- src/mongo/db/exec/working\_set.cpp   (mongod, tools, mongos)
- src/mongo/db/exec/working\_set.h   (mongod, tools, mongos)
- src/mongo/db/exec/working\_set\_common.cpp   (mongod, tools)
- src/mongo/db/exec/working\_set\_common.h   (mongod, tools)
- src/mongo/db/exec/working\_set\_computed\_data.h   (mongod, tools)
- src/mongo/db/exec/working\_set\_test.cpp   ()

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Query Runner Interface
Interface for an object that 

#### Files
- src/mongo/db/query/runner.h   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Cache Aware Query Runners
Query runners that exist because of our strategy of running multiple plans and caching the best one.  They both are aware of the cache and provide feeback to it based on the results of the query execution.

#### Files
- src/mongo/db/query/cached\_plan\_runner.cpp   (mongod, tools)
- src/mongo/db/query/cached\_plan\_runner.h   (mongod, tools)
- src/mongo/db/query/multi\_plan\_runner.cpp   (mongod, tools)
- src/mongo/db/query/multi\_plan\_runner.h   (mongod, tools)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Query Runners
TODO: Document what these are for and how they fit into the query system.

#### Files
- src/mongo/db/query/eof\_runner.cpp   (mongod, tools)
- src/mongo/db/query/eof\_runner.h   (mongod, tools, mongos)
- src/mongo/db/query/idhack\_runner.cpp   (mongod, tools)
- src/mongo/db/query/idhack\_runner.h   (mongod, tools)
- src/mongo/db/query/internal\_runner.cpp   (mongod, tools)
- src/mongo/db/query/internal\_runner.h   (mongod, tools, mongos)
- src/mongo/db/query/runner\_yield\_policy.h   (mongod, tools)
- src/mongo/db/query/single\_solution\_runner.cpp   (mongod, tools)
- src/mongo/db/query/single\_solution\_runner.h   (mongod, tools)
- src/mongo/db/query/subplan\_runner.cpp   (mongod, tools)
- src/mongo/db/query/subplan\_runner.h   (mongod, tools)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)
