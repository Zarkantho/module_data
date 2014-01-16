# mongos\_and\_mongod\_mains

# Module Groups

-------------

Main for mongod

- src/mongo/db/db.cpp   (mongod)
- src/mongo/db/db.h

## Interface
### src/mongo/db/db.cpp
<pre>mongo::snmpInit</pre>
#### Used By:
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp

-------------

Mongod command line options

- src/mongo/db/mongod\_options.cpp   (mongod)
- src/mongo/db/mongod\_options.h
- src/mongo/db/mongod\_options\_init.cpp   (mongod)
- src/mongo/db/mongod\_options\_test.cpp   ()

## Interface

-------------

Main for mongos

- src/mongo/s/server.cpp   (mongos)
- src/mongo/s/server.h

## Interface
### src/mongo/s/server.cpp
<pre>mongo::createDirectClient()</pre>
#### Used By:
- [src/mongo/scripting/engine.cpp](../javascript\_libraries)
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

<pre>mongo::inShutdown()</pre>
#### Used By:
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/auth/user\_cache\_invalidator\_job.cpp](../authentication)
- [src/mongo/db/repl/bgsync.cpp](../replication)
- [src/mongo/db/range\_deleter.cpp](../sharding)
- [src/mongo/db/dur\_journal.cpp](../journaling)
- [src/mongo/db/storage/durable\_mapped\_file.cpp](../journaling)
- [src/mongo/db/repl/write\_concern.cpp](../replication)
- [src/mongo/db/stats/snapshots.cpp](../utilities)
- [src/mongo/util/concurrency/task.cpp](../utilities)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/s/writeback\_listener.cpp](../sharding)
- [src/mongo/client/distlock.cpp](../sharding)
- [src/mongo/db/clientcursor.cpp](../client\_and\_operation\_tracking)
- [src/mongo/s/balance.cpp](../sharding)
- [src/mongo/util/net/listen.cpp](../network)
- [src/mongo/client/dbclient\_rs.cpp](../cpp\_client\_driver)
- [src/mongo/client/dbclientcursor.cpp](../cpp\_client\_driver)
- [src/mongo/s/shardconnection.cpp](../sharding)
- [src/mongo/db/dur.cpp](../journaling)
- [src/mongo/db/ttl.cpp](../indexing)
- [src/mongo/util/assert\_util.cpp](../utilities)
- [src/mongo/db/client.cpp](../client\_and\_operation\_tracking)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)
- [src/mongo/util/net/message\_server\_port.cpp](../network)
- src/mongo/db/modules/subscription/src/snmp/snmp.cpp
- [src/mongo/s/strategy\_shard.cpp](../sharding)
- [src/mongo/util/concurrency/task.cpp](../utilities)
- [src/mongo/s/config\_server\_checker\_service.cpp](../sharding)
- [src/mongo/db/storage/data\_file.cpp](../mmap\_file\_interface)
- [src/mongo/client/connpool.cpp](../cpp\_client\_driver)

<pre>mongo::dbexit(mongo::ExitCode, char const*)</pre>
#### Used By:
- [src/mongo/s/config.cpp](../sharding)
- [src/mongo/db/catalog/ondisk/namespace\_index.cpp](../storage\_layer\_structure)
- [src/mongo/dbtests/framework.cpp](../unit\_tests)
- [src/mongo/db/dbcommands\_generic.cpp](../database\_commands)
- [src/mongo/db/repl/master\_slave.cpp](../replication)
- [src/mongo/util/net/message\_server\_port.cpp](../network)
- [src/mongo/db/repl/rs.cpp](../replication)
- [src/mongo/tools/tool.cpp](../tools)
- [src/mongo/s/d\_migrate.cpp](../sharding)

<pre>mongo::dbexitCalled</pre>
#### Used By:
- [src/mongo/shell/shell\_utils\_launcher.cpp](../mongo\_shell)
- [src/mongo/shell/dbshell.cpp](../mongo\_shell)

<pre>mongo::haveLocalShardingInfo(std::string const&)</pre>
#### Used By:
- [src/mongo/scripting/v8\_db.cpp](../javascript\_libraries)

-------------

Mongos command line options

- src/mongo/s/mongos\_options.cpp   (mongos)
- src/mongo/s/mongos\_options.h
- src/mongo/s/mongos\_options\_init.cpp   (mongos)
- src/mongo/s/mongos\_options\_test.cpp   ()

## Interface
