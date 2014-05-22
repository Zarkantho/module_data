# Query Execution
This handles the actual execution of a query.  This is what interacts with the indexes and the storage layer to actually fetch the stream of results.


-------------

## Query Plan Executor
Class built on top of a Plan Stage tree that knows how to turn the crank on query execution.

#### Files
- [src/mongo/db/query/plan\_executor.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/plan_executor.cpp)   (mongod, tools)
- [src/mongo/db/query/plan\_executor.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/plan_executor.h)   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Query Plan Stage Interface
A plan stage is the basic building block of a query execution plan. The plan stage also keeps track of the state of the execution of the stage.

#### Files
- [src/mongo/db/exec/plan\_stage.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/plan_stage.h)   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Query Plan Stage Builder
Converts a query solution to an actual execution plan, using specific information about the current state of the database, such as what indexes are available.

#### Files
- [src/mongo/db/query/stage\_builder.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/stage_builder.cpp)   (mongod, tools)
- [src/mongo/db/query/stage\_builder.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/stage_builder.h)   (mongod, tools)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Query Plan Stage Types
Enum of all the supported plan stage types.

#### Files
- [src/mongo/db/query/stage\_types.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/stage_types.h)   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Query Plan Stage Implementations
Implementations for all the types of plan stages that can comprise a query.

#### Files
- [src/mongo/db/exec/2d.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/2d.cpp)   (mongod, tools)
- [src/mongo/db/exec/2d.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/2d.h)   (mongod, tools)
- [src/mongo/db/exec/2dcommon.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/2dcommon.cpp)   (mongod, tools)
- [src/mongo/db/exec/2dcommon.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/2dcommon.h)   (mongod, tools)
- [src/mongo/db/exec/2dnear.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/2dnear.cpp)   (mongod, tools)
- [src/mongo/db/exec/2dnear.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/2dnear.h)   (mongod, tools)
- [src/mongo/db/exec/and\_common-inl.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/and_common-inl.h)   (mongod, tools)
- [src/mongo/db/exec/and\_hash.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/and_hash.cpp)   (mongod, tools)
- [src/mongo/db/exec/and\_hash.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/and_hash.h)   (mongod, tools)
- [src/mongo/db/exec/and\_sorted.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/and_sorted.cpp)   (mongod, tools)
- [src/mongo/db/exec/and\_sorted.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/and_sorted.h)   (mongod, tools)
- [src/mongo/db/exec/collection\_scan.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/collection_scan.cpp)   (mongod, tools)
- [src/mongo/db/exec/collection\_scan.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/collection_scan.h)   (mongod, tools, mongos)
- [src/mongo/db/exec/collection\_scan\_common.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/collection_scan_common.h)   (mongod, tools, mongos)
- [src/mongo/db/exec/count.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/count.cpp)   (mongod, tools)
- [src/mongo/db/exec/count.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/count.h)   (mongod, tools)
- [src/mongo/db/exec/distinct\_scan.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/distinct_scan.cpp)   (mongod, tools)
- [src/mongo/db/exec/distinct\_scan.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/distinct_scan.h)   (mongod, tools)
- [src/mongo/db/exec/fetch.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/fetch.cpp)   (mongod, tools)
- [src/mongo/db/exec/fetch.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/fetch.h)   (mongod, tools, mongos)
- [src/mongo/db/exec/filter.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/filter.h)   (mongod, tools)
- [src/mongo/db/exec/index\_scan.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/index_scan.cpp)   (mongod, tools)
- [src/mongo/db/exec/index\_scan.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/index_scan.h)   (mongod, tools, mongos)
- [src/mongo/db/exec/keep\_mutations.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/keep_mutations.cpp)   (mongod, tools)
- [src/mongo/db/exec/keep\_mutations.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/keep_mutations.h)   (mongod, tools)
- [src/mongo/db/exec/limit.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/limit.cpp)   (mongod, tools)
- [src/mongo/db/exec/limit.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/limit.h)   (mongod, tools)
- [src/mongo/db/exec/merge\_sort.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/merge_sort.cpp)   (mongod, tools)
- [src/mongo/db/exec/merge\_sort.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/merge_sort.h)   (mongod, tools)
- [src/mongo/db/exec/mock\_stage.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/mock_stage.cpp)   ()
- [src/mongo/db/exec/mock\_stage.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/mock_stage.h)   ()
- [src/mongo/db/exec/oplogstart.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/oplogstart.cpp)   (mongod, tools)
- [src/mongo/db/exec/oplogstart.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/oplogstart.h)   (mongod, tools)
- [src/mongo/db/exec/or.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/or.cpp)   (mongod, tools)
- [src/mongo/db/exec/or.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/or.h)   (mongod, tools)
- [src/mongo/db/exec/projection.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/projection.cpp)   (mongod, tools)
- [src/mongo/db/exec/projection.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/projection.h)   (mongod, tools)
- [src/mongo/db/exec/projection\_exec.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/projection_exec.cpp)   (mongod, tools)
- [src/mongo/db/exec/projection\_exec.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/projection_exec.h)   (mongod, tools)
- [src/mongo/db/exec/projection\_exec\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/projection_exec_test.cpp)   ()
- [src/mongo/db/exec/s2near.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/s2near.cpp)   (mongod, tools)
- [src/mongo/db/exec/s2near.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/s2near.h)   (mongod, tools)
- [src/mongo/db/exec/shard\_filter.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/shard_filter.cpp)   (mongod, tools)
- [src/mongo/db/exec/shard\_filter.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/shard_filter.h)   (mongod, tools)
- [src/mongo/db/exec/skip.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/skip.cpp)   (mongod, tools)
- [src/mongo/db/exec/skip.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/skip.h)   (mongod, tools)
- [src/mongo/db/exec/sort.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/sort.cpp)   (mongod, tools)
- [src/mongo/db/exec/sort.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/sort.h)   (mongod, tools)
- [src/mongo/db/exec/sort\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/sort_test.cpp)   ()
- [src/mongo/db/exec/text.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/text.cpp)   (mongod, tools)
- [src/mongo/db/exec/text.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/text.h)   (mongod, tools)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Query Stage Test Command
TODO: Document what these are for and how they fit into the system.

#### Files
- [src/mongo/db/exec/stagedebug\_cmd.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/stagedebug_cmd.cpp)   (mongod, tools)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Query Plan Stats
TODO: Document what these are for and how they fit into the system.

#### Files
- [src/mongo/db/exec/plan\_stats.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/plan_stats.h)   (mongod, tools, mongos)

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Working Set
All data in use by a query operation.

#### Files
- [src/mongo/db/exec/working\_set.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/working_set.cpp)   (mongod, tools, mongos)
- [src/mongo/db/exec/working\_set.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/working_set.h)   (mongod, tools, mongos)
- [src/mongo/db/exec/working\_set\_common.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/working_set_common.cpp)   (mongod, tools)
- [src/mongo/db/exec/working\_set\_common.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/working_set_common.h)   (mongod, tools)
- [src/mongo/db/exec/working\_set\_computed\_data.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/working_set_computed_data.h)   (mongod, tools)
- [src/mongo/db/exec/working\_set\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/exec/working_set_test.cpp)   ()

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Query Runner Interface
Interface for an object that 

#### Files
- [src/mongo/db/query/runner.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/runner.h)   (mongod, tools, mongos)

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Cache Aware Query Runners
Query runners that exist because of our strategy of running multiple plans and caching the best one.  They both are aware of the cache and provide feeback to it based on the results of the query execution.

#### Files
- [src/mongo/db/query/cached\_plan\_runner.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/cached_plan_runner.cpp)   (mongod, tools)
- [src/mongo/db/query/cached\_plan\_runner.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/cached_plan_runner.h)   (mongod, tools)
- [src/mongo/db/query/multi\_plan\_runner.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/multi_plan_runner.cpp)   (mongod, tools)
- [src/mongo/db/query/multi\_plan\_runner.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/multi_plan_runner.h)   (mongod, tools)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)

-------------

## Query Runners
TODO: Document what these are for and how they fit into the query system.

#### Files
- [src/mongo/db/query/eof\_runner.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/eof_runner.cpp)   (mongod, tools)
- [src/mongo/db/query/eof\_runner.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/eof_runner.h)   (mongod, tools, mongos)
- [src/mongo/db/query/idhack\_runner.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/idhack_runner.cpp)   (mongod, tools)
- [src/mongo/db/query/idhack\_runner.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/idhack_runner.h)   (mongod, tools)
- [src/mongo/db/query/internal\_runner.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/internal_runner.cpp)   (mongod, tools)
- [src/mongo/db/query/internal\_runner.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/internal_runner.h)   (mongod, tools, mongos)
- [src/mongo/db/query/runner\_yield\_policy.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/runner_yield_policy.h)   (mongod, tools)
- [src/mongo/db/query/single\_solution\_runner.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/single_solution_runner.cpp)   (mongod, tools)
- [src/mongo/db/query/single\_solution\_runner.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/single_solution_runner.h)   (mongod, tools)
- [src/mongo/db/query/subplan\_runner.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/subplan_runner.cpp)   (mongod, tools)
- [src/mongo/db/query/subplan\_runner.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/subplan_runner.h)   (mongod, tools)

#### [Interface](interface/10)

#### [Dependencies](dependencies/10)
