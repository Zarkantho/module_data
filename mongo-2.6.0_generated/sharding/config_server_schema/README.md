# Config Server Schema
Schema for all sharding related collections on the config server.  All direct config server access should use these classes.


-------------

## Config Server Schema
"Schema" for config server metadata. These classes contain structural class definitions for what we expect to find on the config server. They use the field parser above to convert BSON fields into C++ members.

#### Files
- src/mongo/s/type\_changelog.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_changelog.h   (mongod, tools, mongos)
- src/mongo/s/type\_changelog\_test.cpp   ()
- src/mongo/s/type\_chunk.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_chunk.h   (mongod, tools, mongos)
- src/mongo/s/type\_chunk\_test.cpp   ()
- src/mongo/s/type\_collection.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_collection.h   (mongod, tools, mongos)
- src/mongo/s/type\_collection\_test.cpp   ()
- src/mongo/s/type\_config\_version.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_config\_version.h   (mongod, tools, mongos)
- src/mongo/s/type\_config\_version\_test.cpp   ()
- src/mongo/s/type\_database.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_database.h   (mongod, tools, mongos)
- src/mongo/s/type\_database\_test.cpp   ()
- src/mongo/s/type\_lockpings.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_lockpings.h   (mongod, tools, mongos)
- src/mongo/s/type\_lockpings\_test.cpp   ()
- src/mongo/s/type\_locks.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_locks.h   (mongod, tools, mongos)
- src/mongo/s/type\_locks\_test.cpp   ()
- src/mongo/s/type\_mongos.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_mongos.h   (mongod, tools, mongos)
- src/mongo/s/type\_mongos\_test.cpp   ()
- src/mongo/s/type\_settings.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_settings.h   (mongod, tools, mongos)
- src/mongo/s/type\_settings\_test.cpp   ()
- src/mongo/s/type\_shard.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_shard.h   (mongod, tools, mongos)
- src/mongo/s/type\_shard\_test.cpp   ()
- src/mongo/s/type\_tags.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_tags.h   (mongod, tools, mongos)
- src/mongo/s/type\_tags\_test.cpp   ()

#### [Interface](interface/0)

#### [Dependencies](dependencies/0)
