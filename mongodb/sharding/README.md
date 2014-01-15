# sharding

# Module Groups

-------------

Helper classes to delete a range of documents. This is used for example in chunk migrations  when we are cleaning up an old chunk.

- src/mongo/db/range\_deleter.cpp   (mongod, tools)
- src/mongo/db/range\_deleter.h
- src/mongo/db/range\_deleter\_db\_env.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_db\_env.h
- src/mongo/db/range\_deleter\_mock\_env.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_mock\_env.h
- src/mongo/db/range\_deleter\_service.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_service.h
- src/mongo/db/range\_deleter\_stat\_test.cpp   ()
- src/mongo/db/range\_deleter\_stats.cpp   (mongod, tools)
- src/mongo/db/range\_deleter\_stats.h
- src/mongo/db/range\_deleter\_test.cpp   ()
- src/mongo/db/range\_preserver.h

-------------

Utilities for comparing ranges. Useful because our sharding is range based.   okay, but why in s/ ? only used by sharding? seems weird that something   general like range arith is only in s/ but the more specific delete-range   isn't.

- src/mongo/s/range\_arithmetic.cpp   (mongod, tools, mongos)
- src/mongo/s/range\_arithmetic.h
- src/mongo/s/range\_arithmetic\_test.cpp   ()

-------------

Contains metadata about a collection, particularly for sharding. The MetadataLoader populates new  CollectionMetadata objects from config server data.

- src/mongo/s/collection\_metadata.cpp   (mongod, tools)
- src/mongo/s/collection\_metadata.h
- src/mongo/s/collection\_metadata\_test.cpp   ()
- src/mongo/s/metadata\_loader.cpp   (mongod, tools)
- src/mongo/s/metadata\_loader.h
- src/mongo/s/metadata\_loader\_test.cpp   ()

-------------

Code to upgrade config server metadata

- src/mongo/s/config\_upgrade.cpp   (mongos)
- src/mongo/s/config\_upgrade.h
- src/mongo/s/config\_upgrade\_helpers.cpp   (mongos)
- src/mongo/s/config\_upgrade\_helpers.h
- src/mongo/s/config\_upgrade\_v0\_to\_v5.cpp   (mongos)
- src/mongo/s/config\_upgrade\_v4\_to\_v5.cpp   (mongos)

-------------

Distributed lock (lock on the config servers from mongos, i.e. "balancer lock")

- src/mongo/client/distlock.cpp   (mongod, tools, mongos)
- src/mongo/client/distlock.h
- src/mongo/client/distlock\_test.cpp   (mongod, tools)

-------------

Parser for fields in a BSON object. Meant to help enforce a schema on a BSON object.

- src/mongo/db/field\_parser-inl.h
- src/mongo/db/field\_parser.cpp   (mongod, tools, mongos)
- src/mongo/db/field\_parser.h
- src/mongo/db/field\_parser\_test.cpp   ()

-------------

"Schema" for config server metadata. These classes contain structural class definitions for what  we expect to find on the config server. They use the field parser above to convert BSON fields  into C++ members.

- src/mongo/s/type\_changelog.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_changelog.h
- src/mongo/s/type\_changelog\_test.cpp   ()
- src/mongo/s/type\_chunk.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_chunk.h
- src/mongo/s/type\_chunk\_test.cpp   ()
- src/mongo/s/type\_collection.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_collection.h
- src/mongo/s/type\_collection\_test.cpp   ()
- src/mongo/s/type\_config\_version.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_config\_version.h
- src/mongo/s/type\_config\_version\_test.cpp   ()
- src/mongo/s/type\_database.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_database.h
- src/mongo/s/type\_database\_test.cpp   ()
- src/mongo/s/type\_lockpings.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_lockpings.h
- src/mongo/s/type\_lockpings\_test.cpp   ()
- src/mongo/s/type\_locks.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_locks.h
- src/mongo/s/type\_locks\_test.cpp   ()
- src/mongo/s/type\_mongos.cpp   (mongos)
- src/mongo/s/type\_mongos.h
- src/mongo/s/type\_mongos\_test.cpp   ()
- src/mongo/s/type\_settings.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_settings.h
- src/mongo/s/type\_settings\_test.cpp   ()
- src/mongo/s/type\_shard.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_shard.h
- src/mongo/s/type\_shard\_test.cpp   ()
- src/mongo/s/type\_tags.cpp   (mongod, tools, mongos)
- src/mongo/s/type\_tags.h
- src/mongo/s/type\_tags\_test.cpp   ()

-------------

Bizarre legacy sharding code.   From writeback\_listener.h  "The writeback listener takes back write attempts that were made against a wrong shard.  (Wrong here in the sense that the target chunk moved before this mongos had a chance to  learn so.) It is responsible for reapplying these writes to the correct shard."   So basically, the mongos sends an operation to the mongod, and the writeback listener (running on  the mongos) says to the mongod every now and again, "yo, have I screwed up recently?". The mongod  is then like "yeah bro, you screwed up, you wrote all these things to the wrong place and the  writeback listener is like "thanks man" and tries to write them to the correct shard. Meanwhile  the user is like "I'm so glad my data was written". This should go away because of the new write  commands.   rofl

- src/mongo/s/writeback\_listener.cpp   (mongos)
- src/mongo/s/writeback\_listener.h

-------------

mongod component of writeback listener

- src/mongo/s/d\_writeback.cpp   (mongod, tools)
- src/mongo/s/d\_writeback.h

-------------

Sharding code? TODO: verify that this is all sharding related and document the architecture.

- src/mongo/s/balance.cpp   (mongos)
- src/mongo/s/balance.h
- src/mongo/s/balancer\_policy.cpp   (mongos)
- src/mongo/s/balancer\_policy.h
- src/mongo/s/balancer\_policy\_tests.cpp   ()
- src/mongo/s/bson\_serializable.h
- src/mongo/s/chunk.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk.h
- src/mongo/s/chunk\_diff-inl.cpp
- src/mongo/s/chunk\_diff.h
- src/mongo/s/chunk\_diff\_test.cpp   ()
- src/mongo/s/chunk\_manager\_targeter.cpp   (mongod, tools, mongos)
- src/mongo/s/chunk\_manager\_targeter.h
- src/mongo/s/chunk\_version.h
- src/mongo/s/chunk\_version\_test.cpp   ()
- src/mongo/s/cluster\_client\_internal.cpp   (mongos)
- src/mongo/s/cluster\_client\_internal.h
- src/mongo/s/cluster\_write.cpp   (mongod, tools, mongos)
- src/mongo/s/cluster\_write.h
- src/mongo/s/commands/cluster\_merge\_chunks\_cmd.cpp   (mongos)
- src/mongo/s/config.cpp   (mongod, tools, mongos)
- src/mongo/s/config.h
- src/mongo/s/config\_server\_checker\_service.cpp   (mongod, tools, mongos)
- src/mongo/s/config\_server\_checker\_service.h
- src/mongo/s/config\_server\_tests.cpp   ()
- src/mongo/s/cursors.cpp   (mongos)
- src/mongo/s/cursors.h
- src/mongo/s/d\_logic.cpp   (mongod, tools)
- src/mongo/s/d\_logic.h
- src/mongo/s/d\_merge.cpp   (mongod, tools)
- src/mongo/s/d\_merge.h
- src/mongo/s/d\_migrate.cpp   (mongod, tools)
- src/mongo/s/d\_split.cpp   (mongod, tools)
- src/mongo/s/d\_state.cpp   (mongod, tools)
- src/mongo/s/dbclient\_multi\_command.cpp   (mongod, tools, mongos)
- src/mongo/s/dbclient\_multi\_command.h
- src/mongo/s/dbclient\_shard\_resolver.cpp   (mongod, tools, mongos)
- src/mongo/s/dbclient\_shard\_resolver.h
- src/mongo/s/default\_version.cpp   (mongod, tools)
- src/mongo/s/grid.cpp   (mongod, tools, mongos)
- src/mongo/s/grid.h
- src/mongo/s/mock\_multi\_command.h
- src/mongo/s/mock\_ns\_targeter.h
- src/mongo/s/mock\_shard\_resolver.h
- src/mongo/s/mongo\_version\_range.cpp   (mongod, tools, mongos)
- src/mongo/s/mongo\_version\_range.h
- src/mongo/s/mongo\_version\_range\_test.cpp   ()
- src/mongo/s/mongos\_persistence\_stubs.cpp   (mongos)
- src/mongo/s/multi\_command\_dispatch.h
- src/mongo/s/ns\_targeter.h
- src/mongo/s/request.cpp   (mongos)
- src/mongo/s/request.h
- src/mongo/s/shard.cpp   (mongod, tools, mongos)
- src/mongo/s/shard.h
- src/mongo/s/shard\_conn\_test.cpp   ()
- src/mongo/s/shard\_key\_pattern.cpp   (mongod, tools, mongos)
- src/mongo/s/shard\_key\_pattern.h
- src/mongo/s/shard\_resolver.h
- src/mongo/s/shard\_test.cpp   ()
- src/mongo/s/shardconnection.cpp   (mongod, tools, mongos)
- src/mongo/s/shardkey.cpp   (mongod, tools, mongos)
- src/mongo/s/shardkey.h
- src/mongo/s/stale\_exception.h
- src/mongo/s/strategy.cpp   (mongos)
- src/mongo/s/strategy.h
- src/mongo/s/strategy\_shard.cpp   (mongos)
- src/mongo/s/strategy\_single.cpp   (mongos)
- src/mongo/s/version\_manager.cpp   (mongos)
- src/mongo/s/version\_manager.h
- src/mongo/s/version\_mongos.cpp   (mongos)
- src/mongo/s/version\_mongos.h
