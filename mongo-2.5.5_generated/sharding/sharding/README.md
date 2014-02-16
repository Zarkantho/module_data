# sharding

# Module Groups

-------------

# Group Description
Helper classes to delete a range of documents. This is used for example in chunk migrations  when we are cleaning up an old chunk.

## Files
- src/mongo/db/range\_deleter.cpp   (mongod, tools)
- src/mongo/db/range\_deleter.h   (mongod, tools)
- src/mongo/db/range\_deleter\_db\_env.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_db\_env.h   (mongod, tools)
- src/mongo/db/range\_deleter\_mock\_env.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_mock\_env.h   (mongod, tools)
- src/mongo/db/range\_deleter\_service.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_service.h   (mongod, tools)
- src/mongo/db/range\_deleter\_stat\_test.cpp   ()
- src/mongo/db/range\_deleter\_stats.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_stats.h   (mongod, tools)
- src/mongo/db/range\_deleter\_test.cpp   ()
- src/mongo/db/range\_preserver.h   (mongod, tools)

## [Interface](interface/0)

## [Dependencies](dependencies/0)

-------------

# Group Description
Utilities for comparing ranges. Useful because our sharding is range based.   okay, but why in s/ ? only used by sharding? seems weird that something   general like range arith is only in s/ but the more specific delete-range   isn't.

## Files
- src/mongo/s/range\_arithmetic.cpp   (mongod, tools, mongos)
- src/mongo/s/range\_arithmetic.h   (mongod, tools, mongos)
- src/mongo/s/range\_arithmetic\_test.cpp   ()

## [Interface](interface/1)

## [Dependencies](dependencies/1)

-------------

# Group Description
Contains metadata about a collection, particularly for sharding. The MetadataLoader populates new  CollectionMetadata objects from config server data.

## Files
- src/mongo/s/collection\_metadata.cpp   (mongod, tools)
- src/mongo/s/collection\_metadata.h   (mongod, tools, mongos)
- src/mongo/s/collection\_metadata\_test.cpp   ()
- src/mongo/s/metadata\_loader.cpp   (mongod, tools)
- src/mongo/s/metadata\_loader.h   (mongod, tools)
- src/mongo/s/metadata\_loader\_test.cpp   ()

## [Interface](interface/2)

## [Dependencies](dependencies/2)

-------------

# Group Description
Code to upgrade config server metadata

## Files
- src/mongo/s/config\_upgrade.cpp   (mongos)
- src/mongo/s/config\_upgrade.h   (mongos)
- src/mongo/s/config\_upgrade\_helpers.cpp   (mongos)
- src/mongo/s/config\_upgrade\_helpers.h   (mongos)
- src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp   (mongos)
- src/mongo/s/config\_upgrade\_v4\_to\_v5.cpp   (mongos)

## [Interface](interface/3)

## [Dependencies](dependencies/3)

-------------

# Group Description
Distributed lock (lock on the config servers from mongos, i.e. "balancer lock")

## Files
- src/mongo/s/distlock.cpp   (mongod, tools, mongos)
- src/mongo/s/distlock.h   (mongod, tools, mongos)
- src/mongo/s/distlock\_test.cpp   (mongod, tools)

## [Interface](interface/4)

## [Dependencies](dependencies/4)

-------------

# Group Description
Parser for fields in a BSON object. Meant to help enforce a schema on a BSON object.

## Files
- src/mongo/db/field\_parser-inl.h   (mongod, tools, mongos)
- src/mongo/db/field\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/field\_parser.h   (mongod, tools, mongos)
- src/mongo/db/field\_parser\_test.cpp   ()

## [Interface](interface/5)

## [Dependencies](dependencies/5)

-------------

# Group Description
"Schema" for config server metadata. These classes contain structural class definitions for what  we expect to find on the config server. They use the field parser above to convert BSON fields  into C++ members.

## Files
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

## [Interface](interface/6)

## [Dependencies](dependencies/6)

-------------

# Group Description
Bizarre legacy sharding code.   From writeback\_listener.h  "The writeback listener takes back write attempts that were made against a wrong shard.  (Wrong here in the sense that the target chunk moved before this mongos had a chance to  learn so.) It is responsible for reapplying these writes to the correct shard."   So basically, the mongos sends an operation to the mongod, and the writeback listener (running on  the mongos) says to the mongod every now and again, "yo, have I screwed up recently?". The mongod  is then like "yeah bro, you screwed up, you wrote all these things to the wrong place and the  writeback listener is like "thanks man" and tries to write them to the correct shard. Meanwhile  the user is like "I'm so glad my data was written". This should go away because of the new write  commands.   rofl

## Files
- src/mongo/s/writeback\_listener.cpp   (mongos)
- src/mongo/s/writeback\_listener.h   (mongod, tools, mongos)

## [Interface](interface/7)

## [Dependencies](dependencies/7)

-------------

# Group Description
mongod component of writeback listener

## Files
- src/mongo/s/d\_writeback.cpp   (mongod, tools)
- src/mongo/s/d\_writeback.h   (mongod, tools)

## [Interface](interface/8)

## [Dependencies](dependencies/8)

-------------

# Group Description
Sharding code? TODO: verify that this is all sharding related and document the architecture.

## Files
- src/mongo/s/balance.cpp   (mongos)
- src/mongo/s/balance.h   (mongos)
- src/mongo/s/balancer\_policy.cpp   (mongos)
- src/mongo/s/balancer\_policy.h   (mongos)
- src/mongo/s/balancer\_policy\_tests.cpp   ()
- src/mongo/s/bson\_serializable.h   (mongod, tools, mongos)
- src/mongo/s/chunk.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk.h   (mongod, tools, mongos)
- src/mongo/s/chunk\_diff-inl.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk\_diff.h   (mongod, tools, mongos)
- src/mongo/s/chunk\_diff\_test.cpp   ()
- src/mongo/s/chunk\_manager\_targeter.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk\_manager\_targeter.h   (mongod, tools, mongos)
- src/mongo/s/chunk\_version.h   (mongod, tools, mongos)
- src/mongo/s/chunk\_version\_test.cpp   ()
- src/mongo/s/cluster\_client\_internal.cpp   (mongos)
- src/mongo/s/cluster\_client\_internal.h   (mongos)
- src/mongo/s/cluster\_write.cpp   (mongod, tools, mongos)
- src/mongo/s/cluster\_write.h   (mongod, tools, mongos)
- src/mongo/s/commands/auth\_schema\_upgrade\_s.cpp   (mongos)
- src/mongo/s/commands/cluster\_index\_filter\_cmd.cpp   (mongos)
- src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp   (mongos)
- src/mongo/s/commands/cluster\_plan\_cache\_cmd.cpp   (mongos)
- src/mongo/s/commands\_admin.cpp   (mongos)
- src/mongo/s/commands\_public.cpp   (mongos)
- src/mongo/s/config.cpp   (mongod, tools, mongos)
- src/mongo/s/config.h   (mongod, tools, mongos)
- src/mongo/s/config\_server\_checker\_service.cpp   (mongod, tools, mongos)
- src/mongo/s/config\_server\_checker\_service.h   (mongod, tools, mongos)
- src/mongo/s/config\_server\_tests.cpp   ()
- src/mongo/s/cursors.cpp   (mongos)
- src/mongo/s/cursors.h   (mongod, tools, mongos)
- src/mongo/s/d\_logic.cpp   (mongod, tools)
- src/mongo/s/d\_logic.h   (mongod, tools, mongos)
- src/mongo/s/d\_merge.cpp   (mongod, tools)
- src/mongo/s/d\_merge.h   (mongod, tools)
- src/mongo/s/d\_migrate.cpp   (mongod, tools)
- src/mongo/s/d\_split.cpp   (mongod, tools)
- src/mongo/s/d\_state.cpp   (mongod, tools)
- src/mongo/s/dbclient\_multi\_command.cpp   (mongod, tools, mongos)
- src/mongo/s/dbclient\_multi\_command.h   (mongod, tools, mongos)
- src/mongo/s/dbclient\_shard\_resolver.cpp   (mongod, tools, mongos)
- src/mongo/s/dbclient\_shard\_resolver.h   (mongod, tools, mongos)
- src/mongo/s/default\_version.cpp   (mongod, tools)
- src/mongo/s/grid.cpp   (mongod, tools, mongos)
- src/mongo/s/grid.h   (mongod, tools, mongos)
- src/mongo/s/mock\_multi\_write\_command.h   ()
- src/mongo/s/mock\_ns\_targeter.h   ()
- src/mongo/s/mock\_shard\_resolver.h   ()
- src/mongo/s/mongo\_version\_range.cpp   (mongod, tools, mongos)
- src/mongo/s/mongo\_version\_range.h   (mongod, tools, mongos)
- src/mongo/s/mongo\_version\_range\_test.cpp   ()
- src/mongo/s/mongos\_persistence\_stubs.cpp   (mongos)
- src/mongo/s/multi\_command\_dispatch.h   (mongod, tools, mongos)
- src/mongo/s/ns\_targeter.h   (mongod, tools, mongos)
- src/mongo/s/request.cpp   (mongos)
- src/mongo/s/request.h   (mongod, tools, mongos)
- src/mongo/s/shard.cpp   (mongod, tools, mongos)
- src/mongo/s/shard.h   (mongod, tools, mongos)
- src/mongo/s/shard\_conn\_test.cpp   ()
- src/mongo/s/shard\_key\_pattern.cpp   (mongod, tools, mongos)
- src/mongo/s/shard\_key\_pattern.h   (mongod, tools, mongos)
- src/mongo/s/shard\_resolver.h   (mongod, tools, mongos)
- src/mongo/s/shard\_test.cpp   ()
- src/mongo/s/shardconnection.cpp   (mongod, tools, mongos)
- src/mongo/s/shardkey.cpp   (mongod, tools, mongos)
- src/mongo/s/shardkey.h   (mongod, tools, mongos)
- src/mongo/s/stale\_exception.h   (mongod, tools, mongos)
- src/mongo/s/strategy.cpp   (mongos)
- src/mongo/s/strategy.h   (mongod, tools, mongos)
- src/mongo/s/version\_manager.cpp   (mongos)
- src/mongo/s/version\_manager.h   (mongod, tools, mongos)
- src/mongo/s/version\_mongos.cpp   (mongos)
- src/mongo/s/version\_mongos.h   (mongos)

## [Interface](interface/9)

## [Dependencies](dependencies/9)
