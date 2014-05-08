# Query Planner
This is the place where we try to make decisions that optimize query execution.  We do both static and dynamic optimization.
The static optimization involves using information we have independendently of the actual execution, such as whether a query can use an index, or whether a query can be satisfied entirely by the index keys.
The dynamic optimization involves using information about the actual execution of the query to determine what solution to use, which is done by executing multiple possible solutions and caching the best one.


-------------

## Query Solution
Abstract representation of a possible query execution plan.

#### Files
- src/mongo/db/query/query\_solution.cpp   (mongod, tools, mongos)
- src/mongo/db/query/query\_solution.h   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## LRU Key Value Cache
Key value store utility class with limited size and an LRU replacement policy.

#### Files
- src/mongo/db/query/lru\_key\_value.h   (mongod, tools, mongos)
- src/mongo/db/query/lru\_key\_value\_test.cpp   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Query Plan Cache
Maps a parsed and canonicalized query to the best solution that we know of.  Note that this is not the execution tree, but the solution tree, which is the abstract representation of how we should execute the query.

#### Files
- src/mongo/db/query/plan\_cache.cpp   (mongod, tools, mongos)
- src/mongo/db/query/plan\_cache.h   (mongod, tools, mongos)
- src/mongo/db/query/plan\_cache\_test.cpp   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Get Query Runner
Interface to get a query runner.  This contains the code that checks if the plan is cached, looks at the plan parameters that are passed in, and executes the query planner.  In essence, this code is the glue that is responsible for multiplexing between the different types of runners.

#### Files
- src/mongo/db/query/get\_runner.cpp   (mongod, tools)
- src/mongo/db/query/get\_runner.h   (mongod, tools)
- src/mongo/db/query/get\_runner\_test.cpp   ()

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)

-------------

## Query Explain Plan
Code to handle constructing user facing explain output from internal query execution information.

#### Files
- src/mongo/db/query/explain\_plan.cpp   (mongod, tools)
- src/mongo/db/query/explain\_plan.h   (mongod, tools)

#### [Interface](interface/4)

#### [Dependencies](dependencies/4)

-------------

## Explain Document Schema
Schema of the document returned by the explain command, which is how the user gets information about query execution.

#### Files
- src/mongo/db/query/type\_explain.cpp   (mongod, tools)
- src/mongo/db/query/type\_explain.h   (mongod, tools)

#### [Interface](interface/5)

#### [Dependencies](dependencies/5)

-------------

## Query Planner
TODO: Document what these are for and how they fit into the query system.

#### Files
- src/mongo/db/query/planner\_access.cpp   (mongod, tools, mongos)
- src/mongo/db/query/planner\_access.h   (mongod, tools, mongos)
- src/mongo/db/query/planner\_analysis.cpp   (mongod, tools, mongos)
- src/mongo/db/query/planner\_analysis.h   (mongod, tools, mongos)
- src/mongo/db/query/planner\_ixselect.cpp   (mongod, tools, mongos)
- src/mongo/db/query/planner\_ixselect.h   (mongod, tools, mongos)
- src/mongo/db/query/planner\_ixselect\_test.cpp   ()
- src/mongo/db/query/query\_planner.cpp   (mongod, tools, mongos)
- src/mongo/db/query/query\_planner.h   (mongod, tools, mongos)
- src/mongo/db/query/query\_planner\_common.h   (mongod, tools, mongos)
- src/mongo/db/query/query\_planner\_params.h   (mongod, tools, mongos)
- src/mongo/db/query/query\_planner\_test.cpp   ()
- src/mongo/db/query/query\_planner\_test\_lib.cpp   (mongod, tools)
- src/mongo/db/query/query\_planner\_test\_lib.h   (mongod, tools)
- src/mongo/db/query/query\_planner\_text\_test.cpp   ()

#### [Interface](interface/6)

#### [Dependencies](dependencies/6)

-------------

## Query Plan
TODO: Document what these are for and how they fit into the query system.

#### Files
- src/mongo/db/query/internal\_plans.h   (mongod, tools, mongos)
- src/mongo/db/query/plan\_enumerator.cpp   (mongod, tools, mongos)
- src/mongo/db/query/plan\_enumerator.h   (mongod, tools, mongos)
- src/mongo/db/query/plan\_ranker.cpp   (mongod, tools)
- src/mongo/db/query/plan\_ranker.h   (mongod, tools, mongos)

#### [Interface](interface/7)

#### [Dependencies](dependencies/7)

-------------

## Interval
TODO: Document what these are for and how they fit into the query system.

#### Files
- src/mongo/db/query/interval.cpp   (mongod, tools, mongos)
- src/mongo/db/query/interval.h   (mongod, tools, mongos)
- src/mongo/db/query/interval\_test.cpp   ()

#### [Interface](interface/8)

#### [Dependencies](dependencies/8)

-------------

## Query Index Management
TODO: Document what these are for and how they fit into the query system.

#### Files
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

#### [Interface](interface/9)

#### [Dependencies](dependencies/9)
