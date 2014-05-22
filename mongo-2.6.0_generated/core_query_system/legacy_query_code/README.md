# Legacy Query Code
Old query code that is gradually being phased out.


-------------

## Legacy Query Utilities
Legacy utilities for managing queries. Has utilities like range intersection and application of skip and limit. These are allllmost dead. The functionality should be replaced by the new matcher, expressions, and query system.

#### Files
- [src/mongo/db/queryutil-inl.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/queryutil-inl.h)   (mongod, tools, mongos)
- [src/mongo/db/queryutil.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/queryutil.cpp)   (mongod, tools, mongos)
- [src/mongo/db/queryutil.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/db/queryutil.h)   (mongod, tools, mongos)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
