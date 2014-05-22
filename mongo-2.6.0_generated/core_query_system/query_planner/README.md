# Query Planner
This is the place where we try to make decisions that optimize query execution.  We do both static and dynamic optimization.

The static optimization involves using information we have independendently of the actual execution, such as whether a query can use an index, or whether a query can be satisfied entirely by the index keys.

The dynamic optimization involves using information about the actual execution of the query to determine what solution to use, which is done by executing multiple possible solutions and caching the best one.


-------------

## Query Solution
Abstract representation of a possible query execution plan.

#### Files
- [src/mongo/db/query/query\_solution.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_solution.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/query\_solution.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_solution.h)   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## LRU Key Value Cache
Key value store utility class with limited size and an LRU replacement policy.

#### Files
- [src/mongo/db/query/lru\_key\_value.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/lru_key_value.h)   (mongod, tools, mongos)
- [src/mongo/db/query/lru\_key\_value\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/lru_key_value_test.cpp)   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Query Plan Cache
Maps a parsed and canonicalized query to the best solution that we know of.  Note that this is not the execution tree, but the solution tree, which is the abstract representation of how we should execute the query.

#### Files
- [src/mongo/db/query/plan\_cache.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/plan_cache.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/plan\_cache.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/plan_cache.h)   (mongod, tools, mongos)
- [src/mongo/db/query/plan\_cache\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/plan_cache_test.cpp)   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Get Query Runner
Interface to get a query runner.  This contains the code that checks if the plan is cached, looks at the plan parameters that are passed in, and executes the query planner.  In essence, this code is the glue that is responsible for multiplexing between the different types of runners.

#### Files
- [src/mongo/db/query/get\_runner.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/get_runner.cpp)   (mongod, tools)
- [src/mongo/db/query/get\_runner.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/get_runner.h)   (mongod, tools)
- [src/mongo/db/query/get\_runner\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/get_runner_test.cpp)   ()

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Query Explain Plan
Code to handle constructing user facing explain output from internal query execution information.

#### Files
- [src/mongo/db/query/explain\_plan.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/explain_plan.cpp)   (mongod, tools)
- [src/mongo/db/query/explain\_plan.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/explain_plan.h)   (mongod, tools)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Explain Document Schema
Schema of the document returned by the explain command, which is how the user gets information about query execution.

#### Files
- [src/mongo/db/query/type\_explain.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/type_explain.cpp)   (mongod, tools)
- [src/mongo/db/query/type\_explain.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/type_explain.h)   (mongod, tools)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Query Planner
TODO: Document what these are for and how they fit into the query system.

#### Files
- [src/mongo/db/query/planner\_access.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/planner_access.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/planner\_access.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/planner_access.h)   (mongod, tools, mongos)
- [src/mongo/db/query/planner\_analysis.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/planner_analysis.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/planner\_analysis.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/planner_analysis.h)   (mongod, tools, mongos)
- [src/mongo/db/query/planner\_ixselect.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/planner_ixselect.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/planner\_ixselect.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/planner_ixselect.h)   (mongod, tools, mongos)
- [src/mongo/db/query/planner\_ixselect\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/planner_ixselect_test.cpp)   ()
- [src/mongo/db/query/query\_planner.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_planner.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/query\_planner.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_planner.h)   (mongod, tools, mongos)
- [src/mongo/db/query/query\_planner\_common.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_planner_common.h)   (mongod, tools, mongos)
- [src/mongo/db/query/query\_planner\_params.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_planner_params.h)   (mongod, tools, mongos)
- [src/mongo/db/query/query\_planner\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_planner_test.cpp)   ()
- [src/mongo/db/query/query\_planner\_test\_lib.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_planner_test_lib.cpp)   (mongod, tools)
- [src/mongo/db/query/query\_planner\_test\_lib.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_planner_test_lib.h)   (mongod, tools)
- [src/mongo/db/query/query\_planner\_text\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_planner_text_test.cpp)   ()

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Query Plan
TODO: Document what these are for and how they fit into the query system.

#### Files
- [src/mongo/db/query/internal\_plans.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/internal_plans.h)   (mongod, tools, mongos)
- [src/mongo/db/query/plan\_enumerator.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/plan_enumerator.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/plan\_enumerator.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/plan_enumerator.h)   (mongod, tools, mongos)
- [src/mongo/db/query/plan\_ranker.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/plan_ranker.cpp)   (mongod, tools)
- [src/mongo/db/query/plan\_ranker.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/plan_ranker.h)   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Interval
TODO: Document what these are for and how they fit into the query system.

#### Files
- [src/mongo/db/query/interval.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/interval.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/interval.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/interval.h)   (mongod, tools, mongos)
- [src/mongo/db/query/interval\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/interval_test.cpp)   ()

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Query Index Management
TODO: Document what these are for and how they fit into the query system.

#### Files
- [src/mongo/db/query/index\_bounds.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/index_bounds.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/index\_bounds.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/index_bounds.h)   (mongod, tools, mongos)
- [src/mongo/db/query/index\_bounds\_builder.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/index_bounds_builder.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/index\_bounds\_builder.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/index_bounds_builder.h)   (mongod, tools, mongos)
- [src/mongo/db/query/index\_bounds\_builder\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/index_bounds_builder_test.cpp)   ()
- [src/mongo/db/query/index\_bounds\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/index_bounds_test.cpp)   ()
- [src/mongo/db/query/index\_entry.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/index_entry.h)   (mongod, tools, mongos)
- [src/mongo/db/query/index\_tag.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/index_tag.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/index\_tag.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/index_tag.h)   (mongod, tools, mongos)
- [src/mongo/db/query/indexability.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/indexability.h)   (mongod, tools, mongos)

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)
