# Mongod Sharding Metadata
Classes to manage and store sharding related metadata on mongod


-------------

## Global Sharding State
Global class that is the point of contact for all sharding related state in a mongod.  This gets called when sharding is enabled, as well as when sharding metadata is needed.  This class does not directly contain metadata for specific sharded collections, but provides accessors to get to the classes that do contain that data. The definition of this class is in d\_logic.h.

#### Files
- [src/mongo/s/d\_state.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/d_state.cpp)   (mongod, tools)

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)

-------------

## Collection Metadata
Container to hold the sharded metadata of a collection on mongod.

#### Files
- [src/mongo/s/collection\_metadata.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/collection_metadata.cpp)   (mongod, tools)
- [src/mongo/s/collection\_metadata.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/collection_metadata.h)   (mongod, tools, mongos)
- [src/mongo/s/collection\_metadata\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/collection_metadata_test.cpp)   ()

#### [Interface](interface/1)

#### [Dependencies](dependencies/1)

-------------

## Collection Metadata Loader
Helper to load the current metadata for a collection from the config servers.  Does not contain any of the collection state itself.

#### Files
- [src/mongo/s/metadata\_loader.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/metadata_loader.cpp)   (mongod, tools)
- [src/mongo/s/metadata\_loader.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/metadata_loader.h)   (mongod, tools)
- [src/mongo/s/metadata\_loader\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/metadata_loader_test.cpp)   ()

#### [Interface](interface/2)

#### [Dependencies](dependencies/2)

-------------

## Mongod Sharding Globals
Declarations for a bunch of globals used in sharding.  The actual definitions are unfortunately scatterned between d\_logic.cpp, d\_state.cpp, and others.

#### Files
- [src/mongo/s/d\_logic.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/d_logic.h)   (mongod, tools, mongos)

#### [Interface](interface/3)

#### [Dependencies](dependencies/3)
