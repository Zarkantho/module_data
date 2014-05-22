# Config Server Schema
Schema for all sharding related collections on the config server.  All direct config server access should use these classes.


-------------

## Config Server Schema
"Schema" for config server metadata. These classes contain structural class definitions for what we expect to find on the config server. They use the field parser above to convert BSON fields into C++ members.

#### Files
- [src/mongo/s/type\_changelog.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_changelog.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_changelog.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_changelog.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_changelog\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_changelog_test.cpp)   ()
- [src/mongo/s/type\_chunk.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_chunk.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_chunk.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_chunk.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_chunk\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_chunk_test.cpp)   ()
- [src/mongo/s/type\_collection.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_collection.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_collection.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_collection.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_collection\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_collection_test.cpp)   ()
- [src/mongo/s/type\_config\_version.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_config_version.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_config\_version.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_config_version.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_config\_version\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_config_version_test.cpp)   ()
- [src/mongo/s/type\_database.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_database.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_database.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_database.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_database\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_database_test.cpp)   ()
- [src/mongo/s/type\_lockpings.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_lockpings.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_lockpings.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_lockpings.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_lockpings\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_lockpings_test.cpp)   ()
- [src/mongo/s/type\_locks.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_locks.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_locks.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_locks.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_locks\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_locks_test.cpp)   ()
- [src/mongo/s/type\_mongos.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_mongos.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_mongos.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_mongos.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_mongos\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_mongos_test.cpp)   ()
- [src/mongo/s/type\_settings.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_settings.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_settings.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_settings.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_settings\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_settings_test.cpp)   ()
- [src/mongo/s/type\_shard.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_shard.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_shard.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_shard.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_shard\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_shard_test.cpp)   ()
- [src/mongo/s/type\_tags.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_tags.cpp)   (mongod, tools, mongos)
- [src/mongo/s/type\_tags.h](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_tags.h)   (mongod, tools, mongos)
- [src/mongo/s/type\_tags\_test.cpp](https://github.com/mongodb/mongo/tree/r2.6.0/src/mongo/s/type_tags_test.cpp)   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
