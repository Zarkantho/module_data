# Query System Parameters
User facing or hard coded tunables or configuration for the query system.


-------------

## Query Constants
Constants used in the query system.  Currently just has the maximum batch size.

#### Files
- [src/mongo/db/query/find\_constants.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/find_constants.h)   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Query Knobs
Server Parameters that can be used to tune the query system.

#### Files
- [src/mongo/db/query/query\_knobs.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_knobs.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/query\_knobs.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_knobs.h)   (mongod, tools, mongos)

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Query Settings
User settings that put additional constraints on query execution. See the index filter commands in index\_filter\_commands.cpp for an example.

#### Files
- [src/mongo/db/query/query\_settings.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_settings.cpp)   (mongod, tools, mongos)
- [src/mongo/db/query/query\_settings.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/query/query_settings.h)   (mongod, tools, mongos)

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)
